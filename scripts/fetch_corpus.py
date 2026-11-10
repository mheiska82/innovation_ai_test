"""Fetch the corpus listed in a CSV and save raw files plus extracted text.

Usage:
    python scripts/fetch_corpus.py corpus/batch1.csv

For each row with a URL it downloads the page or PDF to data/raw/, extracts
plain text to data/text/<id>.txt and writes a manifest (data/manifest.csv)
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
HEADERS = {"User-Agent": "innovation-state-research/0.1 (academic research)"}
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


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    text = main.get_text("\n", strip=True)
    return re.sub(r"\n{3,}", "\n\n", text)


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

    if row["series"] == "government_programme":
        num = int(doc_id.removeprefix("GP"))
        if not url or not _reachable(url):
            url = index_links().get(num, "")
    if not url:
        return "missing_url", row.get("notes", "")

    resp = requests.get(url, headers=HEADERS, timeout=60)
    if resp.status_code != 200:
        return "http_error", f"{resp.status_code} {url}"

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


def _reachable(url: str) -> bool:
    try:
        return requests.head(url, headers=HEADERS, timeout=20, allow_redirects=True).status_code == 200
    except requests.RequestException:
        return False


def main(csv_path: str) -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    TEXT.mkdir(parents=True, exist_ok=True)
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    results = []
    for row in rows:
        if row["series"] == "benchmark" or row["url_status"] == "library":
            results.append({"id": row["id"], "status": "skipped", "detail": row["url_status"]})
            continue
        try:
            status, detail = fetch(row)
        except Exception as e:  # keep going; the manifest records the failure
            status, detail = "error", repr(e)
        print(f"{row['id']:<8} {status:<12} {detail}")
        results.append({"id": row["id"], "status": status, "detail": detail})
        time.sleep(PAUSE_S)

    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "status", "detail"])
        w.writeheader()
        w.writerows(results)

    ok = sum(r["status"] == "ok" for r in results)
    print(f"\n{ok}/{len(results)} documents saved. Manifest: {MANIFEST}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "corpus" / "batch1.csv"))
