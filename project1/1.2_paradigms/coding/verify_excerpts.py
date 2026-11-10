"""Check that every excerpt in a claims CSV appears verbatim in its source text.

Usage:
    python project1/1.2_paradigms/coding/verify_excerpts.py project1/1.2_paradigms/coding/claims_v0.3.csv

Reads data/text/<document_id>.txt. Two tiers:
  1. 'yes'  -- found after normalising whitespace and line-break hyphens only
               (genuine compounds such as "tutkimus- ja" are kept).
  2. 'yes (PDF spacing)' -- found only after also removing all spaces,
               hyphens, soft hyphens and page headers. Needed for PDFs whose
               text layer splits words ("kilpa ilukykyinen"); the excerpt is
               written in clean Finnish and the letters match exactly.
'…' in an excerpt marks a gap; each part must be found. Also fills `page`
(the PDF page where the excerpt starts) when it is empty.
Writes excerpt_verified (and page) back.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAGE = re.compile(r"\[\[page (\d+)\]\]")


def norm(t: str) -> str:
    t = t.replace("\u00ad", "")
    t = PAGE.sub(" ", t)
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"([a-zåäö]) ?- (?!(?:ja|sekä|tai|eli|että|kuin|and|or)\b)([a-zåäö])", r"\1\2", t)


SQUASH = re.compile("[\\s\u00ad\\-\u2013\x00-\x1f]")


def squash(t: str) -> str:
    t = re.sub(r"\[\[page \d+\]\]\s*\d*", "", t)
    return SQUASH.sub("", t)


def page_of(raw: str, part: str) -> str:
    """PDF page on which the excerpt starts (pages are split on [[page N]])."""
    pieces = PAGE.split(raw)  # [before, n1, text1, n2, text2, ...]
    offsets, joined, pos = [], "", 0
    for i in range(1, len(pieces), 2):
        seg = squash(re.sub(r"^\s*\d*", "", pieces[i + 1]))
        offsets.append((pos, pieces[i]))
        joined += seg
        pos += len(seg)
    k = joined.find(squash(part)[:60])
    if k < 0:
        return ""
    page = ""
    for start, n in offsets:
        if start <= k:
            page = n
    return page


def main(path: str) -> None:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    cache = {}
    counts = {"yes": 0, "yes (PDF spacing)": 0, "NO": 0, "no text": 0}
    for r in rows:
        d = r["document_id"]
        if d not in cache:
            f = ROOT / "data" / "text" / f"{d}.txt"
            raw = f.read_text(encoding="utf-8") if f.exists() else None
            cache[d] = (raw, norm(raw), squash(raw)) if raw else None
        if cache[d] is None:
            r["excerpt_verified"] = "no text"
            counts["no text"] += 1
            continue
        raw, n1, n2 = cache[d]
        parts = [p.strip() for p in r["excerpt_verbatim"].split("…") if p.strip()]
        if all(norm(p).strip() in n1 for p in parts):
            r["excerpt_verified"] = "yes"
        elif all(squash(p) in n2 for p in parts):
            r["excerpt_verified"] = "yes (PDF spacing)"
        else:
            r["excerpt_verified"] = "NO"
        counts[r["excerpt_verified"]] += 1
        if "page" in r and not r["page"] and r["excerpt_verified"] != "NO":
            r["page"] = page_of(raw, parts[0]) if PAGE.search(raw) else "web text"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} claims checked:", counts)


if __name__ == "__main__":
    main(sys.argv[1])
