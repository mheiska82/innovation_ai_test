# Research question 2, analysis v1: has Finland's theory of prosperity changed?

> **Archived.** Superseded by [analysis v2](../analysis_q2_v2.md) (full coding, claims v0.3). Links below point to the old layout (`coding/claims_v0.2.csv` is now `archive/claims_v0.2.csv`).

*Project 1. Status: 10 November 2026. Based on 52 claims in [`coding/claims_v0.2.csv`](coding/claims_v0.2.csv), coded under [`coding/CODING_GUIDE.md`](coding/CODING_GUIDE.md) v0.2. Replaces analysis v0.*

## 0. The question and how it is answered

**Question.** When does the underlying theory of how Finland creates prosperity change?

**Method.**
1. **Documents.** Three government programmes (1987 Holkeri, 2003 Jäätteenmäki / Vanhanen I, 2015 Sipilä) and the 2009 international evaluation of the national innovation system, as the outside view.
2. **Claims.** Every statement linking a driver to a prosperity outcome is coded as **cause (X) → mechanism (M, a mediator, only if stated) → outcome (Y)**, with condition, direction (+/−), chain links and a verbatim excerpt. All 52 excerpts are machine-checked against the source text.
3. **Review pass.** Every claim was reviewed from the stance of an innovation researcher and a policy-maker (`expert_review` column). Four claims were edited, five missed claims added, and six marked low-weight.
4. **Counting.** For each document, the core claims are counted by "engine of prosperity" (theory tag). The engines are compared across years.

**Status.**
- **Single model, unvalidated.** Claude coded and reviewed every claim, and no human has checked them.
- **A sample, not a census.** GP64 was read in full; the other documents were read by key sections plus a search for causal wording.
- **Small counts.** Read the numbers as signals, not statistics.

## 1. Evidence (verbatim)

| Year | Source | Claim (verbatim) | ID |
|---|---|---|---|
| 1987 | Programme | "Suomalaisen tiedon ja osaamisen merkitys on ratkaisevaa." | C002 |
| 1987 | Programme | "Teollisuuden kilpailuedellytyksiä parannetaan vahvistamalla yritysten tutkimus- ja kehitystoimintaa, koulutusta ja markkinointia." | C005 |
| 2003 | Programme | "Hallituksen talouspolitiikka perustuu osaamisen, yrittäjyyden ja muiden kasvun edellytysten vahvistamiseen." | C009 |
| 2003 | Programme | "Suomen talouden kasvu ja kilpailukyky perustuvat jatkossakin ennen kaikkea osaamiseen ja uuden teknologian hyödyntämiseen." | C012 |
| 2003 | Programme | "Rahoitusta on suunnattava muun muassa palvelusektorin ja uusien tuotannonalojen tutkimukseen, kehittämiseen, tuotteistamiseen ja kaupallistamiseen" | C048 |
| 2003 | Programme | "Tutkimus- ja innovaatiorahoitusta lisätään tiede- ja teknologianeuvoston suunnitelman pohjalta." | C049 |
| 2009 | Evaluation | "these inputs do not appear to have resulted in equivalent outputs of a greater global supply of world-class, advanced goods and services" | C040 |
| 2009 | Evaluation | "Growth entrepreneurship is both directly and indirectly a key driver of these two restructuring processes." | C044 |
| 2015 | Programme | "Kasvava talous perustuu hyvään johtamiseen, vahvaan yrittäjyyteen ja omistajuuteen sekä koko Suomen voimavarojen hyödyntämiseen." | C022 |
| 2015 | Programme | "Osaaminen ei muutu innovaatioiksi, innovaatiot eivät kaupallistu." | C024 |
| 2015 | Programme | "Suomi on menettänyt liiallisella sääntelyllä ja hallinnoinnilla ketteryytensä ja samalla kilpailukykynsä." | C027 |
| 2015 | Programme | "yksikkötyökustannusten alentamiseksi vähintään 5 prosentilla" | C052 |
| 2015 | Programme | "Vahvuuksiamme ovat esimerkiksi biotalous, puhtaat teknologiat ja digitalisaatio." | C050 |

## 2. Extracted relations: engines of prosperity, by document

Core claims only (low-weight claims excluded). A claim can carry more than one tag.

| Engine (theory tag) | 1987 | 2003 | 2009 eval. | 2015 |
|---|---:|---:|---:|---:|
| Knowledge, competence | 4 | 3 | 0 | 4 |
| R&D, technology | 2 | **5** | 3 | **0** |
| Entrepreneurship, firms | 0 | 2 | 4 | 4 |
| Commercialisation | 0 | 1 | 0 | 2 |
| Productivity through restructuring | 0 | 0 | **3** | 0 |
| Deregulation, structural reform | 0 | 0 | 0 | **3** |
| Cost competitiveness | 0 | 1 | 0 | 2 |
| Labour-market consensus | 0 | 2 | 0 | 1 |
| Sustainability | 0 | 1 | 0 | 3 |
| Sector choices (bio, cleantech) | 0 | 0 | 0 | 2 |
| Digital, ICT, data | 0 | 0 | 0 | 4 |
| Market failure as rationale | 0 | 1 | 1 | 0 |
| **Core claims** | 7 | 12 | 11 | 16 |
| of which negative (failure or brake) | 0 | 0 | **6** | **4** |

## 3. Interpretation (hypotheses, revised after the review)

**H2a, revised: the engine shifts gradually, not in one jump.**
- *v0 said* the turn to entrepreneurship came in 2015.
- *The review shows* entrepreneurship is already at the foundation of economic policy in 2003 (C009), next to competence, and commercialisation is a funding priority in 2003 (C048).
- *What does change by 2015* is that R&D disappears as a stated cause (5 → 0). Growth is attributed to management, entrepreneurship and ownership (C022), together with deregulation and specific sectors.
- **Revised reading:** 2003 is a *hybrid* (R&D-led, with entrepreneurship added), and 2015 is firm-led with no R&D engine.

**H2b, holds: knowledge stays, but its role changes.** Competence is named about as often in 2015 as in 1987. In 2015, though, it appears in a broken chain (C024): necessary but not sufficient.

**H2c, holds: a turn towards diagnosing failure, starting with the 2009 evaluation.** There are no negative claims in 1987 or 2003, against 6 in the 2009 evaluation and 4 in the 2015 programme. The 2009 diagnosis (inputs without outputs, C040) and the 2015 one (competence without commercialisation, C024) say the same thing. Whether the programme drew on the evaluation is not shown.

**H2d, holds: a new kind of mechanism, removing barriers.** Regulation and rigidities appear as causes only in 2015 (C026, C027).

**H2e, new: "competitiveness" changes meaning.** It is innovation- and knowledge-based in 2003 (C012) and largely cost-based in 2015 (unit labour costs, C052; C030). Comparisons of the word "kilpailukyky" across periods, including the vocabulary counts, need this caveat.

**H2f, new: sectors become causes.** In 2015, specific sectors (bioeconomy, cleantech, water) are named as engines of growth (C050, C051). This prefigures the 2026 Council's thematic strategic choices (Project 2).

**A link to Project 2.** The 2003 programme bases research and innovation funding explicitly on the Science and Technology Policy Council's plan (C049). That is direct evidence of the Council → programme link that Project 2 tests.

**What would weaken these hypotheses:** the 2007 or 2011 programmes already dropping R&D as a cause; the 2008 strategy stating a firm-dynamics theory; a full coding of GP74 finding R&D causal claims that the sample missed.

## 4. Continuity or break?

The answer is mostly **layering**: new engines (entrepreneurship, deregulation, sectors, cost) are added while knowledge persists. The one clear **break** in this sample is R&D's disappearance as a stated cause between 2003 and 2015.

## 5. Next steps

1. Code GP70 (2007) and GP72 (2011) to date the R&D break.
2. Get and code the 2008 strategy (ST2008).
3. Code GP68 and GP74 in full.
4. Have a human spot-check about 10 claims per document before publishing.
5. Code GP77 (Orpo, 2023) to see whether the firm-led theory persists, or whether R&D returns with the 4% target.
