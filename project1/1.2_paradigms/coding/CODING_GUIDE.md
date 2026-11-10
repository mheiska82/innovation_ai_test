# Coding guide: theory-of-prosperity claims (research question 2)

*Project 1.2. Status: 10 November 2026. Version 0.3 (full coding of five programmes; see §4c).*

> **Decision (10.11.2026):** the claims are coded by Claude only (single coder). There is no human gold standard for now. As a result, results are labelled *unvalidated*, and AI extraction can't be scored against this set: scoring it would be Claude grading Claude. A human spot-check of a sample remains the way to validate it later.

**Purpose.** Question 2 asks when the theory of how Finland creates prosperity changes. Word counts can't answer that, because a theory is a claim about causes. This guide defines how such claims are coded by hand. The hand-coded set is then the gold standard for testing the AI claim extraction (`prompts/claim_extraction.md`).

## 1. What counts as a claim

A **claim** is one statement, usually a sentence, that links something to an economic or social outcome. It is coded when it does at least one of the following:

- names a **cause** of prosperity, such as *perustuu*, *edellyttää*, *ratkaisevaa*, "driver of", "source of";
- names a **means** for reaching a prosperity outcome, such as *jotta*, *-n avulla*, *parannetaan … vahvistamalla*;
- **diagnoses** why prosperity is lacking (a broken link, a barrier);
- states the **rationale** for public action (why the state should act at all).

**Outcomes** that count: growth, competitiveness, productivity, employment, welfare, a strong economic base, national success, export success.

**Not coded:** pure lists of measures with no outcome; sector-only goals (for example health, culture or defence) unless they are linked to prosperity; procedural statements.

## 2. Fields (v0.1)

Each claim is coded as **cause (X) → mechanism (M) → outcome (Y)**. The mechanism is a **mediator**, the channel through which X produces Y. Conditions under which X works (moderators, scope) go in their own field. These are the document's own stated causes. Nothing is inferred to be causal in reality.

| Field | Content |
|---|---|
| `claim_id`, `document_id`, `year`, `author`, `page` | As before. The author is an institution, never a named person. `page` is the PDF page index |
| `claim_type` | `causal` · `diagnosis` · `instrument` · `rationale` · `meta` |
| `cause` (X) | The claimed driver. Required |
| `mechanism` (M) | The mediator, **only if the text states it**; otherwise left empty |
| `condition` | A moderator or scope condition (for example "pieni avoin talous", "jatkossakin"), only if stated |
| `outcome` (Y) | The prosperity outcome. Required |
| `direction` | `+` · `−` · `?` (doubt about a link, v0.3), with "(broken chain)" or "(mismatch)" where the text says a link fails |
| `link_to` | The ID or IDs of claims this one builds on (chains, as in C024 → C025, or C042 + C043 → C044) |
| `inferred` | Which fields the coder supplied rather than the text, if any |
| `theory_tags` | From the codebook in §3 |
| `excerpt_verbatim`, `excerpt_verified` | The exact source words; checked by `verify_excerpts.py`: `yes` (whitespace-normalised match) or `yes (PDF spacing)` (letter-for-letter match once the PDF text layer's split words are joined) |
| `coverage` (v0.3) | `key section (v0.2)` · `read in full` · `screened chapter`: how the claim's chapter was covered (see `scope_v0.3.md`) |
| `coder`, `validation` | `Claude`; `unvalidated (single coder)` |
| `weight` (v0.2) | `core`, or `low` for vision rhetoric, agenda-setting, or outcomes outside market prosperity. Low-weight claims are left out of the engine counts |
| `expert_review` (v0.2) | A review pass written from the stance of an innovation researcher and a policy-maker: `ACCEPT` · `EDIT` · `REJECT` · `ADDED`, with a reason |

**Changes from v0:**
- Mechanisms I had inferred are removed. 10 of the 47 claims now have a stated mechanism.
- Conditions moved to their own column (8 claims).
- `direction`, `link_to` and `inferred` were added. 6 claims have an inferred field, always an implicit cause or outcome.
- C020's excerpt was extended to the full sentence.

## 3. Theory tags (codebook v0)

| Tag | The engine of prosperity is… |
|---|---|
| `knowledge_competence` | knowledge, competence, education (*osaaminen*) |
| `rd_technology` | R&D, technology, technology funding |
| `innovation_growth` | innovation in general, as a source of growth |
| `entrepreneurship_firms` | entrepreneurs, firm creation and growth, management and ownership |
| `commercialisation` | turning research into products and markets |
| `competition_markets` | competition and market selection |
| `productivity_restructuring` | reallocation, firm entry and exit, internal restructuring |
| `cost_competitiveness` | cost and price competitiveness (unit labour costs, incomes policy) |
| `export_competitiveness` | exports, success in international competition, a small open economy |
| `labour_consensus` | labour-market cooperation, incomes policy, working life |
| `macro_stability` | stable macroeconomic policy |
| `deregulation_reform` | removing rigidities, regulation and administration; structural reforms |
| `structural_adaptation` | adapting to structural change in the world economy |
| `location_attractiveness` | Finland as a location for firms (taxation, infrastructure) |
| `digital_ict`, `data` | ICT, digitalisation, data |
| `sustainability` | sustainable development as a source of competitiveness |
| `concentration` | concentrating resources into clusters or critical mass |
| `market_failure` | the public role justified by market failure |
| `growth_to_welfare` | growth as the basis for the welfare state |
| `sector_choice` | specific sectors as growth engines (bioeconomy, cleantech) |
| `council_link` | the programme explicitly relies on a Council document (a link to Project 2) |
| `labour_market` (v0.3) | labour supply, matching, activation, incentives to work |
| `demand_management` (v0.3) | fiscal stimulus, purchasing power, aggregate demand |
| `growth_employment` (v0.3) | economic growth itself as the source of jobs |
| `health_wellbeing` (v0.3) | population health and well-being as a competitive factor |
| `state_ownership` (v0.3) | state ownership as a growth instrument |
| `governance_coordination`, `regional`, `experimentation`, `meta_theory` | as named |

The codebook is expected to change after review. Tags may be merged or split, but every change is logged here.

## 4. Draft v0: how it was made

- **Documents:** GP64 (Holkeri, 1987), GP68 (Jäätteenmäki, 2003, also used by Vanhanen I), GP74 (Sipilä, 2015), and EV2009P (the 2009 international evaluation, Policy Report) as the outside view.
- The 2008 national innovation strategy (ST2008) is **not yet included**: the download returned the ministry's publications page, not the strategy.
- **Coverage:**
  - GP64 was read in full.
  - For GP68, GP74 and EV2009P, the key sections were read in full (vision, situation analysis, economic strategy, technology and business policy, competence; for EV2009P the preface and the growth-entrepreneurship chapter). The rest of each document was searched for sentences that combine an outcome word, a cause word and a driver word.
  - **The draft is therefore not exhaustive**, and the reviewer's added rows are what will show how much was missed.
- **Pre-coded by Claude, not yet reviewed.** It is a draft gold standard only, until the reviewer has gone through every row.
- **Every excerpt was checked by script**: 47 out of 47 were found verbatim.

## 4b. Review pass (v0.2)

A second pass by Claude reviewed every claim from the stance of an innovation researcher and a policy-maker. It recorded each decision in the `expert_review` column, and the results were:

- 43 claims accepted.
- 4 edited, with the edits applied:
  - C005: tag added.
  - C006: type changed to `instrument`.
  - C010: excerpt extended and tag added.
  - C030: competitiveness reclassified as cost competitiveness.
- 5 missed claims added (C048–C052).
- 6 claims given low weight.
- The `competitiveness_exports` tag was split into `cost_competitiveness` and `export_competitiveness`, because "kilpailukyky" means different things in different periods.

**This is not independent validation.** The same model coded and reviewed the claims. The review improves consistency, but a human check is still needed.


## 4c. Full coding (v0.3)

**Why.** v0.2 read only key sections, which were mostly the innovation chapters. That risked overstating R&D and missing labour, cost and regional claims. v0.3 codes five programmes (GP64, GP68, GP70, GP72, GP74) under one protocol, so that their shares can be compared.

**Protocol.**
1. **Read in full:** every chapter on the economy, business and innovation, labour and working life, education and science, regions, energy and ownership. Policy programmes and annexes on tax are included.
2. **Screened:** all other chapters. Every sentence with an economic-outcome word is read in context. The screen alone found 25 of 41 hand-coded claims in a test, so it is used only outside the economic core.
3. **Scope rule.** A sentence is coded when it links a driver to an economic outcome (growth, productivity, competitiveness, employment, exports, innovation, structural renewal, welfare-state financing).
   - **Bare action items with no stated outcome are not coded.**
   - **A repeated claim is coded once**, at its first or fullest statement.
   - **EU-level claims are out of scope.** One exception (C270) is coded low and flagged.
4. **Budget annexes:** R&D cuts in a savings annex are coded as instruments with direction `−` (C274, C275), because they are the evidence for the 2015 break.
5. **Existing v0.2 claims are kept with their IDs.** New claims are C053–C275.
6. **Weights** follow v0.2: `low` for vision rhetoric, purely fiscal or social outcomes, minor sector claims and immigration-as-labour-supply. Low-weight claims are left out of engine counts.

**Result.** 275 claims (242 core), all excerpts verified (184 `yes`, 91 `yes (PDF spacing)`). The coverage log is `scope_v0.3.md`, and the analysis is `../analysis_q2_v2.md`.

**Review column.** For new claims, `expert_review` holds the same reviewer stance as v0.2 (`ADDED (full coding)` for 2003/2015 additions, `ACCEPT` for 2007/2011), with a note on why the claim matters. Coding and review are by the same model, so this is not independent validation.

## 5. Review procedure (for a later human spot-check)

1. Read each row against its source passage, and set `reviewer_decision`.
2. Add missed claims as new rows.
3. Note every disagreement about type or tag in `reviewer_notes`. These feed codebook v1.
4. The reviewed file (from `claims_v0.3.csv`) becomes `claims_gold_v1.csv`, the test set for the AI extraction. Results are reported as precision (how many AI claims are correct) and recall (how many gold claims the AI found).
