# Project 1: Government programmes

*Part of [Tracing Finland's Innovation State](../README.md). Overview of the project and its sub-projects 1.1–1.3. Status: 10 November 2026.*

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

This document is the overview. Each question is reported in its own sub-project (§4): vocabulary in 1.1, and the theory of prosperity in 1.2 ([analysis v3](1.2_paradigms/analysis_q2_v3.md): 560 claims, ten programmes from 1987 to 2023 plus one context document fully coded, unvalidated).

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

## 4. Sub-projects

Each research question is a sub-project with its own method, files and status. All of them use the shared corpus in `corpus/programmes.csv`.

| | Question | Status | Main document |
|---|---|---|---|
| **1.1 Vocabulary** | Which concepts dominate each decade? | Tracker v0.1, 30 programmes | [1.1_vocabulary/README.md](1.1_vocabulary/README.md) · [Dashboard 1](https://claude.ai/artifact/8K3c4xNdN4Ppdoh8b2S1rr) |
| **1.2 Paradigms** | When does the theory of prosperity change? | Analysis v3: 560 claims, 10 programmes 1987–2023 + AN2008 fully coded (unvalidated) | [1.2_paradigms/analysis_q2_v3.md](1.2_paradigms/analysis_q2_v3.md) |
| **1.3 Continuity** | Was the start-up ecosystem a continuation or a break? | Planned | [1.3_continuity/README.md](1.3_continuity/README.md) |

Question 4 (the Nokia question) needs firm and start-up data rather than policy documents. It will become a separate project when it starts. Project 1.2 already records the programmes' own framings of Nokia and ICT (hypothesis H2g).

## 5. Results

See the sub-projects: vocabulary results in [1.1](1.1_vocabulary/README.md), theory-of-prosperity results in [1.2](1.2_paradigms/analysis_q2_v3.md).

## 6. Limitations

- **Government programmes only.** The Research and Innovation Council reviews, including their corpus gaps, are handled in [Project 2](../project2/PROJECT2.md).
- **Programmes are one genre**, political coalition agreements, so they show what governments commit to, not the expert policy debate. The Council reviews (Project 2) are needed for that.
- Limitations specific to each sub-project are in its own document.

## 7. Next steps

1. **Link to Project 2:** once the Council reviews are counted, compare the programme and Council vocabularies government by government.
2. **Compare with the human benchmarks.** Does the tracker reproduce the periods found by Eela (2001) and Lemola (2020)?
3. **Claim extraction (weeks 5–9):** evidence-level claims with verbatim excerpts, plus a counter-evidence search.
4. **MCP server and the start-up track (weeks 10–13).**
5. **Video 1:** "60 years of Finnish innovation policy in one chart".

## 8. Repository

The repository layout for both projects is in the [README](../README.md). Project 1's own files:

```
project1/PROJECT1.md                 this overview
project1/corpus/programmes.csv       shared corpus list: 32 programmes, 2 human benchmarks, 5 context documents
project1/1.1_vocabulary/             Q1: README (method, results), data/ (tracker outputs)
project1/1.2_paradigms/              Q2: analysis_q2_v3.md, coding/ (guide, claims v0.4, scope log, checker), data/, archive/
project1/1.3_continuity/             Q3: plan (not started)
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
