# Project 1.1: Vocabulary (research question 1)

*Part of [Project 1](../PROJECT1.md). Question: which policy concepts dominate each decade, and when do they appear and fade? Status: 10 November 2026, tracker v0.1.*

- **Results:** [Dashboard 1](https://claude.ai/artifact/8K3c4xNdN4Ppdoh8b2S1rr)
- **Outputs:** [`data/`](data/) (per-document counts, decade rates, example passages)
- **Code:** shared [`scripts/vocabulary.py`](../../scripts/vocabulary.py) and [`vocab/concepts.csv`](../../vocab/concepts.csv)

```bash
python scripts/fetch_corpus.py project1/corpus/programmes.csv
python scripts/vocabulary.py          # writes project1/1.1_vocabulary/data/
```

## 1. Method

### 1.1 Pipeline

```
project1/corpus/programmes.csv
   → scripts/fetch_corpus.py     download pages/PDFs, extract clean text
   → data/text/<id>.txt
   → scripts/vocabulary.py       count concepts per document and decade
   → project1/1.1_vocabulary/data/vocabulary_*.csv   counts, decade rates, example passages
   → dashboard                   interactive chart with source passages
```

The planned later stages are: claim extraction with an LLM (`prompts/claim_extraction.md`), a Postgres and pgvector store of claims and evidence (`db/schema.sql`), and an MCP server through which Claude can query the corpus.

### 1.2 Text extraction

**Web pages.** Only the main article block of the page is kept. The site's menus, language links, "related news" and contact sections are removed; removing the contact section also takes out named officials.

**PDFs.** Text is extracted page by page. Three cleanups are applied before counting:
- Words split across line breaks are rejoined: *kilpailuky- kyä* → *kilpailukykyä*.
- Genuine compounds are kept as they are: *tutkimus- ja kehitys*.
- Table-of-contents lines are dropped, so section titles are not counted as mentions.

### 1.3 Concept counting (lexical, v0.1)

**Concepts.** `vocab/concepts.csv` defines 23 concepts, each with Finnish word stems. Matching is at the start of a word, so `innovaati` matches *innovaatio*, *innovaatioiden* and *innovaatiopolitiikka*. The concepts are grouped by era:

| Group | Concepts |
|---|---|
| Older paradigm | industrial policy, technology policy, science policy |
| Core | R&D, innovation |
| National-innovation-system era | national innovation system, competence (*osaaminen*), information society, clusters |
| Cross-cutting | competitiveness, internationalisation, R&D spending target |
| Newer paradigm | entrepreneurship, growth companies, start-ups, commercialisation, venture capital, ecosystem, RDI (TKI), digitalisation, artificial intelligence, deep tech, sustainability |

**Rules that prevent false hits:**

1. **Institution names are removed first.** The Council's name *Tutkimus- ja innovaationeuvosto* is not a mention of "innovation". The list is in `vocab/exclude.txt`.
2. **Context rules.** A concept can require nearby words (`near`) or exclude them (`not_near`), within 150 characters:
   - The R&D spending target counts only when R&D, TKI or innovation is nearby. Without that rule, budget surpluses and debt as a percentage of GDP were counted.
   - "Ecosystem" excludes nature contexts, such as *ekosysteemipalvelut*.
   - "Clusters" exclude healthcare competence centres (*osaamiskeskittymä*).
3. **Ambiguous stems were tightened.**
   - "Internationalisation" counts only *kansainvälistyminen*. The adjective *kansainvälistä* mostly appeared in foreign-policy phrases such as "international cooperation".
   - "Commercialisation" counts *kaupallistaminen*, not the adjective *kaupallinen*.
   - "Start-ups" no longer counts the verb *aloittaa* (to start).

All rules were found by reading every matched passage from a full run (231 passages), and are covered by unit tests.

**Measures:**
- **Per document:** mentions per 10,000 words.
- **Per decade:** pooled, meaning all mentions in a decade divided by all words in that decade. This way very short programmes cannot swing a decade. A programme counts in the decade it started.
- **Example passages:** up to three per concept and decade are saved, so every number can be checked against the text.

**Duplicate check.** The script compares each programme with the previous one. It flags a pair when 50% or more of the shorter text's five-word sequences also appear in the other.

## 2. Results (government programmes, 1961–2023)

### 2.1 Concept rates by decade

Mentions per 10,000 words, pooled per decade. Concepts are ordered by total mentions.

| Concept | 1960s | 1970s | 1980s | 1990s | 2000s | 2010s | 2020s | Total mentions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Competence (*osaaminen*) | 0.0 | 0.0 | 5.4 | 22.5 | **24.4** | 18.2 | 14.3 | 341 |
| Competitiveness | 14.4 | 5.6 | 12.6 | **26.3** | 22.0 | 13.4 | 9.6 | 283 |
| Digitalisation | 0.0 | 0.0 | 0.0 | 0.8 | 3.2 | 10.2 | **15.5** | 186 |
| Innovation (any) | 0.0 | 0.0 | 0.0 | 8.3 | 9.6 | **10.8** | 6.3 | 168 |
| Sustainability / green transition | 0.0 | 0.0 | 0.0 | 9.8 | 5.3 | **13.9** | 3.3 | 168 |
| Entrepreneurship | 0.0 | 0.0 | 0.0 | 3.8 | **13.1** | 4.6 | 3.3 | 100 |
| R&D | 0.0 | 2.8 | 7.2 | **11.3** | 5.7 | 3.0 | 3.3 | 81 |
| Information society | 0.0 | 0.0 | 0.0 | 11.3 | **13.5** | 0.6 | 0.0 | 58 |
| RDI (TKI) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | **6.1** | 55 |
| Internationalisation | 0.0 | 0.0 | 1.8 | **4.5** | 3.2 | 3.0 | 1.3 | 49 |
| Industrial policy | **10.8** | 4.2 | 1.8 | 6.8 | 1.8 | 1.7 | 1.6 | 45 |
| Growth companies | 0.0 | 0.0 | 0.0 | 0.0 | 0.7 | **1.8** | 0.9 | 23 |
| Venture capital | 0.0 | 0.0 | 0.0 | 1.5 | **2.5** | 0.8 | 0.5 | 19 |
| Ecosystem | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **1.8** | 0.5 | 19 |
| Artificial intelligence | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.9 | **2.0** | 19 |
| Clusters | 0.0 | 0.0 | 0.0 | 1.5 | **2.1** | 0.5 | 0.0 | 12 |
| Commercialisation | 0.0 | 0.0 | 0.0 | 0.8 | **1.4** | 0.7 | 0.2 | 12 |
| R&D spending target | 0.0 | 0.0 | 0.0 | 0.0 | 0.4 | 0.5 | **1.1** | 11 |
| Start-ups | 0.0 | 0.0 | 0.0 | **0.8** | 0.7 | 0.5 | 0.2 | 8 |
| Technology policy | 0.0 | 0.0 | 0.0 | 0.8 | **1.1** | 0.0 | 0.4 | 6 |
| National innovation system | 0.0 | 0.0 | 0.0 | **3.0** | 0.4 | 0.0 | 0.2 | 6 |
| Science policy | 0.0 | 0.0 | 0.0 | **0.8** | 0.4 | 0.2 | 0.0 | 4 |
| Deep tech | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |

**Corpus size per decade:**

| | 1960s | 1970s | 1980s | 1990s | 2000s | 2010s | 2020s |
|---|---:|---:|---:|---:|---:|---:|---:|
| Programmes | 6 | 10 | 3 | 3 | 2 | 5 | 1 |
| Words | 2,779 | 7,205 | 5,535 | 13,329 | 28,241 | 87,836 | 55,383 |

The dashboard shows the 13 concepts with enough mentions to draw a readable line. The other ten appear in the table above.

### 2.2 Findings

1. **Competitiveness is the constant.** It is the only frequent concept present from the 1960s to the 2020s, and it peaks in the 1990s, during and after the recession of the early 1990s. The goal stays the same while the means change.
2. **Competence (*osaaminen*) becomes the central idea from 1987.** Holkeri's programme states that Finnish knowledge and competence are decisive (*"Suomalaisen tiedon ja osaamisen merkitys on ratkaisevaa"*). Competence is the most frequent concept overall, and it peaks in Lipponen II (1999), at 32.6 mentions per 10,000 words.
3. **"Information society" hands over to "digitalisation".** *Tietoyhteiskunta* appears in 1995, peaks in 2003 and is almost gone by the 2010s. Digitalisation rises as it fades, and is the most frequent concept in 2023.
4. **Entrepreneurship peaks in the 2000s.** In 2003 it was a full policy programme (*Yrittäjyyden politiikkaohjelma*); later it falls back.
5. **"Innovation" never dominates government programmes.** It runs at a steady 6–11 mentions per 10,000 words from 1995. "National innovation system" appears only six times: in Lipponen I and II (1995 and 1999), and once each in 2007 and 2023. The working hypothesis is that this vocabulary lived in the Research and Innovation Council's reviews rather than in the programmes. This is tested in [Project 2](../../project2/PROJECT2.md).
6. **The newest vocabulary.** RDI (TKI), AI and the 4% R&D target appear from the 2010s. Deep tech does not appear at all.

## 3. Limitations (vocabulary)

- **Lexical counting misses ideas expressed in other words.** It also misses compounds where the concept sits inside the word; for example, *kasvuyritysekosysteemi* is not counted as "ecosystem". The planned LLM claim extraction addresses this.
- **Early programmes are very short** (often under 1,000 words), so the 1960s–80s rates rest on few mentions.
- **Decades blur governments.** For example, the 2019 Rinne programme sits in the 2010s, and the 2020s hold a single programme (Orpo).
- **Example passages for five concepts** (internationalisation, R&D target, ecosystem, clusters, RDI) are pending a rerun after their rules changed.
