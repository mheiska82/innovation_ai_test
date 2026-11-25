# Continuity or break? The start-up ecosystem in Finnish government programmes, 1987–2023

*Project 1.3, analysis v1.2. Status: 25 November 2026. Built on the ten coded programmes and the 2008 Government innovation report (AN2008) from [Project 1.2](../1.2_paradigms/analysis_q2_v3.md), plus three outside evaluations added in v1.1 (EV2009F, OE2017, OE2022) and four Research and Innovation Council documents added in v1.2 (RC2014, RC2017, RC2024, RC2026). Unvalidated: one coder (Claude).*

## Question

Was the start-up ecosystem a continuation of the older innovation system, or a break from it? The question is asked of the programmes only: what each government said it would create, keep, redirect or end. It does not evaluate any instrument or agency.

## Data and method

Three tests, all on public documents and all traceable to verbatim excerpts.

1. **Instrument coding** ([`data/instruments_v0.1.csv`](data/instruments_v0.1.csv)).
   - There are 26 items, each naming an instrument, programme or organisation behind innovation and growth firms: 24 claims from claims v0.4, plus 2 passages from the programme texts that are not coded claims.
   - Each item has an action:
     - *create*, *use* or *strengthen*;
     - *continue*, *redirect* or *merge*;
     - *reform*, *reframe* or *end*.
   - Each item may link to an earlier item (`link_to`). The `link_basis` column says whether the link is stated in the text (the same instrument named, or a word such as "jatketaan" or "sijasta") or inferred by the coder.
   - All 26 excerpts pass the excerpt checker (18 exact, 8 after PDF spacing).
2. **Vocabulary of the start-up era** ([`scripts/startup_terms.py`](scripts/startup_terms.py) → [`data/startup_terms.csv`](data/startup_terms.csv), with example passages).
   - It counts Finnish stems in the full texts of the eleven documents, per 10,000 words. The terms are innovation system, ecosystem, growth firm, start-up, venture capital, incubator or accelerator, and commercialisation.
   - Ecological senses of "ekosysteemi" are removed by a context rule. Every match left in the 2019 and 2023 programmes was read.
3. **Growth routes in claims** ([`scripts/families.py`](scripts/families.py) → [`data/claim_families.csv`](data/claim_families.csv), [`data/family_shares.csv`](data/family_shares.csv)).
   - It marks which routes to growth each core claim's Finnish excerpt names, using stems:
     - knowledge and R&D;
     - networks and ecosystems;
     - risk capital;
     - growth firms and start-ups;
     - entrepreneurship in general;
     - markets.
   - The test asks whether growth-firm and risk-capital claims still name knowledge or R&D (continuity of the route) or stand without it (a new route).
   - The 2009 evaluation (EV2009P) is left out because it is in English.
4. **Outside evaluations** (added in v1.1).
   - The documents are:
     - the 2009 international evaluation, full report (EV2009F) and policy report (EV2009P);
     - the OECD Reviews of Innovation Policy: Finland 2017 (OE2017);
     - chapter 2 of the OECD Economic Survey of Finland 2022, "Rebooting the innovation ecosystems" (OE2022, PDF pages 71–120).
   - English stems are counted per 10,000 words with [`scripts/outside_terms.py`](scripts/outside_terms.py) → [`data/outside_terms.csv`](data/outside_terms.csv).
   - 20 claims are coded from targeted passages on the innovation system, ecosystems, start-ups, growth firms, venture capital, SHOKs and Nokia ([`data/claims_context_q3_v0.2.csv`](data/claims_context_q3_v0.2.csv), C561–C580). All 20 excerpts pass the checker (17 exact, 3 after PDF spacing).
   - These are targeted claims, not full coding, so they are not added to the shares in claims v0.4.
5. **Council documents** (added in v1.2).
   - The four Council documents already counted in Project 2 go through the same Finnish stem count (`startup_terms.py`).
   - Six claims on the innovation system and ecosystems are coded from them (C581–C586, same file). All six pass the checker.
   - The Council's 2010 policy review (RC2010) and its 2008 interim review are corpus gaps. Their old minedu.fi addresses are retired, and no copy was found online.

## Evidence: the numbers

### Instruments by action (26 items)

| Action | Items | Years |
|---|---|---|
| Create | 11 | 1999 (2), 2003, 2007 (2), 2008, 2011, 2015, 2019 (2), 2023 |
| Strengthen or use | 6 | 1995, 2003, 2007, 2011 (2), 2023 |
| Continue | 2 | 2015, 2019 |
| Redirect | 2 | 2011, 2015 |
| Merge | 2 | 2007, 2023 |
| Reform or reframe | 2 | 1995, 2008 |
| End | 1 | 2015 |

### Stated lines of descent

| From | To | How the text links them |
|---|---|---|
| 1995: the national innovation system, developed as a whole (C323) | 2008: ecosystems *instead of* national innovation systems (C382) | "Kansallisten innovaatiojärjestelmien sijasta huomio kiinnittyy innovaatioiden ekosysteemeihin" |
| 2003: Centre of Expertise programme (C093) | 2007: cluster-based OSKE strengthened (C155) | Same programme named |
| 2007: SHOKs created (C135) | 2015: SHOKs phased out (C275) | "Tekesin Shokit ajetaan vaiheittain alas." |
| 2011: funding shifted to growth-seeking firms (C203) | 2015: the targeting continued (C266) and Tekes grants turned to growth firms (C274) | "Jatketaan … kohdentamista" and "yhä enemmän"; the predecessor is inferred |
| 2019: agreements with university cities (C441) | 2023: the 18 innovation-ecosystem agreements strengthened (C490) | "tehtyjen innovaatioekosysteemisopimusten, joita nyt on kahdeksantoista" |

### Start-up-era words in the programmes (mentions per 10,000 words)

| Document | Innovation system | Ecosystem | Growth firm | Start-up | Venture capital (count) |
|---|---|---|---|---|---|
| 1995 | 2.57 | 0 | 0 | 0 | 1 |
| 1999 | 4.41 | 0 | 0 | 0 | 0 |
| 2007 | 0.61 | 0 | 1.21 | 0 | 5 |
| **AN2008** | **31.07** | **8.18** | **13.08** | 0 | 4 |
| 2011 | 0 | 0 | 2.80 | 0 | 4 |
| 2015 | 0 | 0 | 0.53 | 0 | 1 |
| 2019 | 0 | 3.87 | 0.97 | 0.48 (2 mentions) | 2 |
| 2023 | 0.17 | 1.21 | 0.69 | 0.17 (1 mention) | 3 |

**Council documents** (same stems, added in v1.2):

| Document | Innovation system | Ecosystem | Growth firm | Start-up | Venture capital (count) |
|---|---|---|---|---|---|
| RC2014 (Council policy review 2015–2020) | 14.96 | 4.67 | 3.74 | 1.87 | 4 |
| RC2017 (Council vision and roadmap 2030, a 10-page slide deck) | 10.70 | 117.65 (11 mentions) | 0 | 0 | 0 |
| RC2024 (multi-annual R&D funding plan) | 1.67 | 7.53 | 1.67 | 5.02 | 1 |
| RC2026 (national strategic RDI choices) | 1.33 | 13.30 | 1.33 | 0.66 | 1 |

RC2017 is very short (935 words), so its rate is indicative only; the count is 11 mentions.

1987, 1991 and 2003 have no mentions of the first four terms. Full counts and example passages are in `data/startup_terms.csv` and `data/startup_terms_examples.csv`.

### Growth routes in core claims

| Era | Core claims | Name knowledge or R&D | Name growth firms or risk capital | …of which also name knowledge or R&D |
|---|---|---|---|---|
| 1987–1999 | 103 | 35 (34 %) | 5 | 0 |
| 2003–2011 (incl. AN2008) | 185 | 73 (39 %) | 13 | 3 |
| 2015–2023 | 201 | 62 (31 %) | 7 | 4 |

### Outside evaluations (mentions per 10,000 words)

| Document | Innovation system | Ecosystem | Growth firm | Start-up | Venture capital |
|---|---|---|---|---|---|
| EV2009P (2009) | 24.26 | 0 | 17.16 | 0.69 | 2.77 |
| EV2009F (2009) | 13.83 | 0 | 20.95 | 1.93 | 4.61 |
| OE2017 | 11.35 | 2.59 | 0.65 | 8.97 | 4.32 |
| OE2022, chapter 2 | 1.73 | 20.82 | 0 | 2.17 | 0.43 |

"Growth firm" includes the 2009 evaluation's abbreviation HGEF (high-growth entrepreneurial firm). The rates are not comparable with the Finnish counts above, because the languages and stems differ; read them within this table only.

## Extracted relations

1. **The start-up instruments have roots in the 1990s.**
   - The 1995 programme already promises risk finance and networking for innovative SMEs: "parantamalla erityisesti niiden vakuus- ja riskirahoitusmahdollisuuksia" (C320).
   - The 1999 programme launches an entrepreneurship project for "uusien yritysten perustamista" (C351).
   - Growth-firm risk capital follows in 2007, with pension companies (C136), and Sitra's start-up functions move to Finnvera (GP70, p. 50).
2. **The words broke first, in a report, not a programme.**
   - The 2008 Government report names ecosystems *instead of* the national innovation system (C382). In that one document "innovation system" appears 19 times and "ecosystem" 5 times.
   - The programmes then drop "innovation system" (none in 2011, 2015 or 2019).
   - They take up "ecosystem" only in 2019, eleven years later.
3. **Most change is redirection and merging, not ending.**
   - Of 26 items, one is an ending: the SHOKs, created in 2007 and phased out in 2015.
   - The R&D funding instrument itself is kept and turned towards growth firms, in 2011 (C203) and 2015 (C266, C274).
   - Public venture capital is merged twice: Sitra into Finnvera in 2007, and three state funds into Suomen Teollisuussijoitus in 2023 (C484).
4. **Growth-firm talk peaks around 2008–2011 and is joined to R&D afterwards.**
   - Claims naming growth firms or risk capital rise from 5 (1987–1999) to 13 (2003–2011), then fall to 7 (2015–2023).
   - In 2015–2023, four of those seven also name R&D or knowledge: R&D money is redirected to growth firms rather than replaced.
   - The 2023 programme states the start-up ecosystem as a goal: "Luodaan edellytyksiä maailman parhaan startup- ja kasvuyritysekosysteemin kehittymiselle." (GP77, p. 100).

5. **The outside evaluations carried growth entrepreneurship first, and ecosystems only later.** *(v1.1)*
   - The 2009 international evaluation never uses "ecosystem". It frames the problem inside the innovation system: "The Finnish innovation system suffers from a mismatch between 1) the growing demand by Finnish HGEFs for global insight, foreign expertise, international networks, and 2) an insufficient supply of inward foreign spillovers…" (C561, EV2009F p. 149). It names growth entrepreneurship as an orphan: "The two main challenges – relatively weak internationalization and somewhat lacking growth entrepreneurship – remain orphans in the Finnish system." (C564, p. 302).
   - The 2011 programme then turns to growth firms (relation 4 above). That is a match in timing, not a proof of influence.
   - The OECD 2017 review uses both vocabularies. It speaks of an "entrepreneurship ecosystem" (C572) and records the redirection seen in the programmes: "Tekes has been instructed by successive governments to focus increasingly on start-ups and entrepreneurship" (C569, p. 37). It also notes the discontinuation of SHOK funding (C570).
   - By 2022 the OECD frames Finland's task as rebooting its innovation ecosystems after Nokia (C575). It uses "innovation system" and "ecosystem" side by side (C576), and links the weakening to "the rapid withdrawal of public funding for applied research and innovation collaboration" (C578, p. 86).

6. **The Council bridges the eleven-year gap.** *(v1.2)*
   - In 2014 the Council still writes mainly of the innovation system: "Innovaatiojärjestelmää kehitetään kokonaisuutena ja kansainvälistetään läpikäyvästi." (C584, RC2014 p. 14). It brings in ecosystems alongside: "Globaalien osaamiskärkien tavoittelu vaatii laaja-alaista, monen toimijan vuorovaikutteista verkostoa, ekosysteemiä." (C581, p. 21).
   - The 2017 vision makes growth ecosystems one of its four main headings. It sets the target "Suomessa on useita yritysvetoisia miljardiluokan kasvuekosysteemejä, jotka tuottavat kilpailukykyisiä ratkaisuja globaaleihin tarpeisiin" (C586, RC2017 p. 7).
   - The 2019 programme uses the same phrase: "Suomeen syntyy uusia miljardiluokan ekosysteemejä" (C431, GP75 p. 99). This is the closest textual echo in the corpus between a Council document and a programme.
   - After 2019 the Council's documents use "ecosystem" far more than "innovation system" (RC2024, RC2026).

## Interpretation (hypotheses, not findings)

- **H3a: continuity by conversion.** The start-up ecosystem grew mainly by converting existing instruments (R&D funding redirected, public funds merged) and layering new ones on top, not by replacing the innovation system. In the programmes, the only instrument ended outright is the SHOKs.
- **H3b: a break in words, not in institutions.** The clearest break is conceptual: "ecosystem instead of the innovation system" in 2008. In the programmes it shows as a gap, with no "innovation system" after 2007 and no "ecosystem" until 2019, rather than as abolished organisations.
- **H3c: 2011 is the hinge.** The 2011 programme redirects funding to growth firms, strengthens public venture capital, names accelerators and plans a capital-market strategy. 2015 continues that turn while cutting.
- **H3d (revised in v1.1): two frames, two routes.**
  - *Growth entrepreneurship* came with the outside view. The 2009 evaluation makes high-growth firms its central problem, and the 2011 programme follows.
  - *Ecosystem* came from inside. The Government's own 2008 report uses it first. The 2009 evaluation does not use it at all. The OECD adopts it as its main frame only in 2022, after the 2019 programme.
  - On this evidence, the ecosystem word was not imported from the international reviews.
  - *(v1.2)* The Council is the most likely bridge in the corpus: ecosystems appear beside the innovation system in 2014, become a main heading in 2017, and the 2019 programme echoes the Council's "billion-euro ecosystems". This is textual evidence of borrowing, not of who drafted what. The missing 2010 review could move the Council's first use earlier.

## Limits

- **Programmes only.** Programmes say what governments intend. Whether instruments were actually created, kept or ended needs budgets, laws and annual reports. Those are not coded here, and agency annual reports would be used in public versions only.
- **Coverage.** Instrument items come from claims coded for question 2 plus two passages. A programme may name instruments outside the coded chapters.
- **One coder.** Actions and links were coded by Claude. Of the eight links between items, four are stated in the text (the same instrument named, or "sijasta"), two carry a stated continuation word but an inferred predecessor, and two are inferred; all are flagged.
- **Small counts.** The growth-route test rests on 25 growth-firm or risk-capital claims in all. The stem rules are in the scripts, and every match is listed in `data/claim_families.csv`.
- **Not an evaluation.** Nothing here judges whether any instrument or agency worked.
- **Missing documents.** The 2008 strategy proposal (ST2008) is not online. The outside evaluations are coded from targeted passages only, and their text layer has some lower-cased words, which the excerpts keep as extracted.
- **Outside evaluations are other people's assessments.** Claims C561–C580 record what the evaluators wrote, and C581–C586 what the Council wrote. They are evidence of the outside view, not findings of this project.

## Where it is shown

The [narrative dashboard](https://claude.ai/artifact/Mwxp27CDnwW6WLswLBUBch) carries this analysis as Act 5 ("the start-up turn") and a section "Who said 'ecosystem' first?" with the instrument list. Narrative dashboard and write-up are private until shared.

## Next steps

1. Code EV2009F, OE2017 and OE2022 in full (v1.1 codes targeted passages).
2. Find the Council's 2010 review, *Tutkimus- ja innovaatiopoliittinen linjaus 2011–2015*, and the 2008 interim review. Library or archive copies would do; they would show whether the Council used "ecosystem" before 2014.
3. Extend the instrument coding to all programme chapters, not only the coded claims.
4. Do a human spot-check of the 26 instrument items.
