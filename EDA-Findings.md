# Exploratory Data Analysis Findings

**Owner:** Gagana Suresh
**Status:** Complete for all six locked business questions, Q1–Q6. Q5 and Q6 (Tier 3, below) were added 1 October 2026, closing a real gap `10-Traceability-Matrix.xlsx` surfaced that day (Gap G5): `07-User-Stories.md` and `08-Test-Cases.md` had both marked the Q5/Q6-dependent stories and test cases Ready/Executable while this document still said the underlying analysis hadn't been performed. Rather than relabel those statuses down, the analysis was run for real.
**Last updated:** 1 October 2026
**Renamed 24 September 2026:** from `06-EDA-Findings.md` to remove a numbering collision — the Master Plan's repo structure (Section 5.1) reserves "06" exclusively for `06-Business-Case.xlsx`, which this document was never meant to compete with. This document was never assigned a number in that structure; it now follows the same unnumbered convention already used for the interview transcripts, the Scope-Decisions-and-Limitations-Log, and Interview-Prep-QA. No content below this line has changed. See the Scope-Decisions-and-Limitations-Log entry of 24 Sept 2026 for the full reasoning.

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

## Q5 (Tier 3 — Act & prevent): Is there a torque/tool-wear threshold that predicts overstrain (OSF) risk clearly enough to justify a proactive replacement policy?

**Pre-agreed statistical bar (fixed before the result below, per Charter O5's own requirement — a bare correlation without a pre-agreed bar does not meet this criterion):** a threshold rule is considered predictive enough to justify a proactive-replacement-policy recommendation if it achieves **at least 90% precision AND at least 90% recall** against OSF, tested against the full dataset rather than fit to it. Deliberately strict: a policy that misses real failures or drowns the maintenance team in false alarms is operationally worse than no policy.

**Rule tested:** `Tool wear [min] × Torque [Nm]` exceeds a tier-specific limit — 11,000 minNm for Low-tier (Ancillary), 12,000 for Medium-tier (Mobile fleet), 13,000 for High-tier (Fixed plant) **[CITED SOURCE: Matzka, S. (2020). "Explainable Artificial Intelligence for Predictive Maintenance Applications." 3rd International Conference on Artificial Intelligence for Industries (AI4I 2020), Irvine, CA, pp. 69–74. IEEE. doi.org/10.1109/AI4I49448.2020.00023 — the dataset's own published generation rule, not a cutoff mined from the data by this analysis].**

**Result, tested against all 10,000 rows [DATASET]:** precision = **100%**, recall = **100%** (98 true positives, 0 false positives, 0 false negatives). This isn't a strong correlation — it's an exact, deterministic relationship: every single row that crosses the tier-specific limit has OSF = 1, and no row below it does. The bar is cleared by a wide margin, and because the threshold came from an external, cited source rather than being tuned against this data to get a good-looking number, this isn't the "bare correlation" Charter O5 warns against — it's a confirmatory validation of a known physical rule, which is stronger evidence, not weaker.

**Go/No-Go recommendation: GO.** A threshold-based monitoring rule on `Tool wear × Torque` is recommended as a proactive-replacement trigger, with one important refinement below.

**The refinement a hiring-manager-credible answer needs, not just "yes there's a threshold":** the hard limit above is, by construction, the point of failure itself — flagging only once it's crossed isn't "proactive," it's a slightly-earlier reactive alarm. The more useful policy question is how much *buffer* below the hard limit to set an earlier warning line. Scanning candidate buffers against the current dataset **[DATASET]**:

| Buffer (% of tier hard limit) | Non-failed rows currently in the zone | By tier (L / M / H) |
|---|---|---|
| ≥80% | 486 (4.9% of all non-failed rows) | 376 / 96 / 14 |
| ≥85% | 313 (3.2%) | 244 / 62 / 7 |
| **≥90% (recommended starting point)** | **140 (1.4%)** | **111 / 27 / 2** |
| ≥95% | 57 (0.6%) | 48 / 9 / 0 |

A 90% buffer currently flags 1.4% of non-failed readings as "approaching the limit" — a manageable alert volume relative to the 98 confirmed OSF events in the same dataset, and a reasonable starting point for a real pilot. **Recommend starting at the 90% buffer and tuning it with the Reliability Engineer once real site data is available** (same calibration discipline already required for FR-07's amber-escalation threshold, BRD §17 Action 4) — this is a sensible starting policy, not a number to lock in blind.

**Limitation that must travel with this finding everywhere it's quoted:** AI4I is cross-sectional, not longitudinal — each row is one independent process snapshot, not a time-ordered sequence of readings from the same physical tool as it wears. This analysis proves the *threshold relationship* is real and exact, and gives a defensible *alert-volume* estimate for a buffer-based policy — it does **not** prove how much real advance warning time (hours, shifts, tonnes) a 90% buffer would actually deliver on a real asset, since there's no "this specific tool's torque×wear climbing over three weeks" trajectory in this dataset to measure that against. Confirming real lead time requires genuine longitudinal, per-asset sensor logging at a real site — exactly the production capability FR-01 (asset history) and FR-07/FR-08 (escalation + calibration) are recommended to build, not something this dataset can validate on its own.

---

## Q6 (Tier 3 — Act & prevent): Which failure modes show detectable sensor precursor patterns that could enable early warning?

**Classification rule (fixed before testing, mirroring Q5's bar):** a failure mode is **Detectable — deterministic** if its documented mechanism variable(s) achieve ≥90% precision AND ≥90% recall; **Detectable — probabilistic** if the mechanism variable is clearly necessary (recall ≥90%) but not sufficient to guarantee failure on its own (so precision is inherently capped by the mode's own design, not by weak analysis); **Not detectable** if no sensor variable shows a meaningful association beyond chance; **Inconclusive** if the sample is too small to trust either way.

| Failure mode | Mechanism tested | Result | Classification |
|---|---|---|---|
| HDF (Heat Dissipation) | `Process temp − Air temp < 8.6K` AND `rotational speed < 1380 rpm` **[CITED SOURCE: Matzka 2020]** | Precision 100%, recall 100% (115/115) **[DATASET]** | **Detectable — deterministic** |
| PWF (Power Failure) | `Power = Torque × rotational speed (rad/s)`, failure if `<3500W` or `>9000W` **[CITED SOURCE: Matzka 2020]** | Precision 100%, recall 100% (95/95) **[DATASET]** | **Detectable — deterministic** |
| OSF (Overstrain) | See Q5 above | Precision 100%, recall 100% (98/98) **[DATASET]** | **Detectable — deterministic** |
| TWF (Tool Wear) | `Tool wear` in the documented 200–240 min risk window **[CITED SOURCE: Matzka 2020 — "tool replaced 69 times, fails 51 times," a random draw within the window]** | Of 46 true TWF occurrences, 43 (93.5%) fall inside the window — strong necessary condition — but only 43 of 790 in-window rows (5.4%) actually fail, since the dataset's own design makes the exact failure point a random draw within the window, not a further threshold **[DATASET]** | **Detectable — probabilistic.** The window is a genuine, usable early-warning signal ("inspect once tool wear passes 200 min"), but precision is capped by design, not by analysis weakness — disclose this distinction rather than let a 5.4% precision figure read as a failed finding. |
| RNF (Random) | Mean sensor values compared, failure vs. non-failure rows (Air/Process temp, rpm, Torque, Tool wear) **[DATASET]** | No sensor variable shows a meaningful separation (e.g., mean torque 43.7 vs. 40.0, mean rpm 1485 vs. 1539 — small, n=19, no consistent direction across variables) | **Not detectable** — consistent with RNF's own documented design (a flat 0.1% chance of failure regardless of process parameters) and with this project's earlier finding that RNF "behaves like background noise in the data" (Q4, above). |

**Answer:** four of the five documented failure modes (HDF, PWF, OSF, and — with the probabilistic caveat — TWF) show a detectable sensor precursor pattern; RNF correctly shows none, which is itself the expected and correct result for a mode defined as pure chance. This directly answers Charter O6's requirement to classify each mode as detectable/not detectable/inconclusive.

**The same cross-sectional limitation from Q5 applies here, stated once for all five modes rather than repeated five times:** every "Detectable" result above means the mechanism variable reliably distinguishes a failure reading from a non-failure reading *at the moment that reading was taken* — a necessary precondition for any real early-warning system. It is not, on its own, evidence of genuine advance lead time, since AI4I provides no per-asset time series to measure how long before failure a reading would have crossed into the warning zone. Per Charter O6's own scope boundary, this is a diagnostic finding only, not a built or validated predictive model — and, per the Instrumentation & Controls Engineer's calibration-provenance limitation (`Scope-Decisions-and-Limitations-Log.md`, 3 Sept 2026), a real deployment of any of these four thresholds would still need calibration-date tracking (FR-08) before trusting that a reading in the warning zone reflects genuine wear rather than sensor drift.

---

## Data provenance summary

Every number in this document traces to exactly one of: the dataset itself (`readings`/`failure_events` tables, `mining_reliability.db`, or — for Q5/Q6's row-level sensor analysis — the raw AI4I 2020 CSV directly), a cited external source (the Q1 repair-time benchmarks, fully referenced in `05-Data-Dictionary.md` §3.1; the Q5/Q6 failure-mode generation rules, Matzka 2020, full citation above), or an explicitly labeled assumption (the hours = count × rate calculation). No figure in this document is presented without one of those three tags. The one dollar figure this document does not yet contain (Q1's cost line) is disclosed as pending, not silently omitted.

**Methodology note for Q5/Q6 (added 1 October 2026):** unlike Q1–Q4, which were queried from `mining_reliability.db`'s pre-built views, Q5 and Q6 required row-level statistical testing (precision/recall against a threshold rule, mean comparisons) that those views don't expose, so this analysis was run directly against the canonical AI4I 2020 CSV in a fresh calculation. Before running it, the exact row counts (10,000 total; 6,000/2,997/1,003 by tier; 339 confirmed failures split 235/83/21; true-occurrence counts of 115/95/98/46/19 for HDF/PWF/OSF/TWF/RNF) were cross-checked against this document's own Q1–Q4 figures and matched exactly — confirming this is the same canonical dataset instance underlying every other number in this project, not a different download that happens to look similar.
