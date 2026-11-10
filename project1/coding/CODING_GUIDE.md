# Coding guide: theory-of-prosperity claims (research question 2)

*Project 1. Status: 10 November 2026. Version 0 (draft for review).*

**Purpose.** Question 2 asks when the theory of how Finland creates prosperity changes. Word counts can't answer that, because a theory is a claim about causes. This guide defines how such claims are coded by hand. The hand-coded set is then the gold standard for testing the AI claim extraction (`prompts/claim_extraction.md`).

## 1. What counts as a claim

A **claim** is one statement, usually a sentence, that links something to an economic or social outcome. It is coded when it does at least one of the following:

- names a **cause** of prosperity, such as *perustuu*, *edellyttää*, *ratkaisevaa*, "driver of", "source of";
- names a **means** for reaching a prosperity outcome, such as *jotta*, *-n avulla*, *parannetaan … vahvistamalla*;
- **diagnoses** why prosperity is lacking (a broken link, a barrier);
- states the **rationale** for public action (why the state should act at all).

**Outcomes** that count: growth, competitiveness, productivity, employment, welfare, a strong economic base, national success, export success.

**Not coded:** pure lists of measures with no outcome; sector-only goals (for example health, culture or defence) unless they are linked to prosperity; procedural statements.

## 2. Fields

| Field | Content |
|---|---|
| `claim_id` | C001… |
| `document_id`, `year`, `author` | From the corpus list. Author is an institution or role, never a named person |
| `page` | The PDF page index in `data/text` (printed page numbers can differ). Empty for web-page programmes |
| `claim_type` | `causal` · `diagnosis` · `instrument` · `rationale` · `meta` (a claim about the theory itself) |
| `cause` → `mechanism` → `outcome` | In English, short. Anything implied but not written is marked `(implicit)` |
| `theory_tags` | One or more from the codebook in §3, separated by `;` |
| `excerpt_verbatim` | The exact words from the source. Part of a sentence is allowed; `…` marks a gap |
| `excerpt_verified` | `yes` if the excerpt is found in the text by `verify_excerpts.py`, which normalises whitespace and line-break hyphens only |
| `reviewer_decision` | `accept` · `edit` · `reject` |
| `reviewer_correction`, `reviewer_notes` | What to change and why |

**Missed claims:** the reviewer adds new rows with `coder` = `reviewer` and `reviewer_decision` = `added`. These measure what the extraction misses (recall).

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
| `competitiveness_exports` | cost and price competitiveness, exports, an open economy |
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

## 5. Review procedure

1. Read each row against its source passage, and set `reviewer_decision`.
2. Add missed claims as new rows.
3. Note every disagreement about type or tag in `reviewer_notes`. These feed codebook v1.
4. The reviewed file becomes `claims_gold_v1.csv`, the test set for the AI extraction. Results are reported as precision (how many AI claims are correct) and recall (how many gold claims the AI found).
