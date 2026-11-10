"""Check that every excerpt in a claims CSV appears verbatim in its source text.

Usage:
    python project1/coding/verify_excerpts.py project1/coding/claims_gold_draft_v0.csv

Reads data/text/<document_id>.txt. Only whitespace and line-break hyphens are
normalised (genuine compounds such as "tutkimus- ja" are kept). '…' in an
excerpt marks a gap; each part must be found. Writes excerpt_verified back.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def norm(t: str) -> str:
    t = re.sub(r"\[\[page \d+\]\]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"([a-zåäö]) ?- (?!(?:ja|sekä|tai|eli|että|kuin|and|or)\b)([a-zåäö])", r"\1\2", t)


def main(path: str) -> None:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    cache, missing = {}, 0
    for r in rows:
        d = r["document_id"]
        if d not in cache:
            f = ROOT / "data" / "text" / f"{d}.txt"
            cache[d] = norm(f.read_text(encoding="utf-8")) if f.exists() else None
        if cache[d] is None:
            r["excerpt_verified"] = "no text"
            continue
        ok = all(norm(p).strip() in cache[d] for p in r["excerpt_verbatim"].split("…") if p.strip())
        r["excerpt_verified"] = "yes" if ok else "NO"
        missing += not ok
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} claims checked, {missing} not found")


if __name__ == "__main__":
    main(sys.argv[1])
