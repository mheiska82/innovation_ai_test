"""Fetch the corpus listed in a CSV and save raw files plus extracted text.

Usage:
    python scripts/fetch_corpus.py project1/corpus/programmes.csv   # Project 1
    python scripts/fetch_corpus.py project2/corpus/council.csv      # Project 2

For each row with a URL it downloads the page or PDF to data/raw/, extracts
plain text to data/text/<id>.txt and writes a manifest (data/manifest_<corpus name>.csv)
recording what worked. Government programmes whose URL is missing or broken
are looked up on the valtioneuvosto.fi index page by their number.

PDFs without a text layer are flagged as `needs_ocr`; run
    ocrmypdf -l fin data/raw/<id>.pdf data/raw/<id>.ocr.pdf
and re-run this script to pick up the OCR'd version.
"""

from __future__ import annotations

import csv
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
TEXT = ROOT / "data" / "text"
MANIFEST = ROOT / "data" / "manifest.csv"
INDEX_URL = "https://valtioneuvosto.fi/historia-ja-rakennukset/hallitusohjelmat"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) innovation-state-research/0.2"}
PAUSE_S = 1.5  # be polite to public servers

_index_links: dict[int, str] | None = None


def index_links() -> dict[int, str]:
    """Map government number -> programme URL, scraped from the index page."""
    global _index_links
    if _index_links is None:
        _index_links = {}
        try:
            html = requests.get(INDEX_URL, headers=HEADERS, timeout=30).text
            for a in BeautifulSoup(html, "html.parser").find_all("a", href=True):
                m = re.match(r"^/-/(\d{1,2})[.-]", a["href"])
                if m:
                    _index_links.setdefault(int(m.group(1)), urljoin(INDEX_URL, a["href"]))
        except requests.RequestException as e:
            print(f"  index page unavailable: {e}")
    return _index_links


# Page chrome on valtioneuvosto.fi that is not part of the document
_DROP_LINES = {"suomi", "svenska", "english", "läs artikeln på svenska",
               "read article in english", "hallitusohjelmat vuodesta 1917",
               "piilotettu", "sivun alkuun"}
# Everything from these lines on is contacts, tags or related news
_CUT_AT = ("Lisätietoja:", "Tutustu myös")


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()
    # valtioneuvosto.fi: the document is the largest journal-content-article block
    blocks = soup.select("div.journal-content-article")
    if blocks:
        main = max(blocks, key=lambda d: len(d.get_text(" ", strip=True).split()))
    else:
        main = soup.find("main") or soup.find("article") or soup.body or soup
    lines = []
    for line in main.get_text("\n", strip=True).splitlines():
        if line.strip().startswith(_CUT_AT):
            break
        if line.strip().lower() not in _DROP_LINES:
            lines.append(line)
    return "\n".join(lines)


VALTO = "https://julkaisut.valtioneuvosto.fi"


def valto_pdf_url(page_url: str, html: str) -> str | None:
    """Valto (julkaisut.valtioneuvosto.fi, DSpace 7) item page -> URL of its PDF.

    urn.fi links resolve to the item's landing page, not the file. Ask the
    DSpace REST API for the item's ORIGINAL bundle; fall back to scanning the
    page for a bitstream download link.
    """
    m = re.search(r"/items/([0-9a-f-]{36})", page_url)
    if m:
        try:
            api = f"{VALTO}/server/api/core/items/{m.group(1)}/bundles?embed=bitstreams"
            data = requests.get(api, headers=HEADERS, timeout=30).json()
            for bundle in data.get("_embedded", {}).get("bundles", []):
                if bundle.get("name") != "ORIGINAL":
                    continue
                for bs in bundle.get("_embedded", {}).get("bitstreams", {}).get("_embedded", {}).get("bitstreams", []):
                    if bs.get("name", "").lower().endswith(".pdf"):
                        return bs["_links"]["content"]["href"]
        except (requests.RequestException, ValueError, KeyError):
            pass
    m = re.search(r'href="([^"]*/bitstreams/[0-9a-f-]{36}/download)"', html)
    return urljoin(page_url, m.group(1)) if m else None


def pdf_to_text(path: Path) -> str:
    from pypdf import PdfReader

    pages = []
    for i, page in enumerate(PdfReader(path).pages, start=1):
        pages.append(f"\n[[page {i}]]\n{page.extract_text() or ''}")
    return "".join(pages)


def fetch(row: dict) -> tuple[str, str]:
    """Return (status, detail) for one corpus row."""
    doc_id, url = row["id"], row["url"].strip()

    ocr = RAW / f"{doc_id}.ocr.pdf"
    if ocr.exists():
        (TEXT / f"{doc_id}.txt").write_text(pdf_to_text(ocr), encoding="utf-8")
        return "ok", "pdf_ocr"
    manual = RAW / f"{doc_id}.pdf"
    if manual.exists():  # a saved PDF (manual or earlier download) wins over the URL
        text = pdf_to_text(manual)
        if len(text.replace("[[page", "").strip()) < 500:
            return "needs_ocr", str(manual)
        (TEXT / f"{doc_id}.txt").write_text(text, encoding="utf-8")
        return "ok", "pdf_text (manual download)"

    resp = _get(url) if url else None
    if (resp is None or resp.status_code != 200) and row["series"] == "government_programme":
        # Fallback: look the programme up on the index page by its number
        alt = index_links().get(int(doc_id.removeprefix("GP")), "")
        if alt and alt != url:
            url, resp = alt, _get(alt)
    if resp is None:
        return "missing_url", row.get("notes", "")
    if resp.status_code != 200:
        return "http_error", f"{resp.status_code} {url} (download manually into data/raw/{doc_id}.pdf)"
    url = resp.url  # after redirects
    if "julkaisut.valtioneuvosto.fi" in url and "pdf" not in resp.headers.get("Content-Type", ""):
        pdf = valto_pdf_url(url, resp.text)
        if not pdf:
            return "needs_manual", f"Valto page without PDF link: {url}"
        url, resp = pdf, _get(pdf)
        if resp is None or resp.status_code != 200:
            return "http_error", f"{getattr(resp, 'status_code', '?')} {url}"

    ctype = resp.headers.get("Content-Type", "")
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        raw = RAW / f"{doc_id}.pdf"
        raw.write_bytes(resp.content)
        text = pdf_to_text(raw)
        if len(text.replace("[[page", "").strip()) < 500:
            return "needs_ocr", str(raw)
        quality = "pdf_text"
    else:
        (RAW / f"{doc_id}.html").write_text(resp.text, encoding="utf-8")
        text = html_to_text(resp.text)
        quality = "html"

    (TEXT / f"{doc_id}.txt").write_text(text, encoding="utf-8")
    return "ok", f"{quality} {len(text.split())} words {url}"


def _get(url: str, tries: int = 3) -> requests.Response | None:
    """GET with retries. (No HEAD requests: valtioneuvosto.fi rejects them.)"""
    for attempt in range(tries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=60, allow_redirects=True)
        except requests.RequestException:
            resp = None
        if resp is not None and resp.status_code not in (429, 500, 502, 503):
            return resp
        time.sleep(5 * (attempt + 1))
    return resp


def main(csv_path: str) -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    TEXT.mkdir(parents=True, exist_ok=True)
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    results = []
    for row in rows:
        if row["url_status"].startswith("same_as:"):
            results.append({"id": row["id"], "status": "skipped", "detail": row["url_status"]})
            continue
        if row["series"] == "benchmark" or row["url_status"] in ("library", "gap_no_access"):
            results.append({"id": row["id"], "status": "skipped", "detail": row["url_status"]})
            continue
        try:
            status, detail = fetch(row)
        except Exception as e:  # keep going; the manifest records the failure
            status, detail = "error", repr(e)
        print(f"{row['id']:<8} {status:<12} {detail}")
        results.append({"id": row["id"], "status": status, "detail": detail})
        time.sleep(PAUSE_S)

    stem = Path(csv_path).stem
    manifest = MANIFEST.with_name(f"manifest_{stem}.csv")
    with open(manifest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "status", "detail"])
        w.writeheader()
        w.writerows(results)

    ok = sum(r["status"] == "ok" for r in results)
    print(f"\n{ok}/{len(results)} documents saved. Manifest: {manifest}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "project1" / "corpus" / "programmes.csv"))
