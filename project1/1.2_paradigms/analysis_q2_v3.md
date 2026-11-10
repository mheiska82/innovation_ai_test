# Research question 2, analysis v3: when does Finland's theory of prosperity change?

*Project 1.2. Status: 10 November 2026. Based on 560 claims in [`coding/claims_v0.4.csv`](coding/claims_v0.4.csv), coded under [`coding/CODING_GUIDE.md`](coding/CODING_GUIDE.md) v0.4, with coverage logged in [`coding/scope_v0.4.md`](coding/scope_v0.4.md). Replaces [analysis v2](archive/analysis_q2_v2.md). Interactive view: [Dashboard 3](https://claude.ai/artifact/U9PoQKHgZxME1N3U4j6wpZ) (it rounds halves up, so a few shares differ by one point from the tables here).*

## 0. The question and how it is answered

**Question.** When does the underlying theory of how Finland creates prosperity change? In particular: when does R&D become the stated engine of growth, when does it stop being one, and did it come back after 2015?

**Documents.** Ten government programmes from 1987 to 2023, plus two context documents:

| ID | Year | Government / author | Claims (all / core) | Coverage |
|---|---|---|---|---|
| GP64 | 1987 | Holkeri | 20 / 16 | whole programme read |
| GP65 | 1991 | Aho | 23 / 22 | whole programme read (new) |
| GP66 | 1995 | Lipponen I | 33 / 31 | full protocol (new) |
| GP67 | 1999 | Lipponen II | 35 / 34 | full protocol (new) |
| GP68 | 2003 | Jäätteenmäki / Vanhanen I | 59 / 50 | full protocol |
| GP70 | 2007 | Vanhanen II | 69 / 60 | full protocol |
| AN2008 | 2008 | Government report on the national innovation strategy (context) | 31 / 17 | read in full (new) |
| EV2009P | 2009 | International evaluation (outside view) | 11 / 11 | key sections only |
| GP72 | 2011 | Katainen | 62 / 58 | full protocol |
| GP74 | 2015 | Sipilä | 54 / 47 | full protocol |
| GP75 | 2019 | Rinne (also used by Marin) | 72 / 70 | full protocol (new) |
| GP77 | 2023 | Orpo | 91 / 84 | full protocol, with a word-filter deviation (new) |

**Method.** Unchanged from v2, and set out in the coding guide (§4c, §4d).
1. **Scope.** A claim is any statement linking a driver to an economic outcome: growth, productivity, competitiveness, employment, exports, innovation, structural renewal, or the financing of the welfare state.
2. **Coverage, two tiers.** Economic, innovation, labour, education, regional, energy and ownership chapters are read in full. All other chapters are screened for economic-outcome words, and every hit is read in context.
3. **One deviation.** In GP77, chapters 5 and 7, section 7.6, section 8.3 and annex D were read through a broad sentence filter rather than in full. Twenty claims come from these sections and are marked in the `coverage` column.
4. **Coding.** Each claim is coded as cause (X) → stated mechanism (M) → outcome (Y), with condition, direction, chain links, theory tags, weight and a verbatim excerpt.
5. **Excerpt check.** All 560 excerpts are machine-checked: 463 match after whitespace normalisation, and 97 more match letter for letter once the PDF text layer's split words are joined.
6. **Counting.** Core claims per document are counted by tag, and shares are used because the documents differ in length.

**AN2008 is not a programme.** It is the Government's report to Parliament (VNS 5/2008) on the 2008 national innovation strategy, and it is used because the strategy proposal itself is not available as a public file. It is shown alongside the programmes, but it is not part of the programme series.

**Status.** One model coded and reviewed every claim, and no human has checked them. The counts are signals, not statistics.

## 1. Evidence: dating the R&D engine

R&D-tagged core claims, counted by rule from the claims file:
- **Causal → growth:** a causal or rationale claim whose stated outcome is growth, productivity, competitiveness, welfare, employment or exports, with a positive direction.
- **Instrument:** an R&D measure or target.
- **Negative:** a doubt, cut or gap.

v2 classified these claims by hand, so its row counts are not directly comparable with this table.

| | 1987 | 1991 | 1995 | 1999 | 2003 | 2007 | 2008 (AN) | 2011 | 2015 | 2019 | 2023 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R&D causal → growth | 0 | 0 | 1 | 1 | 5 | 1 | 1 | 3 | 0 | **6** | **6** |
| R&D instruments | 2 | 3 | 3 | 2 | 4 | 4 | 0 | 5 | 4 | 7 | 5 |
| R&D negative (doubt, cut, gap) | 0 | 0 | 0 | 0 | 0 | 0 | **4** | 1 | 2 | 1 | 1 |
| R&D-intensity target in the text | – | – | rising share (C316, C324) | at least current level (C346) | – | 4 % (C134) | – | 4 % kept (C202) | none | **4 % + roadmap** (C432) | **4 % by 2030, cross-party** (C507) |

The key passages, by period:

**1991: cost, not knowledge.** The Aho programme answers the depression with cost and price competitiveness: "Keskeinen tavoite on suhteellisen kustannustasomme alentaminen kilpailukykyiselle tasolle." (C283). R&D appears only as one of the conditions for industry, alongside transport (C285).

**1995: the turn to "real" competitiveness.**
- The Lipponen I programme sets innovation against price: "…tutkimus- ja kehityspanokseen perustuvaa reaalista kilpailukykyä" (C314).
- It also names "korkeaan osaamiseen perustuvalle uusteollistamiselle" as the condition for halving unemployment (C305).
- The national innovation system appears for the first time, but only as a research-balance aim (C323, low weight).
- R&D is still an input target ("kansantuoteosuutta", C316, C324), not yet a growth claim.

**1999: knowledge as the main factor of production.** Knowledge is "keskeisin tuotannontekijä" (C354), and R&D is named as a growth driver: "koulutuksen, tutkimuksen ja tuotekehityksen kasvavat voimavarat hyödyttävät talouden kasvua" (C333). The first "beyond R&D" claim, on commercialisation, also appears that year: "Tutkimus- ja kehityspanostuksen lisäksi…" (C347).

**2003–2007: the peak.** No change from v2 (C102, C118, C131).

**2008: the doubt arrives in the Government's own strategy report** (AN2008, context document):
- "…investoinnit tutkimukseen ja teknologiaan eivät ole riittävästi näkyneet esimerkiksi nopeaan kasvuun pyrkivien yritysten määränä…" (C373, a broken chain).
- Growth can "ei kuitenkaan enää" be secured by a technology-led strategy alone (C372).
- "Kansallisten innovaatiojärjestelmien sijasta huomio kiinnittyy innovaatioiden ekosysteemeihin" (C382).

**2011 and 2015.** As in v2: R&D is kept but doubted and redirected in 2011 (C205, C206), and dropped through the budget in 2015 (C274, C275).

**2019: R&D returns.**
- "…tutkimus-, kehitys- ja innovaatiotoiminta on käännettävä kasvu-uralle" (C403).
- The economy chapter states a mediator: "Talouskasvu perustuu Suomessa ennen kaikkea tuottavuuden kasvuun. Tuottavuuden kasvun tärkeimmät tekijät ovat osaaminen ja innovaatiot." (C408).
- The 4 % target comes back with a roadmap (C432).

**2023: R&D stays, with the fullest chain in the corpus.**
- R&D funding → competence, productivity and competitiveness → "pitkän aikavälin talouskasvuun, joka vahvistaa hyvinvointiyhteiskunnan rahoituspohjaa" (C531).
- Low R&D is diagnosed as a cause of slow productivity (C474).
- RDI has "ratkaiseva merkitys" (C528).
- The 4 % target becomes a cross-party commitment (C507).

**Dating.**
1. **The R&D engine is a 1999–2011 claim.** It is built up in 1995–1999, peaks in 2003–2007, is doubted at government level from 2008, and is dropped in 2015.
2. **It returns in 2019 and 2023**, with more causal R&D-growth claims than at any earlier point. So the 2015 drop was a dip, not a lasting break.

## 2. Extracted relations: engines of prosperity

Share of core claims carrying each tag. A claim can carry several tags. Tags under 8 % everywhere are left out; raw counts for all tags are in [`data/q2_engines_v3.csv`](data/q2_engines_v3.csv).

| Engine | 1987 | 1991 | 1995 | 1999 | 2003 | 2007 | AN 2008 | EV 2009 | 2011 | 2015 | 2019 | 2023 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Knowledge, competence | **38** | 14 | 16 | 29 | 22 | 13 | 24 | 0 | 12 | 9 | 24 | 15 |
| R&D, technology | 12 | 14 | 13 | 9 | 18 | 10 | **35** | 27 | 16 | 9 | 20 | 18 |
| Innovation (broad) | 0 | 0 | 3 | 6 | 0 | 13 | **24** | 9 | 2 | 0 | 14 | 2 |
| Entrepreneurship, firms | 6 | 9 | 19 | 12 | 20 | 13 | 29 | **36** | 19 | 32 | 16 | 12 |
| Labour supply, activation | 6 | 18 | 19 | 15 | 20 | **25** | 12 | 0 | 16 | 9 | 21 | **25** |
| Location factors | 0 | 9 | 6 | 6 | 12 | 3 | 6 | 0 | 10 | 4 | 16 | **21** |
| Cost competitiveness | 6 | **27** | 6 | 6 | 10 | 7 | 0 | 0 | 5 | 15 | 3 | 4 |
| Macro stability | 0 | **18** | 13 | 12 | 4 | 3 | 0 | 0 | 3 | 0 | 1 | 2 |
| Growth → employment | 0 | 5 | **16** | 15 | 2 | 0 | 0 | 0 | 0 | 0 | 6 | 1 |
| Deregulation, structural reform | 0 | 5 | 3 | 9 | 0 | 2 | 0 | 0 | 2 | **32** | 0 | 8 |
| Sector choice | 0 | 0 | 10 | 9 | 4 | 7 | 0 | 0 | **19** | 13 | 6 | 11 |
| Regions as engines | 6 | 14 | 10 | 12 | **16** | 10 | 0 | 9 | 5 | 2 | 9 | 6 |
| Exports | 6 | 9 | 10 | 9 | 6 | 7 | 0 | 0 | **14** | 4 | 9 | 10 |
| Sustainability as growth | 0 | 5 | 10 | 0 | 2 | 5 | 0 | 0 | 9 | 13 | 10 | 13 |
| Productivity, restructuring | 0 | 9 | 0 | 3 | 0 | 5 | 18 | **27** | 5 | 0 | 7 | 5 |
| Digital, ICT | 0 | 0 | 0 | **15** | 4 | 2 | 0 | 0 | 2 | 11 | 6 | 6 |
| Growth → welfare state | 0 | 0 | 0 | 3 | 6 | **12** | 0 | 0 | 7 | 0 | 6 | 8 |
| Structural adaptation | **31** | 5 | 6 | 0 | 0 | 2 | 0 | 0 | 7 | 0 | 3 | 4 |
| Ecosystems (v0.4) | 0 | 0 | 0 | 0 | 0 | 0 | **12** | 0 | 0 | 0 | 7 | 2 |
| Demand- and user-led (v0.4) | 0 | 0 | 0 | 0 | 0 | 0 | **18** | 0 | 0 | 0 | 0 | 0 |
| Claims of failure or doubt (count) | 0 | 1 | 0 | 0 | 1 | 1 | 5 | 6 | 3 | **11** | 5 | 8 |

Values are percentages, except the last row. The last row now counts every negative or doubt direction ("−", "− (broken chain)", "(gap)", "?"). v2 counted only "-" and "?", which gave 7 for 2015.

## 3. Interpretation (hypotheses, revised)

**H2a, revised: layering with a dip, not a break.**
- The engines are mostly added rather than replaced.
- v2 dated an R&D break in 2015. With 2019 and 2023 coded, it is a dip: R&D returns as a causal growth claim (6 + 6 claims), not only as a spending target. In 2023 it carries the longest stated mediator chain in the corpus (C531).
- Its share (20 % and 18 %) is about the same as in 2003 (18 %), so R&D returns as one engine among several, not as the dominant one.

**H2b, revised: knowledge falls, then rebounds.**
- With the 1990s coded, the knowledge share runs 38 → 14 → 16 → **29** → 22 → 13 → 12 → 9 → **24** → 15.
- It peaks in 1999 ("keskeisin tuotannontekijä", C354) and in 2019.
- The "steady decline" in v2 was an artefact of starting the series in 1987 and stopping it in 2015.

**H2c, extended: the doubt about R&D is older than the 2011 programme.** The first explicit broken chain from R&D to firm dynamics is in the Government's own 2008 report (C373), not in the 2011 programme (C205). The sequence suggests diffusion:
1. strategy (2008);
2. international evaluation (2009);
3. programme (2011, C206).

The programmes do not cite AN2008, so this is an inference from the dates, not from the texts.

**H2d, qualified: deregulation is specific to 2015.** It falls from 32 % in 2015 to 0 % in 2019 and 8 % in 2023. The 2023 reform theory runs through the labour market instead: "Hallitus kehittää Suomen työmarkkinoita joustavampaan suuntaan." (C493). The deregulation claims there concern permitting and national gold-plating (C524, C545).

**H2e, extended: cost competitiveness has three peaks.**
- **1991 (27 %).** It is the depression remedy, carried by macro stability (18 %).
- **2015 (15 %).** It runs through the unit-labour-cost target.
- **2023 (4 %, but stated as a mechanism).** "…hallitus vahvistaa vientivetoista työmarkkinamallia" (C494).
- **1995 renames it.** From 1995, "real" competitiveness ("reaalista kilpailukykyä", C314) sits alongside price competitiveness, and in 2019 the two are named together (C412).

**H2i, new: the 1990s build the innovation theory in three steps.**
1. **1991:** regional competence centres, the first system-type claim (C294).
2. **1995:** innovation-based "real" competitiveness and competence-based re-industrialisation (C305, C314). The NIS is named (C323).
3. **1999:** knowledge as the main factor of production, R&D as a growth driver, and commercialisation added (C333, C347, C354).

The system theory arrives in the programmes before it arrives as a growth claim: it is named in 1995 and argued in 2003.

**H2j, new: 2023 holds two theories at once.** Both are stated in the same programme:
- **R&D and innovation:** the chain via productivity (C531, C474).
- **Work, firms and location:**
  - "Hyvinvointi syntyy työstä. Työllisyys syntyy kannattavan yritystoiminnan kautta." (C478);
  - labour supply at 25 % and location factors at 21 %, both the highest in the series.

The two theories meet in the location argument: a small country cannot compete on subsidies, so it competes on competence and the operating environment (C520).

**H2k, new: the welfare arrow reverses and reverses back.**
- **1999–2011 and 2023:** the welfare state is the *result* of growth (`growth_to_welfare`).
- **2019:** the welfare state is a *source* of competitiveness. "Pohjoismainen hyvinvointimalli … takaa maamme tulevaisuuden kilpailukyvyn" (C406), and the welfare state is listed first among the foundations of growth (C409).
- **Who built it:**
  - 2019: "Koulutukseen, tutkimukseen ja innovaatioihin nojannut kasvu" (C455);
  - 2023: "rakennettu työllä ja yrittämisellä" (C491).

**H2l, new: ecosystems and security.**
- **Ecosystems.** They replace the national innovation system as the unit of attention in AN2008 (C382) and enter the programmes in 2019 (C427).
- **Security.** It enters the theory of prosperity in 2023, with strategic competitiveness, self-sufficiency and security of supply (C517) and geopolitical tension named as a factor for the economy (C557).

## 4. Continuity or break?

**Layering, with one dip, one reversal and two newcomers.**
- **Continuity.** Knowledge, labour supply, cost competitiveness and location factors are present in every programme from 1991 to 2023, with changing weights.
- **The dip.** The R&D engine is built in 1995–1999, affirmed in 2003–2011 and dropped in 2015, then restored in 2019–2023.
- **The reversal.** In 2019 the welfare state is argued to be a source of growth, and in 2023 it becomes its result again.
- **The newcomers.**
  - Deregulation is specific to 2015, and its 2023 form is labour-market reform.
  - Security and resilience enter in 2023.
- **The real turning point of the 1990s is 1995.** Competitiveness is redefined from price to "real", innovation-based competitiveness.

## 5. What extending the corpus changed (robustness)

- **v2's "break in 2015" becomes a dip.** It could only be tested with 2019 and 2023. v2 named the test itself (next step 3: "Does R&D return with the 4 % law…?"), and the answer is yes.
- **The first doubt moves from 2011 to 2008**, through a context document. If AN2008 is set aside, v2's dating for the programmes stands.
- **The knowledge decline was an endpoint effect** (H2b).
- **The GP77 word filter could bias the 2023 shares.** Chapters 5 (competence) and 7 (energy) were filtered, and both are rich in knowledge and sustainability claims, so these two shares for 2023 may be understated. The R&D, labour and location claims come from chapters read in full (1, 4 and 6).

## 6. Limitations

- **Single model, unvalidated.** Claude both coded and reviewed every claim.
- **Shares depend on document length and style.** The 1990s programmes are short (2,700–6,700 words), and GP77 is about 57,000 words. Shares of 22–34 core claims move by 3–5 points per claim.
- **AN2008 and EV2009P are not programmes.** They are shown for context only.
- **ST2008, the 2008 strategy proposal, is still missing.**
- **Screened chapters may miss claims phrased without economic-outcome words.**
- **Counting by tag gives a multi-tag claim weight under each of its tags.**

## 7. Next steps

1. **Human spot-check.** About 10 claims per programme, stratified by coverage tier, including the GP77 word-filter claims.
2. **Fully read GP77 chapters 5 and 7**, to remove the deviation and check the knowledge and sustainability shares for 2023.
3. **Project 2 comparison.** Compare the 2019 and 2023 R&D return with the Council's RC2017, RC2020 roadmap and RC2024. Check whether AN2008's doubt has a Council source (RC2008 and RC2010 are corpus gaps).
4. **Question 1.3 (continuity or break).** Re-use these claims with a firm-dynamics codebook. AN2008 is now the earliest anchor.
5. **Question 1.1 (vocabulary).** Check whether "ekosysteemi" and "huoltovarmuus" rise in the word series when the claims say they do.
