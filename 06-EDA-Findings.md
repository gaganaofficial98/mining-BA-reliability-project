# 06 — Exploratory Data Analysis Findings

**Owner:** Gagana Suresh
**Status:** First-pass EDA complete for Q1–Q4 (Master Plan, Week 2, Day 10). Q5 and Q6 require a deeper sensor-threshold analysis than these three aggregate views provide — flagged as the next layer of work, not answered here.
**Last updated:** 10 September 2026

This is the first document in this project where real numbers — not a plan, not a decision, not a schema — actually answer one of the six locked business questions (`Scope-Decisions-and-Limitations-Log.md`, "FINAL business question set," 24 Aug 2026). Every figure below is pulled directly from the three SQL views in `data/core_queries.sql`, run against `data/mining_reliability.db`, and every one carries a provenance tag per the project's three-tag data-integrity rule (Master Plan §1.2): **[DATASET]** = computed directly from `ai4i2020-kestrel.csv`, **[CITED SOURCE]** = an external, referenced benchmark, **[ASSUMPTION]** = a disclosed labeled assumption. Nothing below is fabricated or estimated without one of those three tags attached.

**Technique used to build this document:** structured-output synthesis — each locked business question is answered in a fixed format (number → provenance tag → interpretation → caveat), the same discipline already used for the Data Dictionary's field-by-field spec, applied here to query results instead of column definitions.

**Methodology note — read this before the numbers below.** The queries behind this document were revised on 10 September 2026, one day after they were first built, following an independent adversarial review (memory-isolated critique loop, the same technique used on the BRD, generalized here from documents to SQL). That review found a real bug — a tie-break rule was silently under-counting one failure mode — and it changes the answer to Q2 below, not just its footnotes. Full story: `Scope-Decisions-and-Limitations-Log.md`, "CORRECTION — failure-mode Pareto," 10 September 2026.

---

## Q1 (Tier 1 — Diagnose): How much production time and cost is being lost to unplanned breakdowns?

**Mobile fleet (Medium tier, 14 real assets):**
83 real failures **[DATASET]** × 2.2 hours per repair, a typical-case average from real mine-site repair records **[CITED SOURCE: Rezaei Dashtaki et al. 2025, Scientific Reports; Jakkula et al. 2025, J. Eng. Mgmt & Sys. Eng.]** = **182.6 hours lost, estimated **[ASSUMPTION: hours = count × cited average]**.

Caveat, added 10 Sept 2026: 182.6 hours is a central estimate, not a ceiling. The same cited sources document individual repairs running as long as 45 hours — a handful of unusually bad repairs could push the real total well above this figure. Report this as "approximately 183 hours, typical case," never as a single precise number presented without a range.

**Fixed plant (High tier):** 21 real failures **[DATASET]** — frequency only. No defensible repair-time source exists for this equipment class after two full sourcing passes and an independent verification pass (Scope log, 25 Aug – 1 Sept 2026, Option B). This gap is itself a finding worth stating plainly in the eventual business case: *the industry doesn't publicly track repair time for the mining equipment that matters most, which is a case for better internal CMMS reporting, not a hole in this analysis.*

**Ancillary (Low tier):** 235 real failures **[DATASET]** — frequency only, for a different reason (Option C, 8 Sept 2026): the only proxy source available covers just 3 of the tier's roughly 8 equipment types, and applying it to the whole tier would overreach what the source actually supports.

**Dollar figure:** not yet computed. The downtime-cost-per-hour benchmark is a separate, still-open sourcing decision deliberately deferred to the Week 3 business case (`00-Assumptions-Log.md`, item #5), not because it's hard to answer but because it hasn't been decided yet. **Q1 status: answerable in hours for the Mobile fleet and in frequency for the other two tiers today; the dollar line completes once Week 3's cost-per-hour benchmark is locked.**

---

## Q2 (Tier 1 — Diagnose): Which one or two failure modes account for the majority of the loss (Pareto)?

| Failure mode | Primary-cause count (event-based, sums to 339) | True-occurrence count (how often it's really present) |
|---|---|---|
| HDF (Heat Dissipation) | 115 (33.9%) | 115 (33.9%) |
| PWF (Power Failure) | 91 (26.8%) | 95 (28.0%) |
| OSF (Overstrain) | 78 (23.0%) | **98 (28.9%)** |
| TWF (Tool Wear) | 46 (13.6%) | 46 (13.6%) |
| RNF (Random) | 0 (0.0%) | 1 (0.3%) |
| Unclassified | 9 (2.7%) | — |

All figures **[DATASET]**, both columns cross-verified against the raw sensor flag columns directly (not just against each other).

**Headline answer: HDF (overheating) is unambiguously the #1 cause of breakdowns either way, at roughly 34%.** But which mode is #2 depends on which column you read — and this is the direct, material consequence of the 10 Sept 2026 fix. Under the original (buggy) single-count Pareto, #2 looked like PWF (91 events, 26.8%), with OSF a distant #3 (78, 23.0%). Once the true-occurrence count is used — counting every real failure OSF was genuinely present in, not just the ones where it won a tie-break — **OSF overtakes PWF for second place (98 vs. 95)**. That's a ranking flip a reader would act on differently: a "target HDF and PWF first" recommendation is not the same recommendation as "target HDF and OSF first."

**Why this matters beyond the chart:** Q5 (the overstrain/torque-threshold question) is specifically about OSF. Confirming OSF as a genuine top-2 failure mode — not a third-place one — is direct evidence that Q5 deserves the priority the Master Plan already gives it (Tier 3, "Act & prevent"), rather than resting on an unverified assumption that overstrain matters.

**Recommended framing for the dashboard/business case:** present both columns, not one. The primary-cause count is still the right number for "how many discrete repair jobs were mainly caused by X" (staffing/scheduling questions). The true-occurrence count is the right number for "how much does this failure mode actually show up" (root-cause prioritization questions, including Q5). Collapsing to one number, as the original view did, answers a narrower question than the one Q2 actually asks.

---

## Q3 (Tier 2 — Explain): Which asset tier drives the highest failure rate — does it justify differentiated investment?

| Tier | Readings | Real failures | Failure rate |
|---|---|---|---|
| Ancillary (Low) | 6,000 | 235 | **3.92%** |
| Mobile fleet (Medium) | 2,997 | 83 | 2.77% |
| Fixed plant (High) | 1,003 | 21 | 2.09% |

All figures **[DATASET]**. This reproduces, from a completely independent query path, the exact inverse-to-criticality pattern first noticed on 24 August 2026 when the synthetic asset register was originally built — the same result, arrived at twice, by two different methods, weeks apart. That's a real reproducibility check, not a coincidence.

**Answer:** the tier that fails *most often* (Ancillary, low-criticality support equipment) is the opposite of the tier that matters *most* per failure (Fixed plant, high-criticality process equipment). The naive recommendation — "the highest-failure-rate tier needs the most investment" — would point maintenance resources at pumps and generators while under-resourcing crushers and mills. The more defensible recommendation, and the one this project should make: **differentiated investment by failure consequence, not failure frequency** — high-frequency/low-consequence preventive maintenance for Ancillary, condition-based/RCM-style monitoring for Fixed plant, with Mobile fleet (the only tier with both a real failure count and a real repair-time figure) as the tier best positioned for a full cost-of-downtime business case today.

---

## Q4 (Tier 2 — Explain): What proportion of failures are mechanically preventable versus inherently random?

Using the primary-cause (event-based, mutually exclusive) counts, since Q4 asks for a proportion of *events*, not a count of flag occurrences:

- **Preventable** (TWF + HDF + PWF + OSF combined): 46 + 115 + 91 + 78 = **330 of 339 confirmed failures (97.3%)** **[DATASET]**.
- **Random** (RNF as the confirmed cause of a real breakdown): **0 of 339 by the primary-cause rule (0.0%)** — but the true-occurrence view shows RNF genuinely present in **1 of the 339 confirmed failures (0.3%)**, co-occurring with a TWF flag on that same row. This single row is a disclosed, ambiguous edge case (10 Sept 2026 finding) — it is not forced into either category, since a mechanically-real tool-wear failure and a coincidentally-tripped random flag on the same event genuinely can't be told apart from this data alone.
- **Unclassified** (no mode flag set at all): 9 of 339 (2.7%) — real, confirmed breakdowns with no attributable mechanism captured by this dataset's taxonomy.

**Answer:** the overwhelming majority of *confirmed* breakdowns — roughly 97% — fall into a mechanically explainable category, and are therefore theoretically preventable through the kind of condition monitoring and threshold management Q5 and Q6 explore. Genuinely random failure, as this dataset defines it, essentially never shows up as an actual confirmed breakdown — RNF's documented ~0.1% design rate mostly manifests as the 18 rows already excluded earlier in this project (RNF triggered with no accompanying real failure — Scope log, 24 Aug 2026), which is itself worth stating in the same breath as this answer: **RNF behaves like background noise in the data, not like a real source of downtime.**

---

## Q5, Q6 (Tier 3 — Act & prevent): not answered in this document

Both questions ask about sensor-level relationships (a torque/tool-wear overstrain threshold for Q5; precursor patterns across all modes for Q6) that these three aggregate views cannot answer — they need row-level correlation and threshold analysis on the raw sensor columns (torque, tool wear, temperatures, rotational speed), not counts and rates. This is the next layer of EDA work, not a gap in what's been done so far.

One finding from this session carries forward directly into that work: Q2's confirmation that OSF is a genuine top-2 failure mode (98 of 339 confirmed failures, 28.9%) is direct support for treating Q5 as a priority question, not a speculative one. When that analysis is built, it must also carry the Instrumentation & Controls Engineer's calibration-provenance limitation forward (`Scope-Decisions-and-Limitations-Log.md`, 3 Sept 2026): a genuine precursor trend and a drifting or fouled sensor "look identical on a chart" at this site, so any Q5/Q6 finding needs that caveat attached, not presented as if it were free of instrumentation risk.

---

## Data provenance summary

Every number in this document traces to exactly one of: the dataset itself (`readings`/`failure_events` tables, `mining_reliability.db`), a cited external source (repair-time benchmarks, fully referenced in `05-Data-Dictionary.md` §3.1), or an explicitly labeled assumption (the hours = count × rate calculation). No figure in this document is presented without one of those three tags. The one dollar figure this document does not yet contain (Q1's cost line) is disclosed as pending, not silently omitted.
