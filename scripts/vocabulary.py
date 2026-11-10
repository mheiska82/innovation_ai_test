"""Count policy concepts per document: the vocabulary tracker (lexical v0.1).

Usage:
    python scripts/vocabulary.py                      # government programmes
    python scripts/vocabulary.py --series all         # every downloaded document
    python scripts/vocabulary.py --series council_review --no-pooling --out project2/data   # Project 2

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
        # optional context rules: a hit counts only if a `near` stem is within
        # WINDOW characters, and no `not_near` stem is
        for key in ("near", "not_near"):
            ctx = [p.strip().lower() for p in (c.get(key) or "").split("|") if p.strip()]
            c[key + "_re"] = re.compile("|".join(re.escape(x) for x in ctx), re.IGNORECASE) if ctx else None
    return concepts


WINDOW = 150


def keep_hit(c: dict, text: str, m: re.Match) -> bool:
    ctx = text[max(0, m.start() - WINDOW): m.end() + WINDOW]
    if c["near_re"] and not c["near_re"].search(ctx):
        return False
    if c["not_near_re"] and c["not_near_re"].search(ctx):
        return False
    return True


def clean(text: str, is_pdf: bool) -> str:
    """Remove page markers and table-of-contents lines; undo PDF line-break hyphenation."""
    text = re.sub(r"\[\[page \d+\]\]", " ", text)
    # table-of-contents lines ("6.1 Koulutus- ja tiedepolitiikka ........ 21")
    text = "\n".join(l for l in text.splitlines() if not re.search(r"\.{5,}|…{3,}", l))
    if is_pdf:
        # "kilpailuky- kyä" -> "kilpailukykyä", "in - novaatio" -> "innovaatio";
        # keep real compounds such as "tutkimus- ja kehitys"
        text = re.sub(r"([a-zåäö])\s?-\s+(?!(?:ja|sekä|tai|eli|että|kuin)\b)([a-zåäö])", r"\1\2", text)
    return text


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
    paths = sorted((ROOT / "corpus").glob("*.csv")) + sorted((ROOT / "project2" / "corpus").glob("*.csv"))
    for path in paths:
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


def shingles(text: str, n: int = 5) -> set[tuple[str, ...]]:
    words = [w.lower() for w in WORD.findall(text)]
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def check_near_duplicates(texts: dict[str, str], corpus: dict[str, dict], threshold: float = 0.5) -> None:
    """Warn when a programme largely repeats the previous one.

    Containment = share of the shorter document's 5-word sequences that also
    appear in the longer one. Above the threshold, consider marking the later
    document same_as:<earlier id> in the corpus CSV so it is counted once.
    """
    ids = sorted((i for i in texts if corpus[i]["series"] == "government_programme"),
                 key=lambda i: corpus[i]["date"])
    found = False
    for a, b in zip(ids, ids[1:]):
        sa, sb = shingles(texts[a]), shingles(texts[b])
        if not sa or not sb:
            continue
        containment = len(sa & sb) / min(len(sa), len(sb))
        if containment >= threshold:
            found = True
            print(f"  near-duplicate: {b} repeats {containment:.0%} of {a} -> consider url_status same_as:{a}")
    if not found:
        print("  no near-duplicate programmes found")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", default="government_programme", help="corpus series to include, or 'all'")
    ap.add_argument("--no-pooling", action="store_true", help="skip the pooled decade file (Project 2 analyses each document separately)")
    ap.add_argument("--out", default=str(OUT), help="output folder (Project 2: project2/data)")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    concepts, corpus, exclude = load_concepts(), load_corpus(), load_exclusions()
    by_doc, examples = [], []
    decade_words: dict[int, int] = defaultdict(int)
    decade_hits: dict[tuple[int, str], int] = defaultdict(int)
    decade_docs: dict[int, list[str]] = defaultdict(list)
    seen_examples: dict[tuple[int, str], int] = defaultdict(int)
    texts: dict[str, str] = {}

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
        raw = path.read_text(encoding="utf-8")
        text = clean(raw, is_pdf="[[page " in raw)
        texts[doc_id] = text
        n_words = len(WORD.findall(text))  # counted before exclusions
        if exclude:
            text = exclude.sub(" [INSTITUTION] ", text)
        if n_words == 0:
            continue
        decade = year // 10 * 10
        decade_words[decade] += n_words
        decade_docs[decade].append(doc_id)

        for c in concepts:
            hits = [m for m in c["regex"].finditer(text) if keep_hit(c, text, m)]
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

    outputs = [("vocabulary_by_document", by_doc), ("vocabulary_examples", examples)]
    if not args.no_pooling:
        outputs.insert(1, ("vocabulary_by_decade", by_decade))
    for name, rows in outputs:
        if rows:
            with open(out / f"{name}.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)

    print("Duplicate check:")
    check_near_duplicates(texts, corpus)

    # Console summary: top concepts per decade
    print(f"{'decade':<8}{'docs':>5}{'words':>8}  top concepts (per 10k words)")
    for decade in sorted(decade_words):
        top = sorted((r for r in by_decade if r["decade"] == decade), key=lambda r: -r["per_10k_words"])[:5]
        tops = ", ".join(f"{r['concept_id']} {r['per_10k_words']}" for r in top if r["count"])
        print(f"{decade}s{len(decade_docs[decade]):>6}{decade_words[decade]:>8}  {tops}")


if __name__ == "__main__":
    main()
