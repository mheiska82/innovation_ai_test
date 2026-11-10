# Tracing Finland's Innovation State

An AI research tool for Finnish innovation-policy history (1960s–today), built on public documents only. Every number links to the exact passages it counts.

It is a personal side project. It uses public data only, with no Business Finland internal data or code, and it does not profile named individuals.

## Two projects

| | Project 1: Government programmes | Project 2: Research and Innovation Council reviews |
|---|---|---|
| Documents | 30 *hallitusohjelmat*, 1961–2023 | 15 Council reviews and decisions, 1973–2026 (4 counted so far) |
| Overview | [project1/PROJECT1.md](project1/PROJECT1.md) | [project2/PROJECT2.md](project2/PROJECT2.md) |
| Corpus list | [project1/corpus/programmes.csv](project1/corpus/programmes.csv) | [project2/corpus/council.csv](project2/corpus/council.csv) |
| Results | [Dashboard 1](https://claude.ai/artifact/8K3c4xNdN4Ppdoh8b2S1rr) | [Dashboard 2](https://claude.ai/artifact/QuE38nxXvvPoXBvLtKEMpB) |
| Sub-projects | [1.1 Vocabulary](project1/1.1_vocabulary/README.md) · [1.2 Paradigms (theory of prosperity, analysis v3)](project1/1.2_paradigms/analysis_q2_v3.md) · [1.3 Continuity (planned)](project1/1.3_continuity/README.md) | [project2/docs/](project2/docs/) |

The two series are different genres: coalition agreements versus expert policy guidelines. They are analysed separately, and compared only government by government.

## Repository layout

```
README.md                      this overview
project1/                      Project 1: government programmes
  PROJECT1.md                  overview, research questions, sub-projects
  corpus/programmes.csv        shared corpus list (32 programmes, 2 human benchmarks, 5 context documents)
  1.1_vocabulary/              Q1 vocabulary: README (method, results), data/ (tracker outputs)
  1.2_paradigms/               Q2 theory of prosperity: analysis_q2_v3.md, coding/ (guide, claims v0.4,
                               scope log, excerpt checker), data/ (engine counts), archive/ (v1, v2)
  1.3_continuity/              Q3 continuity or break: plan
project2/                      Project 2: Council reviews
  PROJECT2.md                  description, corpus gaps, method, results
  corpus/council.csv           corpus list (15 Council documents, 4 anchors, 1 benchmark)
  docs/                        document analyses (RC2026; RC2026 chapters 5–6)
  data/                        tracker outputs, chapter counts, passages
  scripts/sections.py          chapter-level counts
  vocab/                       provisional candidate concepts, chapter headings
scripts/                       shared: fetch_corpus.py (download + text), vocabulary.py (tracker)
vocab/                         shared: concepts.csv (23 concepts), exclude.txt (institution names)
prompts/claim_extraction.md    shared: LLM extraction prompt (stage 2)
db/schema.sql                  shared: claims-and-evidence database (stage 2)
data/raw, data/text            downloaded documents and extracted text (git-ignored, shared)
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
# Project 1: government programmes
python scripts/fetch_corpus.py project1/corpus/programmes.csv
python scripts/vocabulary.py                    # writes project1/1.1_vocabulary/data/
python project1/1.2_paradigms/coding/verify_excerpts.py project1/1.2_paradigms/coding/claims_v0.4.csv

# Project 2: Council reviews, each document separately
python scripts/fetch_corpus.py project2/corpus/council.csv
python scripts/vocabulary.py --series council_review --no-pooling --out project2/data
python project2/scripts/sections.py RC2026
```

A PDF saved by hand as `data/raw/<ID>.pdf` (for example `data/raw/RC2014.pdf`) always takes priority over the web address in the corpus list. Each run writes a log to `data/manifest_<corpus name>.csv`.

**OCR for scanned PDFs** (flagged `needs_ocr` in the log):

```bash
# macOS: brew install ocrmypdf tesseract-lang
ocrmypdf -l fin data/raw/<id>.pdf data/raw/<id>.ocr.pdf
```

**Database** (for the claim-extraction stage):

```bash
createdb innovation_state
psql -d innovation_state -f db/schema.sql
```

## The vocabulary tracker

It counts 23 policy concepts (`vocab/concepts.csv`, Finnish word stems) as mentions per 10,000 words. Institution names in `vocab/exclude.txt` are removed first; for example, the Research and Innovation Council's name is not a mention of "innovation". The example-passage outputs show the matched text, so every number can be checked. To try a change, add a `|`-separated variant to a stem in `concepts.csv`, re-run and compare.

## Ground rules

- Public sources only; no Business Finland internal data or code.
- No profiling of named individuals: institutions and roles only.
- Evidence, extracted relations and interpretations are stored as separate layers.
- Corpus gaps are stated openly (see project2/PROJECT2.md).
