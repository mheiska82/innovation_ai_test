# Research question 2, first analysis (v0): has Finland's theory of prosperity changed?

*Project 1. Status: 10 November 2026. Based on 47 claims in [`coding/claims_v0.1.csv`](coding/claims_v0.1.csv), coded under [`coding/CODING_GUIDE.md`](coding/CODING_GUIDE.md).*

## 0. Status: read this first

- **Single coder, unvalidated.** Every claim was coded by Claude. No human has checked the coding yet, so everything below is a first reading.
- **A sample, not a census.** There are four documents. One was read in full; for the other three, the key sections were read and the rest searched for cause-and-effect wording. The claim counts reflect this sampling as well as the documents themselves.
- **Mixed genres.** Three government programmes (1987, 2003, 2015) plus one outside evaluation (2009). The evaluation is not a government statement. It is included as the outside view at the turning point.
- **Missing pieces.** The 2008 national innovation strategy did not download, and the programmes of 2007 (GP70) and 2011 (GP72) are not yet coded.

## 1. Evidence: the stated theory in each document (verbatim)

| Year | Document | Core causal claim (verbatim) | Claim |
|---|---|---|---|
| 1987 | Holkeri programme | "Suomalaisen tiedon ja osaamisen merkitys on ratkaisevaa." | C002 |
| 1987 | Holkeri programme | "Teollisuuden kilpailuedellytyksiä parannetaan vahvistamalla yritysten tutkimus- ja kehitystoimintaa, koulutusta ja markkinointia." | C005 |
| 2003 | Jäätteenmäki / Vanhanen I programme | "Suomen talouden kasvu ja kilpailukyky perustuvat jatkossakin ennen kaikkea osaamiseen ja uuden teknologian hyödyntämiseen." | C012 |
| 2003 | Jäätteenmäki / Vanhanen I programme | "Siksi tutkimus- ja kehittämistoiminnan kasvun jatkuminen on välttämätöntä." | C013 |
| 2009 | International evaluation | "these inputs do not appear to have resulted in equivalent outputs of a greater global supply of world-class, advanced goods and services" | C040 |
| 2009 | International evaluation | "Growth entrepreneurship is both directly and indirectly a key driver of these two restructuring processes." | C044 |
| 2015 | Sipilä programme | "Kasvava talous perustuu hyvään johtamiseen, vahvaan yrittäjyyteen ja omistajuuteen sekä koko Suomen voimavarojen hyödyntämiseen." | C022 |
| 2015 | Sipilä programme | "Osaaminen ei muutu innovaatioiksi, innovaatiot eivät kaupallistu." | C024 |
| 2015 | Sipilä programme | "Suomi on menettänyt liiallisella sääntelyllä ja hallinnoinnilla ketteryytensä ja samalla kilpailukykynsä." | C027 |

## 2. Extracted relations

### 2.1 Which engine of prosperity each document names

Number of claims carrying each tag; a claim can carry more than one.

| Engine (theory tag) | 1987 | 2003 | 2009 eval. | 2015 |
|---|---:|---:|---:|---:|
| Knowledge, competence | 3 | 4 | 0 | 4 |
| R&D, technology | 2 | 3 | 3 | **0** |
| Entrepreneurship, firms | 0 | 2 | 4 | **5** |
| Deregulation, structural reform | 0 | 0 | 0 | **4** |
| Productivity through restructuring | 0 | 0 | **3** | 0 |
| Digital, ICT, data | 0 | 2 | 0 | 4 |
| Competitiveness, exports | 1 | 1 | 0 | 2 |
| Labour-market consensus | 0 | 2 | 0 | 0 |
| Growth as the basis of welfare | 0 | 2 | 0 | 0 |
| **Claims coded** | 8 | 13 | 11 | 15 |
| of which negative (a failure or brake) | 0 | 0 | **6** | **4** |
| of which with a stated mechanism | 0 | 3 | 5 | 2 |

### 2.2 Chains the documents state

- **2003:** competence and new technology → growth and competitiveness (C012), *therefore* R&D growth is necessary (C013).
- **2009:** growth entrepreneurship → internal and external restructuring → productivity growth (C044 builds on C042 and C043). In parallel: high R&D inputs → *not* matched by outputs (C040) → returns from public R&D too low (C041).
- **2015:** competence → (does *not* become) innovation → (is *not*) commercialised → loss of knowledge-based competitive advantage (C024 → C025). Separately, regulation → lost agility → lost competitiveness (C027).

## 3. Interpretation (hypotheses to test, not findings)

**H2a. The engine changes.** From *knowledge and technology inputs create growth* (1987 and 2003, with R&D stated as "välttämätöntä") to *firms, entrepreneurs and ownership create growth* (2015). In this sample, R&D as a stated cause drops from 3 claims (2003) to 0 (2015), while entrepreneurship rises from 0 (1987) to 5 (2015).

**H2b. Knowledge stays, but its role changes.** Competence is named about equally often in 1987, 2003 and 2015. In 2015, however, it appears in a *broken* chain: knowledge is there but does not turn into innovation. The theory is not abandoned. It is re-specified: knowledge is necessary but no longer sufficient.

**H2c. A turn towards diagnosing failure.** The 1987 and 2003 programmes contain no claims about the system failing. The 2009 evaluation and the 2015 programme do: 6 and 4 negative claims. The 2009 diagnosis (inputs without outputs) and the 2015 diagnosis (competence without commercialisation) are close in substance. That supports reading the 2009 evaluation as a hinge, but it does **not** show that the 2015 programme drew on it.

**H2d. A new kind of mechanism.** Removing barriers (regulation, rigidities) appears as a cause only in 2015. Earlier programmes describe adding inputs or cooperation, not removing obstacles.

**What would weaken these hypotheses:**
- the 2007 or 2011 programmes already state the firm-dynamics theory (the shift would then be earlier and gradual);
- the 2008 strategy frames growth through entrepreneurship and demand (the shift would then come from the strategy, not the evaluation);
- the R&D-to-zero result disappears once GP74 is coded in full rather than sampled.

## 4. Next steps

1. **Code GP70 (2007) and GP72 (2011)** to locate the turning point.
2. **Get the 2008 strategy (ST2008)** from the web archive, then code it.
3. **Code GP74 and GP68 in full**, not by sampling, so that the counts mean more.
4. **A human spot-check** of about 10 claims per document before anything is published.
5. **Code GP77 (Orpo, 2023)** to see whether the 2015 theory persists.
