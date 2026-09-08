# 05 — Data Dictionary: Kestrel Pit Maintenance Reliability Dataset

**Project:** Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability
**Prepared by:** Gagana Suresh, Business Analyst
**Status:** Complete for the merged dataset's 20 columns. Two external benchmark figures documented as labeled assumptions, not yet columns in any file — see Section 3. One aggregation decision flagged open — see Section 3.2.
**Date:** 8 September 2026
**Source documents:** `reskin_deal.py` (asset-dealing methodology) · `ai4i2020-kestrel.csv` (the merged file this dictionary describes) · `Scope-Decisions-and-Limitations-Log.md` (data-quality findings, benchmark sourcing, all decisions cited below) · `00AssumptionsLog.md` (Objective-level open items)

**A note on scope:** this dictionary describes `ai4i2020-kestrel.csv` — the file that already exists, already merged. It does not describe a database schema (that's Day 9) — it's the field-by-field spec that Day 9's cleaning/loading script and SQL queries get built against, so every downstream number can be traced back to exactly what it is and where it came from.

---

## 1. How to read this dictionary

Every field below is tagged one of three ways, same rule used everywhere else in this project:

- **DATASET** — comes straight from the real AI4I 2020 file, untouched in meaning.
- **LABELED ASSUMPTION** — invented for this project (the asset register), disclosed as such, never presented as if it were real client data.
- **CITED SOURCE** — an external, real, referenced figure applied on top of the dataset (used in Section 3 only — none of the 20 columns in the merged file itself carry this tag yet).

A field with no tag would be a defect in this document — flag it if you ever spot one.

---

## 2. Fields in `ai4i2020-kestrel.csv` (20 columns, in file order)

| # | Field | Type | Source | Definition |
|---|---|---|---|---|
| 1 | `UDI` | Integer | DATASET | AI4I's own unique row identifier, 1–10,000. Never re-used or recalculated — the stable key for tracing any row back to the original source file. |
| 2 | `Asset ID` | Text (code) | LABELED ASSUMPTION | Which of the 48 invented Kestrel Pit machines this row was dealt to. Assigned by `reskin_deal.py` — tier-constrained, fixed random seed (20260821), reproducible. This is the join key back to the asset register. |
| 3 | `Asset Name` | Text | LABELED ASSUMPTION | Plain-English machine name (e.g. "Primary Jaw Crusher"). Invented for the register; carried onto every row via the Asset ID join. |
| 4 | `Make / Model` | Text | LABELED ASSUMPTION | A real, plausible make/model (e.g. Caterpillar 793F) invented to make the register read as a credible mine-site fleet, not a genuine procurement record. |
| 5 | `Equipment Class` | Text (categorical) | LABELED ASSUMPTION | Finer-grained than Criticality Tier — e.g. "Mobile - hauling," "Fixed plant - crushing." This is the level the repair-time benchmarks in Section 3 are actually sourced against (mobile fleet / fixed plant / ancillary), not the H/M/L tier directly. |
| 6 | `Criticality Tier` | Text (H / M / L) | LABELED ASSUMPTION | Assigned by consequence-of-failure logic (fixed plant = High, single point of failure; mobile fleet = Medium; support/ancillary = Low) — not by machine size or cost. Must always equal the row's own `Type` value; a mismatch means the tier-matching rule was violated (see `reskin_deal.py`'s own built-in check, which must print 0). |
| 7 | `Location` | Text | LABELED ASSUMPTION | Invented site/circuit name (e.g. "Primary Crushing Circuit"). Background scaffolding only — never to be reported as a data-driven finding (e.g. "Circuit X fails more") since the location assignment carries no real signal, only the failure itself does. |
| 8 | `Product ID` | Text (code) | DATASET | AI4I's own identifier, e.g. `M14860` — the letter prefix duplicates `Type`. Kept for traceability back to the original file; not used analytically once `Type` and `Asset ID` exist. |
| 9 | `Type` | Text (L / M / H) | DATASET | AI4I's real quality/tier classification. This is the field the asset-dealing rule actually matched against — `Criticality Tier` is required to equal this on every row. |
| 10 | `Air temperature [K]` | Numeric | DATASET | Real AI4I sensor reading, Kelvin. |
| 11 | `Process temperature [K]` | Numeric | DATASET | Real AI4I sensor reading, Kelvin. |
| 12 | `Rotational speed [rpm]` | Numeric | DATASET | Real AI4I sensor reading. |
| 13 | `Torque [Nm]` | Numeric | DATASET | Real AI4I sensor reading — feeds the Q5 overstrain-threshold analysis together with Tool wear. |
| 14 | `Tool wear [min]` | Numeric | DATASET | Real AI4I sensor reading — cumulative tool wear at time of reading. |
| 15 | `Machine failure` | Binary (0/1) | DATASET | **The source-of-truth flag** for "did this asset go down." Use this — not the five mode flags below — for every downtime/cost total (Tier 1 metrics). See the source-of-truth rule under row 16. |
| 16 | `TWF` | Binary (0/1) | DATASET | Tool Wear Failure flag. **Use only to categorize a failure already confirmed by `Machine failure` = 1 — never to detect a failure.** See the three data-quality findings below; this rule is what resolves all three cleanly. |
| 17 | `HDF` | Binary (0/1) | DATASET | Heat Dissipation Failure flag. Same usage rule as TWF. |
| 18 | `PWF` | Binary (0/1) | DATASET | Power Failure flag. Same usage rule as TWF. |
| 19 | `OSF` | Binary (0/1) | DATASET | Overstrain Failure flag. Same usage rule as TWF — feeds Q5 directly. |
| 20 | `RNF` | Binary (0/1) | DATASET | Random Failure flag — AI4I's documented ~0.1%-probability independent flag. **Can be 1 while `Machine failure` = 0** (18 such rows exist) — this is expected generation behaviour, not a data error. Excluded from failure totals under the source-of-truth rule; see finding 2 below. |

### Data-quality rules that govern how rows 15–20 are actually used

These three findings were caught during the Week 2 Day 9 validation pass (logged in full in `Scope-Decisions-and-Limitations-Log.md`, 24 Aug 2026) and every SQL query built on this file must respect them:

1. **9 rows have `Machine failure = 1` but none of the five mode flags set.** Real failures — stay in every downtime/cost total — but bucketed as "Unclassified" in the failure-mode Pareto rather than forced into one of the five named modes.
2. **18 rows have `RNF = 1` but `Machine failure = 0`.** Expected per RNF's documented random/independent design. Excluded from failure counts and the Pareto entirely, per the source-of-truth rule (row 15).
3. **24 rows have more than one mode flag set simultaneously** (realistic cascading failures, not a defect). The failure-mode Pareto must count by failure event (row), never by summing the five flag columns independently — summing would double-count these 24 rows against the 339-row failure total.

---

## 3. External benchmark assumptions — not columns in this file

These figures answer "how many hours / how many dollars did a failure cost," which nothing in `ai4i2020-kestrel.csv` can answer on its own — AI4I has no repair-duration or repair-cost field at all (confirmed 24 Aug 2026). Each one below is either ready to use, permanently dropped, or deliberately still open — flagged honestly rather than forced into a false precision.

### 3.1 Repair time per failure (hours) — ready to use for 2 of 3 tiers

Applied by **Equipment Class**, not by individual asset — this is the granularity the real sources actually support.

| Equipment class (tier) | Assumed repair time | Source | Status |
|---|---|---|---|
| Mobile fleet (Criticality Tier M) | **~2.2 hours**, typical job (range extends to 45 hrs for complex jobs) | Two independent real mine-site studies converge near this midpoint: Rezaei Dashtaki, Jandaghi Jafari & Hoseinie (2025), *Scientific Reports* — Sarcheshmeh Copper Mine rope-shovel data (80% of repairs ≤130 min); and Jakkula, Mandela & Tripathi (2025) — Hindustan Zinc LHD data (machine-level MTTR 1.30–3.14 hrs, midpoint an independent arithmetic calculation, not stated by that source directly) | **Ready — but see caveat below** |
| Fixed plant (Criticality Tier H) | *No figure* | No defensible source found despite a widened mining → cement/aggregates search; the one partial candidate (Ball/rod mill) was independently verified and found to misrepresent its own source table — see the Scope log's 25 Aug entry | **Deliberately omitted — Option B, resolved 1 Sept 2026. Report by failure frequency only, never hours or cost, for this tier.** |
| Ancillary (Criticality Tier L) | *No figure* | Only 4 of the tier's 29 assets (the water/dewatering pumps) genuinely resemble what the Idaho National Laboratory source measured (pump/valve/motor, municipal water/wastewater equipment) — the other 25 (vehicles, graders, dozers, generators, compressors, etc.) don't. | **Deliberately omitted — resolved 8 Sept 2026. Report by failure frequency only, same rule as Fixed plant.** |

**Caveat on the Mobile-fleet figure:** blending a rope-shovel (excavator-class) study with an LHD (loader-class) study into one "~2.2 hours" isn't a single clean citation — it's a judgment call that two different real sources happen to land near the same number. Worth stating exactly that way if asked, rather than presenting 2.2 as if one paper said so directly.

### 3.2 Decision, resolved 8 September 2026 — Ancillary tier gets no repair-time figure

The Ancillary tier (29 assets: graders, dozers, water carts, pumps, generators, compressors, feeders, service trucks, light vehicles) is far broader than "pumps, valves, and motors" — the only equipment the INL source actually covers, and only 4 of the 29 assets (the water/dewatering pumps) genuinely match it. Three options were weighed: blend all three INL figures into one average and apply it to all 29 assets; apply the figures only to the machines that plausibly resemble pumps/motors and leave the rest uncovered; or drop a repair-time figure for the whole tier, same as Fixed plant.

**Decision: the third option.** No repair-time figure for any Ancillary-tier asset — the whole tier reports by failure frequency only, exactly like Fixed plant. Chosen for consistency: Fixed plant already established the rule "don't force a benchmark onto equipment the source didn't actually measure," and applying a different, more permissive standard here would be an inconsistency a skeptical reviewer would catch immediately. It also avoids the harder-to-defend middle option, which would require justifying machine-by-machine why some Ancillary assets "count" as pump/motor-like and others don't.

**Correction this surfaces, logged in `Scope-Decisions-and-Limitations-Log.md`:** the 1 September 2026 entry locking the Fixed-plant Option B decision stated that "real, sourced dollar figures still cover 43 of the fleet's 48 assets" — that assumed the Ancillary tier's proxy figures were usable across all 29 of its assets. With this decision, real repair-time coverage is actually just the Mobile fleet's 14 assets. See the Scope log's correction note for the full record.

### 3.3 Repair cost per failure (labor + parts) — permanently dropped, not a gap to revisit

Searched extensively (SMRP, OREDA, Deloitte, IMechE, MaintainX, academic life-cycle-cost papers, OEM handbooks) — genuinely not found anywhere, mining or general industrial. **Decision, 25 Aug 2026: dropped from the business case entirely, all tiers.** Not used in any Day 9 query. The Financial Controller interview's refinement (3 Sept 2026) already reframed this correctly: not "unknowable," just unreachable from this project's chosen dataset — a real ERP would hold it.

### 3.4 Downtime cost per hour (lost production value) — real candidates exist, decision deliberately deferred

Not the same figure as repair cost above. Two real, cited candidates surfaced during the August sourcing run — a 2024 industry survey (~US$25,000/hr, general industrial) and a 2023 UK/Ireland survey (~£5,000/hr) — neither mining-specific. **This is `00AssumptionsLog.md` item #5, explicitly still open and blocking Objective O1.** Not a "couldn't find anything" gap like repair cost — a "found real candidates, deliberately deferred the actual choice to the Week 3 business case" item, where picking and justifying a rate gets the fuller treatment it needs. Not used in any Day 9 query.

---

## 4. One thing this dataset does *not* need to model

The BRD's PP2 finding (the real-world CMMS's messy ~40-option cause-code dropdown) is a process/UI problem in the *real* maintenance workflow this project is redesigning — it is not a missing field in this analytical dataset. AI4I's own five-flag taxonomy (TWF/HDF/PWF/OSF/RNF) already serves as this dataset's failure-mode classification and needs no equivalent "cause code" column added here. The proposed FR-14 (cause-code taxonomy redesign) stays a requirements-level item for the CMMS, tracked in `04-Process-Maps.md` §10 and the Scope-Decisions log — it does not block or change anything in this dictionary.

---

## 5. What feeds Day 9

Day 9's SQL queries can now be built against a fully specified field list: `Machine failure` + the five mode flags (with the three usage rules in Section 2 respected) for the failure-mode Pareto and failure-rate-by-tier queries; `Criticality Tier` / `Equipment Class` for tier segmentation; and the Section 3.1 repair-time figures — for Mobile fleet immediately, for Ancillary once 3.2 is decided, and never for Fixed plant, by design. No query should reference a repair-cost or downtime-cost-per-hour figure yet — neither is ready (3.3 is closed permanently; 3.4 is open on purpose).
