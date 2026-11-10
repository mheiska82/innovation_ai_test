"""Count policy concepts per document: the vocabulary tracker (lexical v0.1).

Usage:
    python scripts/vocabulary.py                      # government programmes
    python scripts/vocabulary.py --series all         # every downloaded document

Reads data/text/<id>.txt and corpus/*.csv, matches the stem patterns in
vocab/concepts.csv, and writes:

    data/vocabulary_by_document.csv   one row per document x concept
    data/vocabulary_by_decade.csv     pooled rate per decade x concept
    data/vocabulary_examples.csv      up to 3 matched passages per concept and
                                      decade, so every number can be checked

Rates are mentions per 10,000 words. Decade rates are pooled (all mentions
divided by all words in the decade), so a 150-word programme can't swing a
decade on its own. Documents marked same_as:<id> are skipped.

Patterns are word-start stems ("innovaati" matches innovaatio, innovaatioiden,
innovaatiopolitiikka...). This is deliberately simple and transparent; the
LLM pass later catches ideas expressed without these words.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT = ROOT / "data" / "text"
OUT = ROOT / "data"
WORD = re.compile(r"[\wåäöÅÄÖ&-]+", re.UNICODE)


def load_concepts() -> list[dict]:
    with open(ROOT / "vocab" / "concepts.csv", encoding="utf-8") as f:
        concepts = list(csv.DictReader(f))
    for c in concepts:
        stems = [p.strip().lower() for p in c["patterns"].split("|") if p.strip()]
        # word-start match; stems may contain spaces, hyphens, & and commas
        c["regex"] = re.compile(r"(?<![\wåäö])(?:" + "|".join(re.escape(s) for s in stems) + ")", re.IGNORECASE)
    return concepts


def load_exclusions() -> re.Pattern | None:
    path = ROOT / "vocab" / "exclude.txt"
    stems = [l.strip().lower() for l in path.read_text(encoding="utf-8").splitlines()
             if l.strip() and not l.startswith("#")] if path.exists() else []
    if not stems:
        return None
    # remove the whole inflected word that starts with the stem
    return re.compile(r"(?<![\wåäö])(?:" + "|".join(re.escape(s) for s in stems) + r")[\wåäö]*", re.IGNORECASE)


def load_corpus() -> dict[str, dict]:
    docs = {}
    for path in sorted((ROOT / "corpus").glob("*.csv")):
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                docs[row["id"]] = row
    return docs


def year_of(row: dict) -> int | None:
    m = re.match(r"(\d{4})", row.get("date", ""))
    return int(m.group(1)) if m else None


def snippet(text: str, start: int, end: int, width: int = 90) -> str:
    a, b = max(0, start - width), min(len(text), end + width)
    return ("…" if a else "") + " ".join(text[a:b].split()) + ("…" if b < len(text) else "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", default="government_programme", help="corpus series to include, or 'all'")
    args = ap.parse_args()

    concepts, corpus, exclude = load_concepts(), load_corpus(), load_exclusions()
    by_doc, examples = [], []
    decade_words: dict[int, int] = defaultdict(int)
    decade_hits: dict[tuple[int, str], int] = defaultdict(int)
    decade_docs: dict[int, list[str]] = defaultdict(list)
    seen_examples: dict[tuple[int, str], int] = defaultdict(int)

    for path in sorted(TEXT.glob("*.txt")):
        doc_id = path.stem
        row = corpus.get(doc_id)
        if not row or row["url_status"].startswith("same_as:") or row["series"] == "benchmark":
            continue
        if args.series != "all" and row["series"] != args.series:
            continue
        year = year_of(row)
        if year is None:
            continue
        text = re.sub(r"\[\[page \d+\]\]", " ", path.read_text(encoding="utf-8"))
        n_words = len(WORD.findall(text))  # counted before exclusions
        if exclude:
            text = exclude.sub(" [INSTITUTION] ", text)
        if n_words == 0:
            continue
        decade = year // 10 * 10
        decade_words[decade] += n_words
        decade_docs[decade].append(doc_id)

        for c in concepts:
            hits = list(c["regex"].finditer(text))
            by_doc.append({
                "document_id": doc_id, "series": row["series"], "year": year, "decade": decade,
                "words": n_words, "concept_id": c["concept_id"], "group": c["group"],
                "count": len(hits), "per_10k_words": round(len(hits) / n_words * 10_000, 2),
            })
            decade_hits[(decade, c["concept_id"])] += len(hits)
            for h in hits:
                key = (decade, c["concept_id"])
                if seen_examples[key] >= 3:
                    break
                seen_examples[key] += 1
                examples.append({"decade": decade, "concept_id": c["concept_id"], "document_id": doc_id,
                                 "match": h.group(0), "passage": snippet(text, h.start(), h.end())})

    by_decade = []
    for decade in sorted(decade_words):
        for c in concepts:
            hits = decade_hits[(decade, c["concept_id"])]
            by_decade.append({
                "decade": decade, "concept_id": c["concept_id"], "label_en": c["label_en"], "group": c["group"],
                "count": hits, "words": decade_words[decade], "documents": len(decade_docs[decade]),
                "per_10k_words": round(hits / decade_words[decade] * 10_000, 2),
            })

    for name, rows in [("vocabulary_by_document", by_doc), ("vocabulary_by_decade", by_decade),
                       ("vocabulary_examples", examples)]:
        if rows:
            with open(OUT / f"{name}.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)

    # Console summary: top concepts per decade
    print(f"{'decade':<8}{'docs':>5}{'words':>8}  top concepts (per 10k words)")
    for decade in sorted(decade_words):
        top = sorted((r for r in by_decade if r["decade"] == decade), key=lambda r: -r["per_10k_words"])[:5]
        tops = ", ".join(f"{r['concept_id']} {r['per_10k_words']}" for r in top if r["count"])
        print(f"{decade}s{len(decade_docs[decade]):>6}{decade_words[decade]:>8}  {tops}")


if __name__ == "__main__":
    main()
