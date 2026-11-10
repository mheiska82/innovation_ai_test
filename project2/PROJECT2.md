# Project 2: the Research and Innovation Council reviews

*Part of [Tracing Finland's Innovation State](../docs/PROJECT.md). Status: 10 November 2026. Public documents only.*

- **Dashboard 2:** [Council reviews](https://claude.ai/artifact/QuE38nxXvvPoXBvLtKEMpB). It is a skeleton: 2 of 15 Council documents are counted so far.
- **Code:** shared with Project 1 (`scripts/`), plus `project2/scripts/`.

## 1. What this project is

Project 1 traces policy vocabulary in **government programmes** (*hallitusohjelmat*), 1961–2023. Project 2 does the same for the **expert-advisory series**: the reviews, policy guidelines and decisions of the Council. It was called Valtion tiedeneuvosto, then Tiede- ja teknologianeuvosto (from 1987), and has been Tutkimus- ja innovaationeuvosto since 2009.

The two series are different genres. Programmes are political coalition agreements; Council documents are expert-led policy guidelines chaired by the Prime Minister. They are therefore analysed **separately**. They are compared only government by government, and only once enough Council documents are in (see §6).

## 2. Research questions

1. **Council vocabulary over time.** Which concepts dominate the Council documents in each period?
2. **Who came first?** Did Council documents use concepts such as *kansallinen innovaatiojärjestelmä* (national innovation system) before the government programmes did? This question needs dated documents from both series.
3. **The newest turn.** Is the security, resilience and data vocabulary of the 2026 strategic choices new, or was it prepared in earlier Council documents? See the hypotheses in [analysis_RC2026.md](docs/analysis_RC2026.md).

## 3. Corpus

The list is in `project2/corpus/council.csv` (20 rows): 15 Council documents, 4 anchor documents and 1 human benchmark.

| ID | Document | Government | Status |
|---|---|---|---|
| RC1973 | Valtion tiedeneuvoston katsaukset 1973–1986 | several | **Gap**: library only |
| RC1987 | Tiede- ja teknologianeuvoston katsaus 1987 | Sorsa IV or Holkeri (date to confirm) | **Gap**: library only |
| RC1990 | Katsaus 1990 | Holkeri | **Gap**: library only |
| RC1993 | Katsaus 1993 | Aho | **Gap**: library only |
| RC1996 | Katsaus 1996 | Lipponen I | **Gap**: library only |
| RC2000 | Katsaus 2000: tiedon ja osaamisen haasteet | Lipponen II | **Gap**: library only |
| RC2003 | Osaaminen, innovaatiot ja kansainvälistyminen | Lipponen II (date to confirm) | Retired minedu.fi address; try the web archive |
| RC2006 | Tiede, teknologia, innovaatiot | Vanhanen I | Not online; PDF ISBN 952-485-190-3 |
| RC2008 | Linjaus 2008 | Vanhanen II | Retired minedu.fi address; try the web archive |
| RC2010 | Tutkimus- ja innovaatiopoliittinen linjaus 2011–2015 | Kiviniemi | Retired minedu.fi address; try the web archive |
| RC2014 | Uudistuva Suomi: tutkimus- ja innovaatiopolitiikan suunta 2015–2020 | Stubb | **Web archive confirmed (12 captures)**; PDF to save |
| RC2017 | Visio ja tiekartta 2030 | Sipilä | **PDF link found**; to fetch on the Mac |
| RC2020 | TKI-tiekartta | Marin | Press release only; PDF to locate (OKM/TEM) |
| RC2024 | Valtion T&K-rahoituksen käytön monivuotinen suunnitelma (VN 2024:31) | Orpo | **Counted** |
| RC2026 | Kansalliset TKI-politiikan ja -toiminnan strategiset valinnat (VN 2026:1) | Orpo | **Counted; analysed** |
| AN2008 | Valtioneuvoston innovaatiopoliittinen selonteko (VNS 5/2008 vp) | Vanhanen II | Anchor, online |
| AN2014 | Evaluation of the Council (OKM 2014:6) | | Anchor, online |
| AN2022 | Act on state R&D funding 2024–2030 (1092/2022) | | Anchor, online |
| AN2023 | First multi-annual R&D plan (parliamentary RDI working group) | | Anchor, online |
| BM2001A | Eela (2001): human analysis of the Council reviews 1973–2000 | | Benchmark, not counted |

**How to add a document.** Save the PDF as `data/raw/<ID>.pdf`, for example `data/raw/RC2014.pdf`, and run `python scripts/fetch_corpus.py project2/corpus/council.csv`. A saved PDF always takes priority over the web address. For a web-archive copy, put `id_` after the timestamp to get the raw file, for example:
`https://web.archive.org/web/2016id_/http://www.minedu.fi/export/sites/default/OPM/Tiede/tutkimus-_ja_innovaationeuvosto/julkaisut/liitteet/Linjaus2015-2020.pdf`

### Corpus gaps (acknowledged)

The corpus is incomplete, and the gaps are not random. They are part of the method, not a footnote.

| Gap | Documents | Why | Consequence |
|---|---|---|---|
| **Council reviews 1973–2000** | RC1973–RC2000 | Print or library scans only. There is no library access at the moment, so they cannot be checked or digitised. | No Council voice for the first four decades. Research question 2 **cannot be answered yet** for the 1990s, when "national innovation system" entered Finnish policy. Eela (2001) covers this period and is used as a secondary reference only. |
| **Retired web addresses** | RC2003, RC2008, RC2010, RC2014 | Published as PDFs on the old Ministry of Education site (minedu.fi), which was retired, and not moved to the Valto archive. RC2014 is confirmed in the web archive; the others still need checking. | Until retrieved, 2003–2015 is missing on the Council side. |
| **2006 review not online** | RC2006 | Title, date and a PDF ISBN are confirmed; no web address found. | As above. A request to the Council secretariat or to the ministry registry (OKM kirjaamo) is the likeliest route. |
| **Press release instead of main text** | RC2020 | Only the announcement has been found. | Not counted until the main document is found. |

Until these gaps close, nothing in this project is a claim about the Council series as a whole. Rows marked `gap_no_access` are skipped by the fetch script but stay in the log, so the gap remains visible.

## 4. Method

- **The same tracker as Project 1:** 23 concepts in `vocab/concepts.csv`, the same context rules, and institution names removed first (`vocab/exclude.txt`). Rates are mentions per 10,000 words.
- **No pooling.** Council documents differ widely in genre (a funding plan, a vision, a strategy report), so each document is reported **on its own**. There are no decade averages; the script is run with `--no-pooling`.
- **Chapter-level counts** (`project2/scripts/sections.py`) split a document at its own chapter headings, listed in `project2/vocab/sections_<ID>.txt`. This separates, for example, the 2026 report's chapter on other countries from Finland's own choices.
- **Candidate concepts** (`project2/vocab/candidate_concepts.csv`) cover vocabulary the tracker lacks: security, resilience, defence, dual use, data, disruptive technologies, quantum, semiconductors, space, breakthrough innovation, risk-taking, attracting RDI investment, health, climate and the Arctic. They are **provisional**: not yet checked against every matched passage and not unit-tested, so they are always shown with that label.

**To reproduce:**

```bash
python scripts/fetch_corpus.py project2/corpus/council.csv
python scripts/vocabulary.py --series council_review --no-pooling --out project2/data
python project2/scripts/sections.py RC2026
```

## 5. Results so far (2 documents, both from the Orpo term)

Mentions per 10,000 words for each document separately. The counts are in brackets. Both documents are from the same government, so this shows nothing about change over time yet.

| Concept | RC2024 multi-annual R&D plan (10,854 words) | RC2026 strategic choices (13,599 words) |
|---|---:|---:|
| RDI (TKI) | 72.8 (79) | 181.6 (247) |
| R&D (T&K) | 312.3 (339)* | 64.0 (87) |
| Innovation (all forms) | 53.4 (58) | 66.2 (90) |
| Competence (*osaaminen*) | 59.0 (64) | 55.2 (75) |
| Competitiveness | 10.1 (11) | 25.7 (35) |
| Artificial intelligence | 3.7 (4) | 25.7 (35) |
| Digitalisation | 7.4 (8) | 19.1 (26) |
| Sustainability | 4.6 (5) | 11.0 (15) |
| Ecosystem | 6.4 (7) | 10.3 (14) |
| Start-ups | 6.4 (7) | 0.7 (1) |
| Entrepreneurship | 0 | 0 |
| National innovation system | 1.8 (2) | 1.5 (2)** |

\* RC2024 is a plan for R&D (*T&K*) funding, so the term is frequent by design.
\** Whole-document figure. In the 2026 report's body text, the only mention refers to other countries; see the analysis.

**Analyses:**
- [RC2026 as a whole](docs/analysis_RC2026.md): chapter structure, verbatim evidence, tracker and candidate counts, three hypotheses
- [RC2026 chapters 5–6](docs/analysis_RC2026_ch5-6.md): risk-taking, investment attraction, implementation and monitoring, actor–role–instrument relations

## 6. Next steps

1. **Add RC2017 and RC2014.** RC2017 needs `git pull` and then the fetch command; RC2014 needs a save from the web archive. With them, the Council series covers three governments (Stubb, Sipilä, Orpo), and Dashboard 2 gets its comparison panel.
2. **Check the candidate concepts** against every matched passage, add context rules and tests, and promote them to tracker v0.2. Then rerun Project 1 with v0.2 too.
3. **Request RC2006 and the archived reviews** (RC2003, RC2008, RC2010) from the Council secretariat or the ministry registry.
4. **The 1973–2000 reviews** wait for library access.
5. **Government-by-government comparison with Project 1**, once at least three governments are covered on the Council side.

## 7. Ground rules

These are the same as Project 1: public sources only, with no employer data; institutions and roles, not named individuals; evidence, extracted relations and interpretation kept as separate layers; and every number traceable to its passages. Business Finland is named in several Council documents as an implementer, and the author works there. Project 2 therefore describes what the documents say about it and does not evaluate it.
