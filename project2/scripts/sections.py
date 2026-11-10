"""Project 2: concept counts per chapter of one Council document.

Usage:
    python project2/scripts/sections.py RC2026

Reads data/text/<id>.txt, splits it at the chapter headings listed in
project2/vocab/sections_<id>.txt (one heading per line, as printed in the
document), and counts (a) the 23 tracker concepts (vocab/concepts.csv, same
rules as Project 1) and (b) the provisional candidate concepts in
project2/vocab/candidate_concepts.csv. Writes project2/data/sections_<id>.csv.

The table of contents repeats every heading, so the last occurrence of each
heading is taken as the start of the chapter body. Text after the stop marker
(first line of the file starting with 'STOP:') is excluded (appendix, sources).
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import vocabulary as v  # noqa: E402

P2 = ROOT / "project2"


def main(doc_id: str) -> None:
    text = v.clean((ROOT / "data" / "text" / f"{doc_id}.txt").read_text(encoding="utf-8"), True)
    lines = (P2 / "vocab" / f"sections_{doc_id}.txt").read_text(encoding="utf-8").splitlines()
    heads = [l for l in lines if l.strip() and not l.startswith("STOP:")]
    stop = next((l[5:].strip() for l in lines if l.startswith("STOP:")), None)

    starts = []
    for h in heads:
        hits = [m.start() for m in re.finditer(r"(?m)^" + re.escape(h), text)]
        if not hits:
            raise SystemExit(f"heading not found: {h!r}")
        starts.append((hits[-1], h))
    starts.sort()
    end = len(text)
    if stop:
        m = re.search(r"(?m)^" + re.escape(stop), text[starts[-1][0]:])
        if m:
            end = starts[-1][0] + m.start()

    exclude = v.load_exclusions()
    concepts = v.load_concepts()
    with open(P2 / "vocab" / "candidate_concepts.csv", encoding="utf-8") as f:
        cands = [dict(r, regex=re.compile(r["pattern"], re.I)) for r in csv.DictReader(f)]

    rows = []
    for i, (s, h) in enumerate(starts):
        chunk = text[s:(starts[i + 1][0] if i + 1 < len(starts) else end)]
        words = len(v.WORD.findall(chunk))
        if exclude:
            chunk = exclude.sub(" [INSTITUTION] ", chunk)
        for c in concepts:
            n = sum(1 for m in c["regex"].finditer(chunk) if v.keep_hit(c, chunk, m))
            rows.append({"document_id": doc_id, "section": h, "words": words, "concept_id": c["concept_id"],
                         "kind": "tracker_v0.1", "count": n})
        for c in cands:
            rows.append({"document_id": doc_id, "section": h, "words": words, "concept_id": c["concept_id"],
                         "kind": "candidate_provisional", "count": len(c["regex"].findall(chunk))})

    out = P2 / "data" / f"sections_{doc_id}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(starts)} sections -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "RC2026")
