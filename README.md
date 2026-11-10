# Tracing Finland's Innovation State

An AI research tool for Finnish innovation-policy history (1960s–today), built on public documents only. Every claim links to the exact passage that supports it.

## Structure

```
corpus/batch1.csv          Project 1: 32 government programmes (1961–2023), 2 human benchmarks
project2/                  Project 2: Research and Innovation Council reviews
                           (own corpus, docs, outputs; see project2/PROJECT2.md)
db/schema.sql              Postgres + pgvector schema (documents, claims, evidence, entities)
prompts/claim_extraction.md  Extraction prompt v0.1 and output schema
scripts/fetch_corpus.py    Downloads the corpus and extracts text
data/                      raw/ and text/ (git-ignored)
```

## Corpus status (batch 1)

`url_status` in the CSV:

- `verified`: link confirmed (16)
- `pattern`: government programme URL built from the site's pattern; the script falls back to the index page if it fails (11)
- `locate`: title known, link still to find (22); mostly post-2003 programmes and Council reviews
- `library`: catalogue record only; request or scan via the National Library (3)

The benchmark rows (Eela 2001, Lemola 2001, Lemola 2020) are not corpus. They are human analyses to compare the AI's findings against.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/fetch_corpus.py corpus/batch1.csv
```

Database (when you reach extraction):

```bash
createdb innovation_state
psql -d innovation_state -f db/schema.sql
```

OCR for scanned PDFs (flagged `needs_ocr` in `data/manifest.csv`):

```bash
# macOS: brew install ocrmypdf tesseract-lang
ocrmypdf -l fin data/raw/<id>.pdf data/raw/<id>.ocr.pdf
```

## Vocabulary tracker

```bash
python scripts/vocabulary.py               # government programmes only
python scripts/vocabulary.py --series all  # every downloaded document
# Project 2 (Council reviews), each document separately:
python scripts/fetch_corpus.py project2/corpus/council.csv
python scripts/vocabulary.py --series council_review --no-pooling --out project2/data
python project2/scripts/sections.py RC2026
```

Counts 23 policy concepts (`vocab/concepts.csv`, Finnish word stems) per document and per decade, as mentions per 10,000 words. Decade rates are pooled, so very short programmes can't swing a decade. Institution names in `vocab/exclude.txt` are removed first (the Research and Innovation Council's name is not a mention of "innovation"). `data/vocabulary_examples.csv` shows matched passages so every number can be checked.

Edit the stems in `concepts.csv` freely: add a `|`-separated variant, re-run, compare.

## Ground rules

- Public sources only; no Business Finland internal data or code.
- No profiling of named individuals: institutions and roles only.
- Evidence, extracted relations and interpretations are stored as separate layers.
