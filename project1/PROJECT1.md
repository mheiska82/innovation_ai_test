# Project 1: Government programmes

*Part of [Tracing Finland's Innovation State](../README.md). Project description, methodology and first results. Status: 10 November 2026.*

## 1. What this project is

This is an AI-assisted research tool for the history of Finnish innovation policy, built only on public documents. It has two purposes:

1. **Research:** to trace how Finland's model of innovation-led growth changed from the 1960s to today.
2. **Expertise and outreach:** to show, step by step and in public (YouTube and LinkedIn), how AI can be used rigorously in innovation research, with every finding traceable to its source.

It is a personal side project. It uses public data only, with no Business Finland internal data or code, and it does not profile named individuals.

- **Code:** [github.com/mheiska82/innovation_ai_test](https://github.com/mheiska82/innovation_ai_test)
- **Plan:** [project plan doc](https://claude.ai/artifact/UWkWKbdpyKRT3nZfL5VuMR)
- **Results:** [interactive dashboard](https://claude.ai/artifact/8K3c4xNdN4Ppdoh8b2S1rr)

## 2. Research questions

**Core question.** How did Finland's model of innovation-led growth shift from a state-coordinated technology system to an ecosystem model centred on entrepreneurship, commercialisation and private capital?

**Secondary questions**, in the order the tool is being built:

1. **Vocabulary.** Which policy concepts dominate each decade, and when do they appear and fade?
2. **Paradigm shifts.** When does the underlying theory of how Finland creates prosperity change?
3. **Continuity or break.** Was the start-up ecosystem a continuation of the older innovation system, or a break from it?
4. **The Nokia question.** Through which mechanisms did Nokia's rise and decline shape Finnish start-ups?

This document reports on question 1, the first stage. An analysis of question 2 (v1, unvalidated), based on 52 coded and reviewed claims, is in [analysis_q2_v1.md](analysis_q2_v1.md).

## 3. Data

### Corpus, batch 1

The corpus list is in `project1/corpus/programmes.csv` (39 entries: 32 government programmes, 2 human benchmarks and 5 context documents for research question 2). All 30 counted programmes are downloaded.

> **The Research and Innovation Council reviews are now a separate track, [Project 2](../project2/PROJECT2.md),** with their own corpus list (`project2/corpus/council.csv`), corpus gaps, analyses and [Dashboard 2](https://claude.ai/artifact/QuE38nxXvvPoXBvLtKEMpB). This document covers Project 1: the government programmes.

| Series | Documents | Status |
|---|---|---|
| Government programmes (*hallitusohjelmat*), governments 46–77, 1961–2023 | 32 entries, 30 counted | All downloaded |
| Human benchmark studies (Lemola 2001; Lemola 2020) | 2 | Reference only, not counted. Eela (2001), a benchmark for the Council reviews, moved to Project 2 |
| Context documents for question 2 (2008 national innovation strategy, 2009 evaluation of the innovation system, OECD 2017 and 2022) | 5 | 4 online; the 2008 strategy has a retired tem.fi address. Not counted with the programmes |

**Sources.** The programmes up to 1999 come as web text from valtioneuvosto.fi ("Hallitusohjelmat vuodesta 1917"). Programmes from 2003 onwards come as PDFs from the government publication archive Valto (julkaisut.valtioneuvosto.fi).

**Duplicates removed.** Two governments did not write a programme of their own, so each programme is counted once:

| Government | What it used | Evidence |
|---|---|---|
| Vanhanen I (2003) | Jäätteenmäki's programme (2003) | Concept counts are near-identical, e.g. R&D 13 vs 13 |
| Marin (2019) | Rinne's programme (2019) | Its parliamentary statement, VNT 2/2019 vp |

**Documents to read with care:**

| Government | Note |
|---|---|
| Aura II (1971) | Caretaker government; the text is the Prime Minister's speech |
| Kiviniemi (2010) and Stubb (2014) | Short programmes that continue their predecessors' programmes with additions |

### Context documents for research question 2

Question 2 (when does the theory of how Finland creates prosperity change?) needs documents where that theory is stated explicitly, not only programmes. They are listed in the same corpus file but kept out of the programme counts (`series` = `strategy` or `evaluation`).

| ID | Document | Why it matters | Link status |
|---|---|---|---|
| ST2008 | Kansallinen innovaatiostrategia (proposal, 12.6.2008) | The clearest written statement of the theory at the 2000s turning point; basis of the Government report VNS 5/2008 (Project 2, AN2008) | Retired tem.fi address: web archive or manual save |
| EV2009F | Evaluation of the Finnish National Innovation System, Full Report (2009) | An outside, international view of the system at the turning point, starting from the 2008 strategy | Online (ETLA) |
| EV2009P | The same evaluation, Policy Report (2009) | Summary of the key findings | Online (ETLA) |
| OE2017 | OECD Reviews of Innovation Policy: Finland 2017 | An outside view after the restructuring of the 2010s; cited in the 2026 Council report | Online (OECD, DOI) |
| OE2022 | OECD Economic Surveys: Finland 2022, chapter "Rebooting the innovation ecosystems" | The ecosystem framing from outside; cited in the 2026 Council report | Online (OECD, DOI) |

**Language.** EV2009 and the OECD documents are in English. The tracker's stems are Finnish, so these documents are used for claim extraction (and later English stems), not for the Finnish vocabulary counts.

### Size

The 30 counted programmes total about **200,000 words**. Programme length grew roughly 300-fold, from 52 words (Liinamaa 1975) and 168 words (Miettunen 1961) to 55,383 words (Orpo 2023). Because of this growth, all results are given as mentions per 10,000 words.

## 4. Method

### 4.1 Pipeline

```
project1/corpus/programmes.csv
   → scripts/fetch_corpus.py     download pages/PDFs, extract clean text
   → data/text/<id>.txt
   → scripts/vocabulary.py       count concepts per document and decade
   → project1/data/vocabulary_*.csv   counts, decade rates, example passages
   → dashboard                   interactive chart with source passages
```

The planned later stages are: claim extraction with an LLM (`prompts/claim_extraction.md`), a Postgres and pgvector store of claims and evidence (`db/schema.sql`), and an MCP server through which Claude can query the corpus.

### 4.2 Text extraction

**Web pages.** Only the main article block of the page is kept. The site's menus, language links, "related news" and contact sections are removed; removing the contact section also takes out named officials.

**PDFs.** Text is extracted page by page. Three cleanups are applied before counting:
- Words split across line breaks are rejoined: *kilpailuky- kyä* → *kilpailukykyä*.
- Genuine compounds are kept as they are: *tutkimus- ja kehitys*.
- Table-of-contents lines are dropped, so section titles are not counted as mentions.

### 4.3 Concept counting (lexical, v0.1)

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

## 5. Results (government programmes, 1961–2023)

### 5.1 Concept rates by decade

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

### 5.2 Findings

1. **Competitiveness is the constant.** It is the only frequent concept present from the 1960s to the 2020s, and it peaks in the 1990s, during and after the recession of the early 1990s. The goal stays the same while the means change.
2. **Competence (*osaaminen*) becomes the central idea from 1987.** Holkeri's programme states that Finnish knowledge and competence are decisive (*"Suomalaisen tiedon ja osaamisen merkitys on ratkaisevaa"*). Competence is the most frequent concept overall, and it peaks in Lipponen II (1999), at 32.6 mentions per 10,000 words.
3. **"Information society" hands over to "digitalisation".** *Tietoyhteiskunta* appears in 1995, peaks in 2003 and is almost gone by the 2010s. Digitalisation rises as it fades, and is the most frequent concept in 2023.
4. **Entrepreneurship peaks in the 2000s.** In 2003 it was a full policy programme (*Yrittäjyyden politiikkaohjelma*); later it falls back.
5. **"Innovation" never dominates government programmes.** It runs at a steady 6–11 mentions per 10,000 words from 1995. "National innovation system" appears only six times: in Lipponen I and II (1995 and 1999), and once each in 2007 and 2023. The working hypothesis is that this vocabulary lived in the Research and Innovation Council's reviews rather than in the programmes. This is tested in [Project 2](../project2/PROJECT2.md).
6. **The newest vocabulary.** RDI (TKI), AI and the 4% R&D target appear from the 2010s. Deep tech does not appear at all.

## 6. Limitations

- **Government programmes only.** The Research and Innovation Council reviews, including their corpus gaps, are handled in [Project 2](../project2/PROJECT2.md).

- **Lexical counting misses ideas expressed in other words.** It also misses compounds where the concept sits inside the word; for example, *kasvuyritysekosysteemi* is not counted as "ecosystem". The planned LLM claim extraction addresses this.
- **Early programmes are very short** (often under 1,000 words), so the 1960s–80s rates rest on few mentions.
- **Decades blur governments.** For example, the 2019 Rinne programme sits in the 2010s, and the 2020s hold a single programme (Orpo).
- **Programmes are one genre**, political coalition agreements, so they show what governments commit to, not the expert policy debate. The Council reviews (Project 2) are needed for that.
- **Example passages for five concepts** (internationalisation, R&D target, ecosystem, clusters, RDI) are pending a rerun after their rules changed.

## 7. Next steps

1. **Link to Project 2:** once the Council reviews are counted, compare the programme and Council vocabularies government by government.
2. **Compare with the human benchmarks.** Does the tracker reproduce the periods found by Eela (2001) and Lemola (2020)?
3. **Claim extraction (weeks 5–9):** evidence-level claims with verbatim excerpts, plus a counter-evidence search.
4. **MCP server and the start-up track (weeks 10–13).**
5. **Video 1:** "60 years of Finnish innovation policy in one chart".

## 8. Repository

The repository layout for both projects is in the [README](../README.md). Project 1's own files:

```
project1/PROJECT1.md               this document
project1/corpus/programmes.csv     corpus list: 32 government programmes, 2 human benchmarks
project1/data/                     tracker outputs (counts, decade rates, example passages)
```

**To reproduce:**

```bash
python scripts/fetch_corpus.py project1/corpus/programmes.csv
python scripts/vocabulary.py
```

## 9. Ground rules

- Public sources only; no employer data.
- Institutions and roles, not named individuals.
- Evidence, extracted relations and interpretations are kept as separate layers.
- Every number can be traced to the passages it counts.

## Sources

- Valtioneuvosto: [Hallitusohjelmat vuodesta 1917](https://valtioneuvosto.fi/historia-ja-rakennukset/hallitusohjelmat)
- Valtioneuvoston julkaisuarkisto Valto: [julkaisut.valtioneuvosto.fi](https://julkaisut.valtioneuvosto.fi)
- Eela, R. (2001). *Suomen teknologiapolitiikka valtion tiede- ja teknologianeuvoston katsausten valossa.* VTT Teknologian tutkimuksen ryhmä, työpaperi 56. [PDF](https://sarjaweb.vtt.fi/julkaisut/muut/2001/tp56.pdf)
- Lemola, T. (2001). *Tiedettä, teknologiaa ja innovaatioita kansakunnan parhaaksi.* VTT, työpaperi 57. [PDF](https://sarjaweb.vtt.fi/julkaisut/muut/2001/tp57.pdf)
- Lemola, T. (2020). *Kohti uutta tutkimus- ja innovaatiopolitiikkaa.* Tampere: Vastapaino.
- Pelkonen, A., Nieminen, M. & Lehenkari, J. (2014). *Tutkimus- ja innovaationeuvoston toiminnan ja vaikuttavuuden arviointi.* OKM 2014:6. [URN](https://urn.fi/URN:ISBN:978-952-263-271-5)
