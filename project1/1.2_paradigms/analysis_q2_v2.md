# Research question 2, analysis v2: when does Finland's theory of prosperity change?

*Project 1.2. Status: 10 November 2026. Based on 275 claims in [`coding/claims_v0.3.csv`](coding/claims_v0.3.csv), coded under [`coding/CODING_GUIDE.md`](coding/CODING_GUIDE.md) v0.3, with coverage logged in [`coding/scope_v0.3.md`](coding/scope_v0.3.md). Replaces [analysis v1](archive/analysis_q2_v1.md).*

## 0. The question and how it is answered

**Question.** When does the underlying theory of how Finland creates prosperity change? In particular, when does R&D stop being the stated engine?

**Documents.** Five government programmes, plus the 2009 innovation-system evaluation as an outside view:

| ID | Year | Government | Claims (all / core) | Coverage |
|---|---|---|---|---|
| GP64 | 1987 | Holkeri | 20 / 16 | whole programme read |
| GP68 | 2003 | Jäätteenmäki / Vanhanen I | 59 / 50 | full protocol |
| EV2009P | 2009 | International evaluation (outside view) | 11 / 11 | key sections only (not a programme) |
| GP70 | 2007 | Vanhanen II | 69 / 60 | full protocol |
| GP72 | 2011 | Katainen | 62 / 58 | full protocol |
| GP74 | 2015 | Sipilä | 54 / 47 | full protocol |

**Method (new in v2: full coding).**
1. **Scope.** A claim is any statement linking a driver to an economic outcome: growth, productivity, competitiveness, employment, exports, innovation, structural renewal, or the welfare state's financial base. EU-level, purely social and public-administration claims are out of scope. One exception is coded at low weight and flagged.
2. **Coverage, two tiers.**
   - **Read in full:** every chapter on the economy, business and innovation, labour, education and science, regions, energy and ownership.
   - **Screened:** all other chapters (foreign policy, justice, health and social services, and so on) were screened sentence by sentence for economic-outcome words, and every hit was read in context. The chapter-by-chapter log is in `scope_v0.3.md`.
   - The screen is not used alone. It found only 25 of the 41 claims previously coded by hand, so it is a backstop, not a substitute.
3. **Coding.** Each claim is coded as cause (X) → stated mechanism (M) → outcome (Y), with its condition, direction (+, − or ? for doubt), chain links, theory tags, weight and a verbatim excerpt.
4. **Excerpt check.** All 275 excerpts are machine-checked: 184 match after whitespace normalisation, and 91 more match letter for letter once the PDF text layer's split words are joined.
5. **Counting.** Core claims per document are counted by "engine" tag, and shares are used because the documents differ in length.

**Status.** One model coded and reviewed every claim, and no human has checked them. The counts are signals, not statistics.

**Coverage gap (noted 11.11.2026).** v2 stops at 2015. It can date when R&D stops being the stated engine, but not whether that is a lasting break or a dip: the programmes after Sipilä are not coded yet.
- **GP75** (Rinne 2019, also used by Marin) has not been uploaded to the workspace.
- **GP77** (Orpo 2023) arrived on 11.11.2026 and is next in the coding queue.

Both matter because R&D returns as a policy goal in that period: the 4 % target in 2019 and the R&D funding law of 2022 (Project 2, AN2022). The 1990s programmes (GP65 Aho 1991, GP66 Lipponen 1995, GP67 Lipponen II 1999) are also not coded, so the jump from 1987 to 2003 hides the decade when the national innovation system arrived. The short continuation programmes GP71 (Kiviniemi 2010) and GP73 (Stubb 2014) are left out on purpose.

## 1. Evidence: dating the R&D engine

R&D claims with a positive, economy-wide effect, as distinct from sector-specific R&D or budget cuts:

| | 1987 | 2003 | 2007 | 2011 | 2015 |
|---|---|---|---|---|---|
| R&D as a national engine | 2 | 9 | 5 | 6 | 1 (a targeting rule) |
| Sector-specific R&D | – | – | 1 | 2 | 1 |
| R&D intensity target | – | – | 4 % (C134) | 4 % kept (C202) | none |
| Doubt or cuts | – | – | – | 1 doubt (C205) | 2 cuts (C274, C275) |

The key passages:

- **2007:** productivity "voi perustua vain uusien ideoiden hyödyntämiseen ja uuden teknologian luomiseen…" (C118). Section 3.4 is titled "Innovaatiokyky kilpailukyvyn ja tuottavuuden kasvun moottoriksi" (C131). The programme describes itself as resting on a strategy "osaamiseen ja innovaatioihin perustuvassa" (C170).
- **2011, the turning point.**
  - **R&D is still affirmed:** basic and applied research are "keskeistä pitkällä aikavälillä" (C204), and the 4 % target stays (C202).
  - **It is redirected:** funding shifts to "pieniin ja keskisuuriin, kasvuhakuisiin… yrityksiin" (C203).
  - **It is questioned for the first time:** after fifteen years of growth in R&D resources, it is "perusteltua arvioida saavutettuja tuloksia" (C205).
  - **A new bottleneck is diagnosed:** the scarcity of growth firms and risk capital, "siirryttäessä tuotekehityksestä tuotantoon ja markkinointiin" (C206).
- **2015.**
  - **No national R&D causal claim and no intensity target.** The only national RDI sentence is a rule targeting digital services and growth firms (C266).
  - **The break happens in the savings annex, not in the theory chapters:** Tekes R&D grants are cut by €95 million and redirected "kasvuhakuisiin yrityksiin ja radikaaleihin innovaatioihin" (C274), and the SHOKs are wound down (C275).

**Dating.** The R&D engine peaks in **2003–2007**, is **kept but doubted and redirected in 2011**, and is **dropped in 2015**. In 2015 the change is made by budget cuts rather than by any argument in the text.

## 2. Extracted relations: engines of prosperity

Share of core claims carrying each tag. A claim can carry several tags. Tags with fewer than 5 % everywhere are omitted.

| Engine | 1987 | 2003 | 2007 | 2011 | 2015 | EV2009 |
|---|---|---|---|---|---|---|
| Knowledge, competence | **38 %** | 22 % | 13 % | 12 % | 9 % | 0 % |
| R&D, technology | 12 % | 18 % | 10 % | 16 % | 9 % | 27 % |
| Innovation (broad) | 0 % | 0 % | **13 %** | 2 % | 0 % | 9 % |
| Entrepreneurship, firms | 6 % | 20 % | 13 % | 19 % | **32 %** | 36 % |
| Deregulation, structural reform | 0 % | 0 % | 2 % | 2 % | **32 %** | 0 % |
| Cost competitiveness | 6 % | 10 % | 7 % | 5 % | **15 %** | 0 % |
| Labour supply, activation | 6 % | 20 % | **25 %** | 16 % | 9 % | 0 % |
| Sector choice | 0 % | 4 % | 7 % | **19 %** | 13 % | 0 % |
| Exports | 6 % | 6 % | 7 % | **14 %** | 4 % | 0 % |
| Sustainability as growth | 0 % | 2 % | 5 % | 9 % | 13 % | 0 % |
| Regions as engines | 6 % | **16 %** | 10 % | 5 % | 2 % | 9 % |
| Structural adaptation | **31 %** | 0 % | 2 % | 7 % | 0 % | 0 % |
| Growth → welfare state | 0 % | 6 % | **12 %** | 7 % | 0 % | 0 % |
| Location factors (tax, infrastructure) | 0 % | 12 % | 3 % | 10 % | 4 % | 0 % |
| Claims of failure or doubt (count) | 0 | 1 | 1 | 3 | 7 | 6 |

Raw counts are in [`data/q2_engines_v2.csv`](data/q2_engines_v2.csv).

## 3. Interpretation (hypotheses, revised)

**H2a, revised again: layering with a dated break.** The engines are mostly added rather than replaced. The R&D engine is the exception: it is affirmed until 2011 and dropped in 2015 (§1). 2007 is the high point of the "innovation system" theory, and 2011 is the bridge. The 2009 evaluation's diagnosis of growth firms and risk capital reaches the programme in 2011 (C206), two years after the evaluation, though the programme does not cite it.

**H2b, holds: knowledge declines steadily.** Knowledge and competence fall from 38 % of claims in 1987 to 9 % in 2015. Its role also narrows: from adaptation capacity (1987), to employability and innovation input (2003–2007), to a necessary but insufficient condition (2015, C024).

**H2c, holds: the diagnosis turns to failure.** Claims of failure or doubt rise from 0 → 1 → 1 → 3 → 7 across the programmes. The first doubt about R&D is in 2011 (C205).

**H2d, sharpened: deregulation is the real 2015 novelty.** Structural reform and deregulation go from almost nothing to 32 % of claims. The 2015 master diagnosis is that "perimmäiset ongelmat ovat rakenteellisia" (C243), and its remedy claim is exclusive: growth comes "vain yrittäjyyden ja työn tekemisen kautta" (C246). This mirrors 2007's exclusive innovation claim (C118). A mild precursor exists in 2007 ("parantamalla säädösympäristöä", C169).

**H2e, corrected: cost competitiveness is constant; its mechanism changes.**
- **Present throughout.** Price competitiveness is a stated condition in 2003 (C069) and 2007 (C122: "Vahva talouskasvu edellyttää hyvää hintakilpailukykyä").
- **What changes is the route:**
  - In 2003–2011 it runs through consensual incomes policy (C123, C186).
  - In 2015 it runs through a unit-labour-cost target (C052), local bargaining (C257) and looser employment protection (C258).
- **Contrast with 2007:** the 2007 programme called the permanent job "työn tuottavuuden tae" (C167).

**H2f, extended: sectors become engines in 2011, after Nokia.** Sector choice peaks in 2011 (19 %), with services, cleantech, energy technology and the creative industries. The cleantech line runs unbroken from 2007 (C156) through 2011 (C218) to 2015 (C261). The 2015 bioeconomy has a 2011 precursor in the forest programme (C219).

**H2g, new: three Nokia-era framings of ICT (link to question 4).**
1. **2003:** the ICT *producer* position is itself the engine, with spillovers "koko kansantaloudessa" (C102).
2. **2011:** the mobile-phone sector's restructuring is framed as an *opportunity* for growth and renewal (C210), and accelerators appear for the first time (C213).
3. **2015:** ICT is a general-purpose *productivity* lever, "tuottavuusloikan" (C265), not a sector.

**H2h, new: labour supply peaks in 2007; growth-for-welfare disappears in 2015.**
- **Labour supply and activation peak in 2007 (25 %).** That year, insufficient labour is named the biggest threat to growth (C127).
- **The welfare framing changes.** In 2007 growth is justified by the welfare state it finances (12 %). By 2011, fiscal sustainability has become the *precondition* of growth (C188: "Vain tätä kautta…"), and in 2015 no core claim argues from growth to welfare.

## 4. Continuity or break?

**Layering, with one dated break and one new engine.**
- **Continuity:** knowledge, cost competitiveness, location factors and labour supply are present in every programme from 2003 to 2015, with changing weights.
- **The break:** the R&D engine, affirmed in 2003–2011, is dropped in 2015, chiefly through the budget.
- **The new engine:** deregulation and structural reform, which is close to absent before 2015 and dominant in it.
- **Entrepreneurship:** present from 2003 and strongest in 2015. It does not appear suddenly.

## 5. What full coding changed (robustness)

- **v1 overstated R&D.** v1 coded key sections only, and those sections were mostly the innovation chapters. In 2003, R&D was 42 % of the key-section claims (5 of 12) but is 18 % of the full set. Labour-supply claims went from 0 to 10. v1's "R&D 5 → 0" becomes "9 national claims in 2003 → 1 targeting rule plus 2 cuts in 2015": the direction is the same, but the size is now honestly measured.
- **v1's 2015 picture holds.** Deregulation and entrepreneurship dominate under full coding too.
- **The test v1 set for itself.** v1 named one finding that would weaken its account: 2007 or 2011 already dropping R&D. They did not.

## 6. Limitations

- **Single model, unvalidated.** Claude both coded and reviewed every claim.
- **The scope rule is a judgement.** Bare action items with no stated outcome are not coded. This undercounts instruments such as the 2003 seed-capital sentence.
- **Screened chapters may miss claims phrased without economic-outcome words.**
- **Missing comparison documents.** The 2009 evaluation is still coded by key sections only, and the 2008 national innovation strategy (ST2008) is not yet in the corpus.
- **Counting by tag gives a multi-tag claim weight under each of its tags.**

## 7. Next steps

1. **Human spot-check.** About 10 claims per programme, stratified by coverage tier.
2. **Add ST2008.** Did the 2008 strategy's "broad-based innovation policy" (cf. C151) state a firm-dynamics theory before 2011?
3. **Code GP77 (Orpo, 2023).** Does R&D return with the 4 % law, or does the deregulation theory persist?
4. **Project 2 comparison.** Does the 2011 doubt about R&D follow the Council's 2010 review? This needs RC2010 (Project 2 corpus gap).
5. **Question 1.3 (continuity or break).** Re-use these claims with a firm-dynamics codebook.
