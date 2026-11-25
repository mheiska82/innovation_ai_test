# Said vs funded: R&D in Finnish government programmes and state budgets, 1987–2026

*Project 1.2, extension of [analysis v3](analysis_q2_v3.md). Status: 25 November 2026. Story page: [Words first, money later](https://claude.ai/artifact/5G6CEHCLJZcgXAUEWS1RCS); dashboard: [Dashboard 4](https://claude.ai/artifact/9kvnpVHKr248vjyVSJgyCe) ; full narrative: [dashboard](https://claude.ai/artifact/Mwxp27CDnwW6WLswLBUBch) and [write-up](https://claude.ai/artifact/YAkJ731Pg9eWpAxmSECEBG) (all private until shared). Unvalidated: the claims have one coder (Claude).*

## Question

When Finnish government programmes say that R&D drives growth, does state R&D funding follow?

## Data

- **What governments said:** the 560 claims in [`coding/claims_v0.4.csv`](coding/claims_v0.4.csv). For each programme, core claims tagged `rd_technology` are split by rule:
  - **R&D drives growth:** a causal or rationale claim whose stated outcome matches growth, productivity, competitiveness, prosperity, welfare, employment, exports, income, GDP or the economy, with a positive direction.
  - **Measures and targets:** claims of type `instrument`.
  - **Doubts or cuts:** claims with a negative or doubt direction.
- **What governments funded:** Statistics Finland, *Government R&D funding in the state budget*, table 13vw (1975–2026), last updated 26 August 2026, downloaded 25 November 2026 ([`data/funding_13vw.csv`](data/funding_13vw.csv)).
  - The figures are state budget appropriations and authorisations, meaning the intention to spend, in current prices.
  - 2026 is preliminary. GDP shares for 2024–2026 are preliminary, and the 2026 GDP is a Ministry of Finance forecast.
- **Terms:** [`data/government_terms.csv`](data/government_terms.csv). Each term runs from the programme year, whose budget the government inherited, to the last budget it set (the next programme year). The Orpo term is ongoing and ends at 2026 here.
- **Decisions:** [`data/rd_policy_decisions.csv`](data/rd_policy_decisions.csv) lists 11 dated decisions from 1983 to 2026, each with a public source and a short excerpt.
- **Result table:** [`data/said_vs_funded_terms.csv`](data/said_vs_funded_terms.csv).

## Evidence: the numbers

| Government | Programme | R&D drives growth | Measures and targets | Doubts or cuts | GDP share start → end (%) | Share of state spending, change (pp) | €, change (%) |
|---|---|---|---|---|---|---|---|
| Holkeri | 1987 | 0 | 2 | 0 | 0.71 → 0.92 | +0.13 | +66.2 |
| Aho | 1991 | 0 | 3 | 0 | 0.92 → 0.94 | +0.24 | +16.3 |
| Lipponen I | 1995 | 1 | 3 | 0 | 0.94 → 1.00 | +1.49 | +37.1 |
| Lipponen II | 1999 | 1 | 2 | 0 | 1.00 → 0.96 | −0.17 | +13.9 |
| Jäätteenmäki / Vanhanen I | 2003 | 5 | 4 | 0 | 0.96 → 0.93 | +0.08 | +19.7 |
| Vanhanen II / Kiviniemi | 2007 | 1 | 4 | 0 | 0.93 → 1.05 | −0.31 | +19.1 |
| Katainen / Stubb | 2011 | 3 | 5 | 1 | 1.05 → 0.95 | −0.43 | −3.4 |
| Sipilä | 2015 | 0 | 4 | 2 | 0.95 → 0.84 | −0.13 | +0.4 |
| Rinne / Marin | 2019 | 6 | 7 | 1 | 0.84 → 0.86 | −0.75 | +16.9 |
| Orpo (ongoing) | 2023 | 6 | 5 | 1 | 0.86 → 1.08* | +0.63 | +32.9 |

\* 2026 is preliminary.

Records in the series (1975–2026):

- **Largest one-year rise since 1975:** +26.11 % in 1997.
- **Largest one-year cut in the series:** −8.25 % in 2016.
- **R&D's share of state spending** (excluding debt servicing):
  - highest in 1999, at 4.67 %;
  - 2.96 % in 2023, the lowest since 1993.
- **GDP share:** 1.08 % in 2026 (preliminary), the highest since 2010 (1.10 %).
- **State spending** (excluding debt servicing) grew 46.4 % between 2019 and 2023.

## Extracted relations: four moments

1. **1995 programme → 1997 budget: words, then money.** The 1995 programme pledged to support "nostaa tutkimus- ja tuotekehitysvarojen kansantuoteosuutta" (C324). Two years later came the largest one-year rise in the series since 1975.
2. **2015 programme → 2016 budget: words and money fell together.**
   - The 2015 programme has no claims that R&D drives growth. Its growth claim is: "Suomen talous ja työllisyys kyetään kääntämään kasvuun vain yrittäjyyden ja työn tekemisen kautta." (C246).
   - The 2016 budget made the largest one-year cut in the series.
3. **2019 programme → 2020–2023 budgets: words without a matching rise in share.**
   - The programme has six R&D-drives-growth claims and pledged a roadmap to 4 % (C432).
   - The GDP share moved from 0.84 % to 0.86 %.
   - R&D's share of state spending fell to its lowest since 1993. State spending itself grew 46.4 % over these years (the pandemic), which pulls the share down. In euros, R&D funding rose 16.9 %, unadjusted for inflation.
4. **2021 commitment → 2023 law → 2024–2026 budgets: the money followed the law.**
   - In December 2021 all parliamentary parties committed to 4 % of GDP by 2030.
   - The R&D funding act (1092/2022, in force from 1 January 2023) sets state R&D funding on a path to 1.2 % of GDP in 2030.
   - The GDP share rose from 0.86 % (2023) to 1.08 % (2026, preliminary).

## Interpretation (hypotheses, not findings)

- **H-SF1: the words lead and the money lags.** Only in 2015 did words and money move together within a single term. Elsewhere the money moved one or more terms after the words (1995 → 1997, 2019 → 2024).
- **H-SF2: a law, not a programme, closed the gap.** The rise from 2024 coincides with a cross-party commitment written into law. A coalition programme was not enough in 2019–2023. Testing this would need the budget negotiations themselves, which are outside this corpus.
- **H-SF3: 1999 was the high-water mark of priority.** R&D's share of state spending peaked in 1999. That year's programme called knowledge "keskeisin tuotannontekijä" (C354).

## Limits

- **Measures.**
  - The GDP share rises when GDP falls (1991–1993, 2009).
  - The share of state spending falls when other spending surges (2020–2023).
  - Euros are nominal.
- **Appropriations are not spending.** Budget figures are intentions; supplementary budgets and actual payments revise them.
- **Claims.** Claim counts are small, so a single claim changes a term's count. The 1990s programmes are short. The claims are unvalidated.
- **Timing is not causation.** Budgets also answer to the economy, to other priorities and to Parliament.
- **Not an evaluation of any agency.** Only the national total is used.

## Note on the author's position

The author works at Business Finland, which channels a large part of state R&D funding. This analysis is a personal project on public data. It describes what governments said and budgeted, makes no recommendation on funding levels, and does not use or evaluate any agency's own data.
