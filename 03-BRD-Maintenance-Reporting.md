# 03 — Business Requirements Document: Maintenance Reliability Reporting

**Project:** Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability (mining fleet + fixed-plant maintenance function)
**Prepared by:** Gagana Suresh, Business Analyst
**Version:** v2 — revised following an adversarial red-team review (Master Plan, Week 1, Day 5). See Appendix A for the full critique and Appendix B for the change log.
**Status:** DRAFT — pending sign-off (four outstanding validation actions before final approval — see Section 17)
**Date:** 4 September 2026
**Data note:** This engagement is a simulated portfolio project. All interviews are role-played personas standing in for unavailable real stakeholders (flagged per the project's data-integrity rule), and the operational dataset is a real, published industrial dataset (AI4I 2020) re-skinned onto a synthetic mining asset register — not real company data. See `Scope-Decisions-and-Limitations-Log.md` for the full data-lineage record, Section 2.1 for what "independent corroboration" does and doesn't mean in a simulated engagement, and Section 13 for what all of this means for every figure below.

**Related documents:** `00-Master-Plan.md` · `01-Project-Charter.md` (v5) · `02-Stakeholder-Register.md` · `Scope-Decisions-and-Limitations-Log.md` · six interview transcripts (`Interview-Transcript-*.md`)

## Revision History

| Version | Date | Change |
|---|---|---|
| v1 | 3 Sept 2026 | Initial draft, synthesizing all six interview transcripts and the Scope-Decisions-and-Limitations-Log |
| v2 | 4 Sept 2026 | Revised following a structured adversarial red-team review (30 findings across 6 categories). Fixes an FR-06 Must/Should self-contradiction; adds three missing functional requirements (FR-11/12/13) so every locked business requirement (BR-01–BR-06) has a corresponding FR; corrects Must/Should mislabeling against the document's own stated rule; rewrites Section 15's acceptance criteria to be individually testable; adds a methodology note (Section 2.1) on the actual strength of "independent corroboration" claims between role-played personas; adds four new limitations (no frontline data-entry, CMMS-owner, or capital-planning stakeholder was interviewed; small-sample precision); adds two new risks; corrects a source-count contradiction on FR-10; moves AI-process/methodology narration out of the client-facing body and into Appendix C, mirroring the pattern already used in `01-Project-Charter.md` Appendix C. See Appendix B for the full finding-by-finding change log. |

---

## 1. Executive Summary

The site's maintenance function cannot currently tell leadership, with any defensible confidence, which assets, failure modes, or asset classes are driving unplanned production loss — or what it is costing. Six stakeholders, interviewed across four full sessions and two short targeted conversations, each described having personally signed, defended, or quietly distrusted a downtime or cost figure they could not fully stand behind. Three of those stakeholders, working from different incentives and interviewed in separate, isolated sessions, each asked for a version of the same underlying artifact: an asset-level, time-windowed, cumulative view of failure and cost. Section 2.1 explains plainly what that convergence does and does not prove in a simulated engagement — it is treated throughout this document as a real, useful signal, not as courtroom-grade independent proof.

This BRD defines the requirements for a maintenance reliability reporting capability that answers six locked business requirements (Section 7) using a re-skinned real-world failure dataset, a small set of externally sourced and disclosed cost/time benchmarks, and — where the underlying data genuinely does not support a trustworthy dollar figure — an honest, named gap rather than a fabricated one. The most consistently requested requirement is a per-asset cumulative failure/cost rollup (Section 8, FR-01). The most consistent constraint is that four of five fixed-plant asset types have no trustworthy repair-time or repair-cost data today — a real operational gap, not a project shortcoming, and one this BRD recommends fixing at the process level (Section 8, FR-06), not just reporting around.

This document is scoped to the CMMS reporting enhancement and the underlying data/process requirements that support it. It does not scope the dashboard's visual design, the SQL/data-model implementation, or the business case's financial model — those follow in Weeks 2–3 per the Master Plan and reference this document as their source of truth. **Before this document proceeds to final sign-off, four validation actions remain open — see Section 17.** They exist because this discovery phase, like any six-interview discovery phase on a real site, did not reach every stakeholder who should weigh in before build (frontline tradespeople, the CMMS/IT system owner, and capital planning); this is disclosed here rather than glossed over.

---

## 2. Business Context & Problem Statement

Unplanned equipment breakdowns are absorbing production time and maintenance spend that the site cannot currently quantify, attribute, or defend with confidence. Four full stakeholder interviews each produced a specific, real incident where the interviewee had to sign or defend a downtime/cost figure they knew was soft:

- The **Maintenance Manager** built the monthly downtime-hours slide for a GM-level ops review "at nine o'clock the night before," by eyeballing CMMS descriptions to guess which were genuinely unplanned, and rates his own confidence in the resulting number at "plus or minus twenty, twenty-five percent" (Interview-Transcript-Maintenance-Manager.md, Q3).
- The **Reliability Engineer** routinely completes technically sound root-cause analyses that are shelved because he has no downtime-cost figure to compete with production's ready-made tonnes-times-price argument in the room — "I'm one bloke with a spreadsheet and a hunch" (Interview-Transcript-Reliability-Engineer.md, Q3, Q8).
- The **Mining/Operations Manager** has personally written the line "loss of digger availability contributed to the shortfall" into a board pack without a number behind it, because no clean way exists to tie a specific breakdown to a specific tonnage miss (Interview-Transcript-Operations-Manager.md).
- The **Financial Controller** caught a primary-crusher work order that overstated unplanned downtime by roughly five hours because a planned inspection had been bundled into the same work order as an unplanned failure — and was explicit that she only caught it because the dollar impact was large enough to be visually obvious in a spreadsheet, meaning smaller versions of the same error are almost certainly sitting undetected in every report she has signed (Interview-Transcript-Financial-Controller.md, Q2).

Two further findings sharpen why this matters beyond data hygiene. First, two senior stakeholders — the Mining/Operations Manager and the Maintenance Superintendent, Fixed Plant — each, unprompted, named the same cognitive bias in their own gut-feel estimates of their worst-performing asset: dramatic, disruptive failures are memorable, while frequent, minor ones are not, so instinct alone systematically over-weights the wrong things. Second, the Maintenance Superintendent, Fixed Plant named a live, unresolved disagreement with the Reliability Engineer — he believes the primary jaw crusher is the site's worst offender by event count; the Reliability Engineer believes it is the mill by total downtime hours — and said plainly: "we've never sat down and actually looked at it side by side with real numbers... everyone's got their own asset they reckon is the worst and nobody's got the data to settle it" (Interview-Transcript-Maintenance-Superintendent-Fixed-Plant.md, Q5). This document does not claim its Pareto/tier reporting (BR-02, FR-02) *settles* that disagreement — count and downtime-hours are two different, both-valid metrics, and FR-02 is required to display both side by side rather than declare one authoritative. It is, however, the clearest illustration on record of why the two metrics need to sit next to each other in the first place.

**Why this keeps happening — two distinct root causes, not one:** discovery surfaced a data-quality explanation (inconsistent CMMS entry, two disagreeing downtime clocks, a ~40-option cause-code dropdown where roughly half the options do not fit what actually happened, and repair durations reconstructed from memory rather than timed live — Interview-Transcript-Maintenance-Superintendent-Fixed-Plant.md, Q2, Q4) and a separate, structural process/incentive explanation the Financial Controller was positioned to see: quick patch repairs are typically opex and can be approved within her own delegated authority in days, while proper root-cause fixes are often capex and must queue behind the site's capital round for months — so a meaningful share of "production pressure keeps winning" may be an approval-pathway effect, not purely an argument-quality one (Interview-Transcript-Financial-Controller.md, Q8). **This second explanation is reported by one stakeholder only and has not been corroborated by anyone who actually owns capital planning or procurement — see Section 13.10.** It is carried forward as a credible, well-reasoned hypothesis worth testing in the business case, not as an established structural fact. Better reporting alone addresses the data-quality cause. It does not, by itself, address the approval-pathway cause — see Risk 1, Section 14.

### 2.1 A note on "independent corroboration" in a simulated engagement — read this before the rest of the document

This document repeatedly notes when more than one interviewed stakeholder asked for the same thing without being shown each other's answers — for example, three personas independently describing a version of the asset-level rollup in FR-01. That description of the *process* is accurate: each interview was conducted in a separate, isolated conversation, and no persona was shown another persona's transcript before answering. **What this does not establish is genuine independence in the way that phrase implies for real human stakeholders.** All six personas were generated by the same underlying process, working from the same project brief and the same general mining-industry knowledge. Structural consistency between them is expected even without any content leaking across sessions — six well-informed people asked similar questions about a similar operational problem will often converge on similar answers, real or simulated. This document therefore treats multi-stakeholder convergence as a genuinely useful design signal (it tells you which requirements are *plausible* and *low-risk to prioritize*), not as statistical proof that a real Maintenance Manager, Operations Manager, and Financial Controller would independently ask for the same thing at a real site. Wherever this document uses language like "requested by N stakeholders," that is a factual count of interview sources, stated plainly, without the inflated language of "independent proof" this document's v1 draft sometimes used. A full validation of any FR this reasoning supports still requires the four actions in Section 17, including engagement with stakeholder groups no persona in this discovery phase represents.

---

## 3. Business Objectives

This initiative exists to give the maintenance function and its cross-functional stakeholders a shared, trustworthy, asset-level view of unplanned downtime — replacing gut-feel, memory, and disputed one-off numbers with a reporting capability that can be defended in a GM-level meeting or a capital-approval request. Success is defined operationally, not just technically, and traces directly to `01-Project-Charter.md`'s per-objective success criteria (O0–O6), each of which names an accountable reviewer and, where judgement is involved, a threshold agreed in advance rather than decided after seeing the result. Two stakeholder-level standards sharpen what "successful" means day to day:

- The **Maintenance Manager's** own four-part bar (Interview-Transcript-Maintenance-Manager.md, Q10): the underlying data must be trustworthy, not an automated version of today's inconsistent entries; it must not add data-entry burden to tradespeople; every figure must be traceable and defensible; and it must be used by Operations, not live only in Maintenance's own report.
- The **Financial Controller's** own six-part standard (Interview-Transcript-Financial-Controller.md, Q4): traceable to source work orders; a documented, dated, and consistent methodology; the planned/unplanned split trustworthy at the point of entry; broken down by asset and cause; honest about which figures are hard data versus estimate; and reconcilable with what she already owns in the finance system.

Section 15 restates the union of both standards as formal, individually testable acceptance criteria.

---

## 4. Scope

### 4.1 In scope

- Six locked business requirements (Section 7, BR-01 through BR-06), answered using the re-skinned AI4I 2020 dataset, the synthetic mining asset register, and externally sourced, cited, and disclosed cost/time benchmarks where AI4I itself cannot supply a figure.
- Functional and data requirements for a CMMS reporting enhancement that supports those six requirements (Section 8), including a dedicated functional requirement for every one of BR-01 through BR-06 (Section 8, see the traceability note at the top of that section).
- Requirements for how the current CMMS work-order lifecycle should change to make future data trustworthy (planned/unplanned separation at point of entry, corrected-duration capture, calibration-date logging) — process requirements, not just reporting requirements, and explicitly flagged as unvalidated against real CMMS platform capability pending Section 17's Action 2.
- Non-functional requirements governing traceability, auditability, and cross-team usability (Section 9).
- Explicit documentation of every data gap and scope boundary this analysis is subject to (Section 13), so the deliverable is defensible on its own terms rather than silently incomplete.

### 4.2 Out of scope

- Root causes of production loss unrelated to equipment failure — blast delays, weather, haul-road closures, rostering/crew shortages. This analysis quantifies the **equipment-attributable share** of downtime only; see the limitation in Section 13.1, raised unprompted by the Mining/Operations Manager, who was explicit that treating every tonnes miss as a maintenance issue would cause him to misread weeks where the real story was something else.
- Sub-threshold stoppages (roughly under 15 minutes) that never generate a CMMS work order today — see Section 13.2. This is a structural blind spot of any work-order-based analysis, not a gap this project's data cleaning can close.
- Repair cost (labour + parts) as a business-case input. Dropped for this project specifically because no publicly verifiable external benchmark exists and AI4I has no cost fields — not because repair cost is unknowable at a real site. See Section 10.4 and the Financial Controller's correction of this framing (Interview-Transcript-Financial-Controller.md, Q5).
- A capital-replacement business case, depreciation/write-off analysis, or OEM mobile-fleet maintenance-contract cost modelling — flagged by the Financial Controller as real considerations for a future phase, not this engagement (Interview-Transcript-Financial-Controller.md, Q11).
- The dashboard's visual/UX design, the SQL data model implementation, and the financial business-case model itself — each is a separate Week 2/3 deliverable that will trace back to this document, not duplicate it.
- The optional ML proof-of-concept module (Master Plan, Section 2) — out of scope for this BRD entirely; addressed, if built at all, only after every core deliverable is complete.
- A decision on whether "Operations Superintendent" and "Mining/Operations Manager" name the same individual — genuinely open; see `02-Stakeholder-Register.md` Section 4 and `01-Project-Charter.md` Appendix G. Does not block this document's approval (Section 16).

---

## 5. Stakeholders

Full stakeholder analysis, tiering, and methodology are maintained in `02-Stakeholder-Register.md` and are not duplicated here. In summary: governance follows a split sponsor model resolved 1 September 2026 and title-clarified 3–4 September 2026 (`01-Project-Charter.md` v5) — the **Operations Superintendent holds the Project Sponsor role** (commissions the engagement, final go/no-go authority; represented in the register by the Mining/Operations Manager, stakeholder #7), and the **Maintenance Manager holds the Accountable Business Owner role** (owns the budget and the KPI this initiative is built to move; day-to-day sign-off on this BRD and downstream artifacts). The dividing line is explicit: the Sponsor approves whether the work continues and within what boundary; the Business Owner approves what the work says. Section 16 restates the approval chain for this specific document.

Six stakeholders were interviewed directly to inform this BRD (four full interviews, two short targeted conversations): Maintenance Manager, Reliability Engineer, Mining/Operations Manager, Financial Controller, Maintenance Superintendent – Fixed Plant, and Instrumentation & Controls Engineer. The rationale for who was interviewed and who was deliberately not is documented in the Scope-Decisions-and-Limitations-Log's "Interview list" entry. **Three stakeholder groups this discovery phase did not reach at all — frontline tradespeople, the CMMS/IT system owner, and capital planning/procurement — are named explicitly in Section 13.8–13.10 as open validation gaps, not silently absorbed into the register's existing tiers.**

---

## 6. Current State (As-Is) Summary

A full as-is process map is a separate Week 2 deliverable (`04-Process-Maps.md`); this section summarizes the specific process and data breakdowns discovery surfaced, each traced to source, as direct input to that mapping exercise and to the functional requirements in Section 8.

| # | As-is pain point | Evidence |
|---|---|---|
| 1 | Downtime is recorded by two independent, unsynchronized clocks — production's shift-stoppage log and maintenance's work-order timestamps — which routinely disagree, with neither treated as authoritative | Maintenance Superintendent – Fixed Plant, Q2; corroborated structurally by the Financial Controller's crusher work-order incident, Q2 |
| 2 | Cause-code selection in the CMMS uses a ~40-option dropdown where roughly half the options do not fit what actually happened, so entries default to "other" with the real story, if captured at all, left in free text | Maintenance Superintendent – Fixed Plant, Q2 |
| 3 | Repair duration is not timed live — tradespeople reconstruct start/finish times from memory, sometimes days after the job, and a work order left open while a crew is pulled onto a higher-priority failure silently absorbs that dead time into the recorded duration | Maintenance Superintendent – Fixed Plant, Q4 — the most specific, mechanism-level finding from discovery |
| 4 | The CMMS is work-order- and asset-centric, not failure-mode-centric — there is no way to query "which failure mode is costing the most repeat hours across the fleet" without a person manually reinterpreting inconsistent free-text entries | Reliability Engineer, Q2 |
| 5 | Root-cause analyses are technically sound but frequently do not convert into scheduled corrective action — the case competes against an immediate production need and loses, until the failure repeats | Reliability Engineer, Q3–Q4; corroborated independently by the Maintenance Manager's alternator-mount example and the Reliability Engineer's own mill-gearbox-contamination example (two different incidents, not one retold) |
| 6 | Condition-monitoring "amber" (caution) readings have no escalation mechanism — red alarms get actioned, amber readings roll over month to month unless someone manually reviews historical reports; the Reliability Engineer estimates the programs catch "maybe a third" of what they could | Reliability Engineer, Q7 |
| 7 | No calibration-provenance tracking exists against sensor ID, so a genuine early-warning sensor trend and a drifting/fouled sensor "look identical on a chart" — confirmed with two concrete incidents (crusher vibration attributed to dust buildup, not bearing wear; a weeks-long temperature trend that was a fouled RTD) | Instrumentation & Controls Engineer, Q4–Q5 |
| 8 | No mechanism separates operator-influenced equipment damage from genuine wear-and-tear/design failure — all of it is currently absorbed into maintenance's reliability numbers by default | Maintenance Manager, Q11 (raised unprompted) |
| 9 | The repeat-cost of chronic under-investment in a single asset is invisible even to Finance — five or six separate patch-repair work orders on the same asset, each individually under approval-scrutiny thresholds, are never rolled up against that asset unless someone deliberately goes looking | Financial Controller, Q8 |
| 10 | Quick patch repairs (opex, approved within the Financial Controller's own delegated authority) and proper root-cause fixes (often capex, queued behind the site's capital round) sit in structurally different approval pathways — a possible driver of "production wins" independent of data quality; single-sourced, see Section 13.10 | Financial Controller, Q8 |
| 11 | Sub-threshold stoppages (roughly under 15 minutes) never generate a work order at all and are invisible to any CMMS-based analysis | Reliability Engineer, Q11 (raised unprompted) |

---

## 7. Business Requirements

The six business questions locked in `Scope-Decisions-and-Limitations-Log.md` (1 September 2026) are restated here as formal business requirements, organized on the same Diagnose → Explain → Act narrative funnel, with the data-treatment caveat for each stated plainly rather than left implicit. **Every BR below has at least one dedicated functional requirement in Section 8 — see the traceability table at the top of that section.**

**Tier 1 — Diagnose**

**BR-01.** The reporting capability must quantify how much production time and cost is being lost to unplanned breakdowns. *Data treatment: fully quantified for Medium- and Low-tier (mobile fleet and ancillary) assets, using AI4I-derived failure counts applied against externally sourced, cited repair-time and downtime-cost benchmarks, with the confidence mechanism defined in FR-04 (a visible dataset-derived / cited-source / labeled-assumption tag, plus a source-stated error range where the benchmark's own publication provides one, or an explicit qualitative confidence tier — High/Medium/Low — where it does not). High-tier (fixed plant) assets are reported by failure frequency only — see BR-06 and Section 10.3 (Option B).*

**BR-02.** The reporting capability must rank failure modes by their share of total downtime/cost loss (a Pareto analysis), directly speaking to the live, unresolved disagreement documented in Section 2 between the Maintenance Superintendent, Fixed Plant and the Reliability Engineer. *Data treatment: failure-mode counts are fully data-derived from AI4I; a dollar-weighted version of the Pareto carries the same Medium/Low-tier caveat as BR-01. Per `01-Project-Charter.md` Objective O2's success criterion, success is the rigor and completeness of the ranking and its methodology (including the multi-flag-row handling rule, Section 10.1) — not any predetermined "one or two modes account for the majority" threshold; no such threshold is fixed in advance, and none should be inferred from this requirement's wording.*

**Tier 2 — Explain**

**BR-03.** The reporting capability must display, side by side, the failure rate and (within BR-01's cost scoping) cost for each asset tier (AI4I's Low/Medium/High classification, mapped to the synthetic asset register's ancillary/mobile-fleet/fixed-plant tiers). *Data treatment: failure rate is fully answerable and data-derived for all three tiers. A genuine, non-obvious finding from the tier-mapping exercise itself: failure rate runs inverse to criticality (High-tier roughly 2%, Medium roughly 3%, Low roughly 4% — rounded; see Section 13.11 on why more precision than this overstates what a 5/14/29-asset synthetic register actually supports) — so the eventual answer is not the simple "critical assets fail most, fund them more," but the more nuanced "low-criticality assets fail more often, but each high-criticality failure costs far more." **Whether this evidence justifies differentiated maintenance investment is a business-case recommendation, evaluated against the materiality threshold `01-Project-Charter.md` Objective O3 requires be agreed before the analysis is run — it is a judgement made in the business case (Week 3), not a system behavior this reporting capability itself performs. This BRD's job is to display the figures the recommendation is based on (FR-03); it does not claim the system will decide the investment question.***

**BR-04.** The reporting capability must show what proportion of failures are mechanically preventable versus inherently random, using AI4I's own distinction between its four explainable failure modes and its documented random-failure category (RNF). *Data treatment: fully answerable, directly from the dataset's own taxonomy — not a labeled assumption. See FR-11.*

**Tier 3 — Act & Prevent**

**BR-05.** The reporting capability must identify whether a torque/tool-wear threshold predicts overstrain risk clearly enough to justify a proactive replacement policy. *Data treatment: fully answerable from AI4I's real sensor columns, tested against the pre-agreed statistical bar `01-Project-Charter.md` Objective O5 requires be fixed before the analysis runs. This demonstrates a method on this project's dataset — it is not a claim that the site's real fleet is currently instrumented to support the same analysis in production; see the calibration-provenance limitation in Section 13.3 and FR-12.*

**BR-06.** The reporting capability must identify which failure modes show detectable precursor patterns in the sensor data that could enable early warning. *Data treatment: fully answerable from AI4I; subject to the same calibration-provenance caveat as BR-05. Per `01-Project-Charter.md` Objective O6, this is a diagnostic finding only — explicitly not a commitment to build or validate a predictive model in this engagement. See FR-13 (surfacing the finding) and FR-07/FR-08 (the process fixes this finding depends on to be actionable rather than, as the Reliability Engineer put it, "a bigger inbox to feel guilty about" — Interview-Transcript-Reliability-Engineer.md, Q8).*

---

## 8. Functional Requirements

**Traceability to Section 7:** BR-01 → FR-01, FR-04; BR-02 → FR-02; BR-03 → FR-03; BR-04 → FR-11; BR-05 → FR-12; BR-06 → FR-07, FR-08, FR-13. Every locked business requirement has at least one dedicated functional requirement — this table closes the gap the v1 draft left open for BR-04 and BR-05 (see Appendix B, findings 4.1–4.3).

**Must/Should rule (revised in v2 — see Appendix B, finding 4.5):** a requirement is labeled **Must** when it is either (a) requested by more than one interview source, or (b) required to directly answer one of the six locked business requirements, even where discovery produced only one or zero interview sources speaking to it directly — a locked business requirement does not stop being mandatory just because this particular discovery phase happened not to surface a second voice asking for it. A requirement is labeled **Should** when it is a single-source enhancement, a stretch goal, or supports but does not itself directly answer a BR. Every Must below states which branch of the rule applies.

### 8.1 Reporting & analysis

**FR-01 (Must — requested by 3 of 6 interviewed stakeholders; rule branch a) — Asset-level cumulative rollup.** The system must allow a user to select an asset and view its full failure and cost history over a trailing window, selectable from a fixed set of three options — 6, 12, or 24 months — with a running total, a month-over-month percentage-change figure, and a simple linear trend indicator, drillable down to the individual work orders that make up the total. Requested in separate, isolated interviews by the Maintenance Manager, as negotiating leverage for planned downtime against Operations (Q8); the Mining/Operations Manager, to plan proactively instead of reactively (Q10); and the Financial Controller, available at the point of work-order sign-off so a fourth patch repair on the same gearbox does not sail through unnoticed because each approval looked reasonable in isolation (Q9). Per Section 2.1, this convergence is read as a strong design signal, not as independent statistical proof. **See Risk 6 (Section 14): this requirement was framed by one requester explicitly as a negotiating tool against another stakeholder group whose trust and adoption this same capability depends on — the rollout and UI framing must manage that tension, not just the data model.** This is the dashboard's primary design element (Master Plan, Week 3), with the site-wide KPI/Pareto summary as a secondary layer.

**FR-02 (Must — rule branch b, required to answer BR-02) — Failure-mode Pareto view.** The system must present failure counts, ranked by failure mode across the fleet, and (where BR-01's cost scoping applies) the cost-weighted equivalent ranking, shown side by side rather than collapsed into one "worst" ranking. This directly answers BR-02. It does not, on its own, resolve which single metric (event count vs. cumulative downtime hours) makes an asset "the worst offender" — see Section 2's discussion of the Superintendent-vs-Reliability-Engineer disagreement; both views are surfaced so that disagreement can be argued with data, not settled by this requirement declaring a winner.

**FR-03 (Must — rule branch b, required to answer BR-03; zero interview sources address this view directly, stated plainly rather than implied) — Asset-tier segmentation view.** The system must present failure rate and (where in scope) cost broken down by asset tier (Low/Medium/High → ancillary/mobile fleet/fixed plant), side by side, supporting BR-03. This requirement exists because BR-03 is a locked business question (`Scope-Decisions-and-Limitations-Log.md`, 1 Sept 2026) and is grounded in the stakeholder register's decision-driven mapping for Q3 (Asset Manager – corporate, Maintenance Manager, Financial Controller, Mine Planning Engineer, Reliability Engineer — `02-Stakeholder-Register.md` Section 3), not in a specific interview transcript quote naming this exact view.

**FR-04 (Must — requested by 3 of 6 interviewed stakeholders across Section 15's acceptance criteria; relabeled from Should in v1 — see Appendix B, finding 4.4) — Confidence and traceability disclosure on every figure.** Every reported figure must carry a visible, consistently applied tag — a colored badge or icon, not merely a footnote — reading one of "Dataset-derived," "Cited source," or "Labeled assumption" (the project's three-tag data-integrity rule), state which external benchmark and source underpins any applied rate, and allow drill-down to the underlying work orders. This directly answers the Financial Controller's standard that "false precision" is the fastest way to lose her trust (Q4, Q10), and operationalizes BR-01's confidence-range requirement.

### 8.2 Data capture & process (CMMS reporting enhancement)

**FR-05 (Must — requested by 2 of 6 interviewed stakeholders; rule branch a) — Planned/unplanned separation at point of entry, not after the fact.** The work-order form must require an explicit planned/unplanned flag captured when the work order is raised, with a distinct mechanism for a work order that spans both a planned activity and an unplanned failure (rather than one combined duration, the specific defect that inflated the Financial Controller's crusher-event figure by roughly five hours — Q2). This is a process/data-capture requirement, not just a reporting one, and its technical feasibility against the site's actual CMMS platform is not yet validated — see Section 13.9.

**FR-06 (Must — rule branch a; minimum bar and stretch goal separated to remove the v1 self-contradiction — see Appendix B, finding 1.6) — Corrected repair-duration capture.**
- *Minimum bar (required to pass UAT):* every work order must support a flag indicating the crew was reassigned mid-repair to a higher-priority job, so recorded duration can be corrected for known dead time rather than silently overstating true repair time. This alone satisfies FR-06.
- *Stretch goal, not required for go-live:* live start/stop timestamp capture against a work order, where the CMMS platform supports it, is recommended as a fuller fix and should be pursued if Section 13.9's platform-feasibility validation confirms it is practical.

This directly operationalizes the Maintenance Superintendent, Fixed Plant's named mechanism for why fixed-plant repair-duration data is currently unusable (Q4), and converts Section 6's pain point #3 into a specific, buildable requirement rather than a general observation that the data is "not great."

**FR-07 (Should — single-sourced) — Automatic amber-trend escalation rule.** Condition-monitoring readings that remain in "amber" (caution) status for **three consecutive review cycles** — a starting assumption, not an empirically derived figure, pending confirmation by the Reliability Engineer before build (see Section 11) — must trigger an automatic flag or scheduling prompt, rather than relying on a person manually reviewing historical reports. Directly requested by the Reliability Engineer (Q7), who estimates current programs catch "maybe a third" of what they could without this. Sequencing note: per the Reliability Engineer's own caution (Q8), this should be implemented before or alongside any expansion of early-warning signal volume (FR-13) — more alerts on top of an unchanged escalation gap would add noise, not value.

**FR-08 (Should — single-sourced) — Calibration date logged against sensor ID.** The system should capture and display the last verified calibration date for each sensor feeding a condition-monitoring or precursor-pattern finding, so a future user can distinguish a genuine trend from instrumentation drift or fouling. Directly requested by the Instrumentation & Controls Engineer (Q5) as the fix for the calibration-provenance gap described in Section 13.3.

**FR-09 (Should — single-sourced; Operations-side review not yet obtained, see Section 13.8 and Risk 7) — Contributing-factor field, distinct from failure mode.** The work-order close-out form should offer a lightweight, non-disciplinary "suspected contributing factor" field (e.g., normal wear, suspected operator-influenced, overload/misuse suspected) separate from the technical failure-mode field. Requested unprompted by the Maintenance Manager (Q11), who was explicit this must be framed as a contributing-factor category for reliability analysis, never a blame or disciplinary record — a chunk of what is currently counted against maintenance's reliability numbers may in fact be an Operations training/supervision issue, and today there is no way to separate the two. **This field must not proceed to build without a review and sign-off from an Operations-side stakeholder — none was consulted on its design, and Risk 7 (Section 14) names why that matters given the field's sensitivity.**

**FR-10 (Should — single-sourced) — Cost-figure/report reconciliation.** Wherever a fixed-plant asset is reported by frequency only under BR-01/BR-06's Option B scoping (Section 10.3), that treatment must be reflected consistently in any parallel monthly cost reporting for the same asset, so the two documents never show conflicting figures for the same equipment. Requested by the Financial Controller (Q6) as a condition for the frequency-only treatment to hold up under scrutiny rather than create a new credibility problem. *(Correction from v1: this requirement is sourced to the Financial Controller alone. The Maintenance Superintendent, Fixed Plant's related but distinct request — pairing frequency with downtime hours, Q3 — is a separate ask, addressed under FR-06's duration-capture work, not this requirement; v1 Section 10.3 incorrectly credited both stakeholders to FR-10 itself. See Appendix B, finding 4.4.)*

**FR-11 (Must — rule branch b, required to answer BR-04) — Preventable-vs-random failure split view.** The reporting capability must display the percentage of total failures attributable to each of the four mechanically-explainable modes (TWF/HDF/PWF/OSF) individually and to the random-failure category (RNF), together with the multi-flag-row counting rule (Section 10.1) and RNF's own labelling-inconsistency caveat (Section 10.1, Finding 2) displayed alongside — per `01-Project-Charter.md` Objective O4's success criterion. *(New in v2 — closes the traceability gap flagged in Appendix B, finding 4.1.)*

**FR-12 (Should — demonstrates a method per `01-Project-Charter.md` Objective O5; not yet a production-deployable capability given Section 13.3) — Torque/tool-wear threshold display.** The reporting capability must display the tested torque/tool-wear threshold(s) for overstrain risk and the statistical result against the pre-agreed bar Objective O5 requires, with an explicit on-screen label that this demonstrates a method on AI4I's real sensor data, not a claim that the site's real fleet is currently instrumented to support the same finding in production. *(New in v2 — closes the traceability gap flagged in Appendix B, finding 4.2.)*

**FR-13 (Should — rule branch b, required to surface BR-06's finding) — Precursor-pattern classification display.** The reporting capability must classify and display, for each failure mode, whether it is detectable / not detectable / inconclusive for sensor precursor patterns, per `01-Project-Charter.md` Objective O6 — distinct from FR-07 (escalation) and FR-08 (calibration), which support acting on a detected pattern rather than displaying whether one exists in the first place. *(New in v2 — closes the traceability gap flagged in Appendix B, finding 4.3.)*

---

## 9. Non-Functional Requirements

**NFR-01 — No added data-entry burden, defined as a testable rule.** No new mandatory field may be added to the work-order close-out form (FR-05, FR-06, FR-08, FR-09) unless either (a) an existing mandatory field is removed or consolidated so the total mandatory-field count at close-out does not increase from today's baseline, or (b) a frontline tradesperson representative has explicitly signed off that the specific addition is worth the extra time. **Neither condition has been met yet for FR-05, FR-06, or FR-09 — see Section 13.8. This sign-off is required before those requirements proceed to build**, not assumed satisfied by the Maintenance Manager speaking on his crew's behalf (Q10).

**NFR-02 — Cross-functional technical access.** The reporting output must be technically accessible to Operations users at launch, not gated to Maintenance alone. *(Narrowed in v2 from "visible to and used by Operations" — the "used by" half is an adoption outcome, not something a build can guarantee on day one; it now lives as a tracked KPI in Section 9.1, not as a go-live gate. See Appendix B, finding 1.9.)*

**NFR-03 — Auditability.** Every figure must be traceable from a summary view down to the source work order(s) that produced it, on demand, without requiring a multi-day chase across teams. Explicitly required by the Financial Controller (Q4, Q10) as her non-negotiable first condition and her single fastest way to lose trust in the output.

**NFR-04 — Methodological stability and disclosure.** Any benchmark rate or methodology applied (e.g., a downtime-cost-per-hour figure) must remain stable across reporting periods, or, if it changes, the change and its reason must be explicitly flagged rather than silently absorbed into a new number. Explicitly required by the Financial Controller (Q4, Q10), who has personally seen two different downtime rates used for the same asset class in the same year with no one flagging it. *(Ongoing stability is verified across reporting cycles, not at a single UAT pass — see AC-4, Section 15.)*

**NFR-05 — Reconciliation with existing finance-system data.** Where a figure this project produces overlaps with data the Financial Controller already owns in the ERP/finance system (e.g., maintenance spend), the two must be reconcilable within a tolerance to be agreed with the Financial Controller before UAT sign-off (see Section 17, Action 3) — not run as two parallel, potentially conflicting versions of the truth with no defined tolerance for disagreement.

### 9.1 Post-launch adoption KPIs (tracked in the Benefit Realization Report — not a go-live gate)

**KPI-01 — Operations usage.** The reporting output is visibly used by Operations, not just present in a report Operations nods at and ignores, measured at six months post-launch. This is the Maintenance Manager's own stated bar for success (Q10) and is tracked as a benefit-realization outcome, not a build-time acceptance criterion — a system cannot be "tested" into being used by a team that chooses not to open it. *(Moved out of Section 15's acceptance-criteria list in v2 — see Appendix B, finding 5.10.)*

---

## 10. Data Requirements & Data Sources

### 10.1 Operational dataset

The core operational dataset is AI4I 2020 (UCI Machine Learning Repository / Kaggle), a real, published industrial predictive-maintenance dataset of 10,000 machine records with sensor readings and failure-mode labels. It is re-skinned onto a 48-asset synthetic mining fleet (5 High-tier fixed plant / 14 Medium-tier mobile fleet / 29 Low-tier ancillary equipment), matching AI4I's real tier proportions as closely as whole-number counts allow, via a reproducible, fixed-seed random tier-constrained assignment (0 tier violations across all 10,000 rows). Full data-lineage detail, including the three logical-consistency findings from the 24 August 2026 validation pass (unclassified-failure rows, RNF/machine-failure mismatches, overlapping failure-mode flags) and their resolution rules, is maintained in `Scope-Decisions-and-Limitations-Log.md` and will be restated in full in the eventual `data-lineage-note.md`.

### 10.2 External benchmarks (labeled assumptions)

AI4I has no repair-time, repair-cost, or timestamp field of any kind. Two categories of external, cited benchmark are used to make BR-01/BR-03 answerable in dollar/hours terms, applied uniformly at the asset-tier level rather than fabricated per row:

- **Repair time (partial coverage):** real, cited mining- and cement/aggregates-industry sources exist for mobile-fleet-class equipment (rope-shovel and LHD classes) and, as a cross-industry proxy, ancillary equipment (pumps, valves, motors). No defensible source exists for fixed-plant equipment as a class — see 10.3.
- **Downtime cost per hour:** a real, cited industry benchmark (not a fabricated round number), applied as a single external multiplier against AI4I-derived failure counts — never used to compute or back into a "finding" the dollar figure was meant to test.

Every figure produced from these benchmarks must carry the three-tag disclosure required by FR-04 and the Master Plan's own data-integrity rule.

### 10.3 Fixed-plant treatment — Option B (locked 1 September 2026)

Of the fleet's five High-tier (fixed-plant) equipment types, real, individually verified repair-duration data was found for only one — the ball/rod mill, sourced from Nugroho, Syawitri & An'am (2024), "Maintenance Analysis of Raw Mill Machines in Cement Production," *Engineering Proceedings* 63(1):5, MDPI (open access), doi.org/10.3390/engproc2024063005 — and even that required correcting the source paper's own misstated figures during an independent verification pass against its own Table 8 (full detail in `Scope-Decisions-and-Limitations-Log.md`). No usable repair-cost data exists for fixed plant at all, mining-specific or general industrial. **Decision: fixed-plant assets are reported by failure frequency only — no dollar or hours-lost figure is presented for this tier**, rather than forcing a tier-wide number from one mechanically dissimilar asset's data (a crusher, a mill, a conveyor, and a thickener fail in fundamentally different ways). This is written up as a named finding in its own right — the absence of trustworthy repair-duration data for the site's highest-criticality equipment is itself evidence for FR-06's process recommendation — not apologized for as an incomplete analysis. Per the Financial Controller's refinement (Section 8, FR-10), every frequency-only row must carry its own one-line disclosed reason, and the treatment must stay consistent with parallel monthly cost reporting for the same assets. The Maintenance Superintendent, Fixed Plant's related request — pairing frequency with downtime hours rather than a bare count (Q3) — is addressed separately, under FR-06's duration-capture work, since downtime hours is exactly the figure Option B exists because it is untrustworthy for this tier today.

### 10.4 Repair cost (labour + parts) — dropped from scope, explicitly disclosed

No publicly verifiable benchmark for mining maintenance repair cost exists anywhere, despite a targeted, documented sourcing effort (SMRP, OREDA, Deloitte, IMechE, MaintainX, academic life-cycle-cost literature, OEM handbooks). Repair cost is therefore dropped from the business case for all tiers; the dollar story runs on the sourced downtime-cost-per-hour figure instead. Per the Financial Controller's correction (Interview-Transcript-Financial-Controller.md, Q5), this is disclosed in these exact terms: *"This analysis does not include potential reductions in maintenance labour and parts cost, which represents additional unquantified upside; a real engagement would source this directly from the client's ERP/CMMS cost data, which this project's synthetic dataset has no equivalent for."*

---

## 11. Assumptions

- The AI4I 2020 dataset's failure behaviour, once re-skinned, is a reasonable stand-in for mining equipment failure patterns for the purpose of demonstrating this reporting methodology — not a claim that this simulated site's real fleet would show identical failure rates.
- Externally sourced repair-time and downtime-cost benchmarks (Section 10.2) are applied uniformly within an asset tier; a real deployment would refine these to asset- or failure-mode-specific rates as its own CMMS data matured.
- The synthetic asset register's criticality tiering (fixed plant = High, mobile fleet = Medium, ancillary = Low) reflects consequence-of-failure logic (single point of failure vs. fleet redundancy), not asset purchase cost or size — confirmed independently by the Maintenance Superintendent, Fixed Plant's own reasoning for why crusher and mill get default priority (Q1).
- Site location, used only as background scaffolding for the stakeholder narrative and process map, is never a reported finding (e.g., "Site B fails more than Site A") — that assignment is arbitrary and reporting it as an insight would be fabrication.
- **FR-07's "three consecutive amber cycles" threshold is a starting point for discussion with the Reliability Engineer, not a validated figure** — flagged for confirmation before build (Section 17, Action 4).

## 12. Constraints

- No real company data is used or available; every figure not directly computed from AI4I must be an externally sourced, cited benchmark or an explicitly labeled assumption — never a plausible-sounding invented number.
- No per-row dates exist in AI4I and none will be fabricated to enable trend/seasonality analysis; the missing time dimension is disclosed as a limitation (Section 13.4) rather than worked around.
- The project's data-integrity rule prohibits any assumption that presupposes the answer the analysis is meant to derive (e.g., assuming a planned/unplanned split in order to report one) — only assumptions of facts genuinely external to the dataset are permitted.
- This discovery phase reached six stakeholders across four full interviews and two short conversations; it did not reach frontline tradespeople, the CMMS/IT system owner, or capital planning/procurement — see Section 13.8–13.10 for what that leaves unvalidated.

---

## 13. Limitations

Presented here as explicit, named scope boundaries — the same discipline required of every dollar figure in this document — rather than left implicit or discovered by a skeptical reader.

**13.1 Equipment-attributable share only.** This analysis quantifies production loss attributable to unplanned equipment failure only. Blast delays, weather, haul-road closures, and rostering/crew shortages are real, additional causes of production shortfall that this dataset has no way to represent, and are out of scope. Raised unprompted by the Mining/Operations Manager, who warned that treating every tonnes miss as an equipment issue would itself cause misattribution.

**13.2 Sub-threshold stoppages are structurally invisible.** Stoppages under roughly 15 minutes — a conveyor tripping and resetting, an excavator stalling and restarting — never generate a CMMS work order today and are therefore invisible to any work-order-based dataset, including AI4I. This bounds BR-02, BR-04, and BR-06: a genuinely high-frequency, low-severity failure pattern (the exact "death by a thousand cuts" pattern the Reliability Engineer named for conveyor idlers) could be a larger true cost than anything this methodology can surface. Raised unprompted by the Reliability Engineer; not a data-cleaning defect this project can fix, since there is no sub-threshold event data to recover without fabricating it.

**13.3 Precursor/threshold findings cannot currently be distinguished from sensor drift or fouling.** No calibration-provenance tracking exists against sensor ID at this simulated site, so a genuine early-warning trend and an instrumentation artifact "look identical on a chart" (Instrumentation & Controls Engineer, Q4–Q5, with two concrete supporting incidents). BR-05 and BR-06 (FR-12, FR-13) demonstrate a valid analytical method on AI4I's real sensor data; they are not a claim that this finding is currently deployable in production without first closing this gap — see FR-08.

**13.4 No timestamp field — no trend or seasonality analysis.** AI4I has no chronological ordering. No dates are fabricated to enable a trend chart; this is disclosed rather than worked around.

**13.5 Commodity-price contamination (forward-looking, does not affect current build).** A downtime-cost-per-hour rate is ultimately a function of commodity price, which moves. Comparing that rate across time periods without disclosing the price assumption used each time risks mistaking a market move for a reliability signal. Raised by the Financial Controller (Q11); does not affect this project's current single-benchmark-rate build, but is a real consideration for any future longitudinal extension.

**13.6 Mobile fleet and fixed plant do not share a comparable cost structure.** A portion of mobile-fleet spend sits inside fixed-rate OEM maintenance contracts rather than itemized in-house repair costing, and would need to be treated differently in any future repair-cost analysis. Raised by the Financial Controller (Q11); already consistent with this project's existing tier-based benchmark segmentation (Section 10.2).

**13.7 This is a simulated engagement.** All stakeholder interviews are role-played personas standing in for unavailable real stakeholders, clearly flagged as such in each transcript. The dataset is a real, published, cited industrial dataset adapted to a synthetic mining context, not real company data — disclosed here and in every downstream deliverable per the project's data-integrity rule. See Section 2.1 for what "independent corroboration" between these personas does and does not establish.

**13.8 No frontline data-entry stakeholder was interviewed.** FR-05, FR-06, and FR-09 all add or change fields at work-order close-out, and NFR-01's "no added burden" standard is sourced entirely from the Maintenance Manager speaking on his crew's behalf (Q10) — no tradesperson who would actually complete these fields was interviewed. This is a real gap, not a formality: management's estimate of what feels burdensome to frontline staff is frequently wrong in real engagements. **FR-05, FR-06, and FR-09 must not proceed to build without direct frontline validation — see Section 17, Action 1.**

**13.9 No CMMS/IT system owner was interviewed.** FR-05 through FR-08 all require changes to the CMMS platform itself. None of the six interviewees administers or owns that system, so the technical feasibility, cost, and implementation complexity of these four requirements against the site's actual platform is entirely unvalidated. **See Section 17, Action 2.**

**13.10 The opex/capex approval-pathway finding is single-sourced.** The explanation in Section 2 for why quick fixes structurally out-compete root-cause repairs — separate opex/capex approval pathways with very different timelines — comes from the Financial Controller alone (Q8). No capital planning or procurement stakeholder was interviewed to corroborate how approval pathways actually work at this site. Carried forward in this document as a credible, well-reasoned hypothesis worth testing in the Week 3 business case, not as an established structural fact — Risk 1 (Section 14) and As-Is pain point #10 (Section 6) are both worded to reflect this.

**13.11 Small-sample precision limit.** The tier failure-rate figures cited in BR-03 (Section 7) are computed from a 5-asset High tier, 14-asset Medium tier, and 29-asset Low tier. Reporting these to two decimal places, as the v1 draft of this document did, implies a level of statistical precision a sample this small does not actually support. This document now rounds these figures to whole numbers in narrative text; the underlying exact values remain available in the data layer (Section 10.1) for anyone who specifically needs them, with the same rounding discipline to be applied consistently in the dashboard and business case.

---

## 14. Risks

| # | Risk | Source / evidence | Mitigation |
|---|---|---|---|
| 1 | Better reporting alone does not fix the fast-fix-vs-root-cause tension if the underlying opex/capex approval-pathway mismatch is left unaddressed — the Reliability Engineer named this directly as a way the project could fail: "if it shows me the pattern is real but nothing changes downstream... that's almost worse than not having the proof" (Q10). This risk itself rests partly on the single-sourced finding in Section 13.10 | Reliability Engineer Q10; Financial Controller Q8 (single-sourced, see 13.10) | Recommend FR-01's rollup be explicitly positioned as decision-support input to the capex/opex approval conversation (business case, Week 3), not only a technical report; validate the approval-pathway explanation with a capital-planning stakeholder before treating it as settled (Section 17, Action 2 area) |
| 2 | Repeated loss of the fast-fix-vs-root-cause argument has already produced a chilling effect — the Reliability Engineer now pre-emptively softens his own recommendations before they reach the Maintenance Manager, meaning the decision-maker may not be seeing the full technical picture today | Reliability Engineer Q9 | Flag in the business case; a trustworthy, quantified rollup (FR-01) is intended to directly counter this by giving the case "a number instead of a hunch" |
| 3 | If the reporting output is ever perceived as a blame tool rather than a decision tool, data quality degrades from the input side — people begin writing vague close-out notes deliberately | Reliability Engineer Q10 | FR-09's contributing-factor field is explicitly scoped as non-disciplinary; this framing must be preserved in how the field is introduced operationally, not just in this document — see Risk 7, which sharpens this specifically for FR-09 |
| 4 | If the underlying data is not kept current post-launch, trust collapses quickly and silently — the Reliability Engineer described this as a pattern he has "watched happen twice already": people quietly stop opening a report rather than flagging that it is wrong | Reliability Engineer Q10 | NFR-01 (no added burden) and FR-05/FR-06 (capture correctness at point of entry) are designed specifically to reduce the maintenance cost of keeping the data current |
| 5 | Frequency-only fixed-plant rows (Section 10.3) may read as an unexplained gap rather than a disclosed boundary if presentation requirements (FR-10) are not followed exactly | Financial Controller Q6 | Every frequency-only row carries a one-line disclosed reason per FR-10; treated as a mandatory formatting requirement, not an optional nicety |
| 6 | FR-01's asset-level rollup was requested by the Maintenance Manager explicitly as negotiating leverage against Operations (Q8), while NFR-02 and KPI-01 (Section 9.1) require the same view to be technically accessible to, and eventually trusted and used by, Operations. A tool rolled out as one team's ammunition risks the cross-functional adoption this project's own success bar depends on | Maintenance Manager Q8, in tension with Q10's own cross-functional-use standard | Rollout messaging and dashboard framing (Week 3 design) must present the view as shared decision-support — e.g., labeled "asset history," not a "worst offenders" league table — not as a weapon for one side of the Maintenance–Operations relationship. Explicit input for the Week 3 dashboard-design and Week 4 rollout-planning deliverables |
| 7 | FR-09's contributing-factor field was designed with input from the Maintenance Manager only. No Operations-side stakeholder has reviewed a field that, however carefully worded as non-disciplinary, assigns suspected fault in Operations' direction — combined with Risk 3's blame-tool concern, this is a specific, foreseeable adoption risk on top of a general one | Maintenance Manager Q11; absence of any Operations-side source on this specific field | FR-09 is explicitly held from build pending Operations-side stakeholder review and sign-off (also stated inline at FR-09, Section 8.2, and Section 17, Action 1) |

---

## 15. Acceptance Criteria

The Maintenance Manager's and Financial Controller's standards (Section 3) are merged below into one testable list, each item rewritten so a UAT tester has an actual pass/fail mechanism — not merely a value the document asserts is important. Three items from the v1 draft that were not independently testable have been consolidated into others, one has been reworded into a process-based test, and one adoption-outcome item has been moved to Section 9.1 as a post-launch KPI rather than a go-live gate (see Appendix B, findings 5.1–5.10, for the specific reasoning behind each change).

1. **Traceable.** Every summary figure can be drilled down to the specific underlying work order(s) it is built from, on demand.
2. **Every figure carries its FR-04 disclosure tag** (Dataset-derived / Cited source / Labeled assumption) at the point of display, with no figure presented untagged. *(Consolidates v1's items 2, 5, and 7, which all restated the same underlying "don't present estimates as if they were hard data" requirement in different words.)*
3. **Meets NFR-01's data-entry-burden rule** — no new mandatory close-out field without either removing an existing one or securing frontline sign-off (Section 9, NFR-01).
4. **Methodology is documented and dated as of launch** — any benchmark rate states its source and last-review date at go-live. *(Ongoing stability across future reporting cycles is a separate, ongoing check under NFR-04, not a one-time UAT gate — ongoing drift can only be observed over multiple reporting periods, not certified at a single point in time.)*
5. **Broken down by asset and by cause**, not presented as a single site-wide lump figure.
6. **Reconciles with existing finance-system figures within a tolerance agreed with the Financial Controller before UAT sign-off** (Section 17, Action 3 — no tolerance is invented here; setting one is an explicit open action, not a gap papered over with a plausible-sounding number).
7. **Survives a structured mock-challenge review** — every dollar/hours figure can be defended, using only its FR-04 disclosure and FR-01 drill-down, in a pre-go-live review session run with Finance and a GM-equivalent reviewer. *(Reworded from v1's untestable "survives scrutiny from Finance or the GM" into an actual process with a pass/fail outcome — a review meeting either happens and the figures hold up, or it doesn't and they don't.)*

Full traceability from these criteria to specific test cases is a Week 3 deliverable (`08-Test-Cases.md`) and will reference this section directly. **Section 9.1's post-launch adoption KPI (Operations usage within six months) is tracked separately in the Benefit Realization Report and is explicitly not part of this go-live acceptance list** — see Appendix B, finding 5.10, for why mixing a day-one gate with a six-month outcome in one undifferentiated list was a defect in v1.

---

## 16. Governance & Sign-off

Per the governance model resolved 1 September 2026 and title-clarified 3–4 September 2026 (`02-Stakeholder-Register.md` Section 4; `01-Project-Charter.md` v5, Appendix G):

- **Accountable Business Owner — Maintenance Manager.** Day-to-day sign-off authority on this document's content.
- **Project Sponsor — Operations Superintendent** (represented in the register by the Mining/Operations Manager role). Commissions the engagement and holds go/no-go authority.

Whether "Operations Superintendent" and "Mining/Operations Manager" name the same individual on a real org chart remains an open, separate question — see `02-Stakeholder-Register.md` Section 4 and `01-Project-Charter.md` Appendix G for the full reasoning. It does not block this document's approval, since both roles' sign-off authority holds regardless of how that identity question resolves.

**Approval record (to be completed at sign-off, not before — and not before the four validation actions in Section 17 are closed):**

| Role | Name/title | Approval | Date |
|---|---|---|---|
| Accountable Business Owner | Maintenance Manager | Pending | — |
| Project Sponsor | Operations Superintendent | Pending | — |

---

## 17. Next Steps

This document reflects revisions made in response to a structured adversarial review (Appendix A, Appendix B). Four validation actions remain open before this BRD proceeds to final sign-off — each traces to a specific gap the red-team review surfaced, not a generic disclaimer:

1. **Validate FR-05, FR-06, and FR-09 with frontline tradespeople** who will actually complete the affected fields, per NFR-01 and Section 13.8. Management's estimate of acceptable burden is not a substitute for the people doing the work weighing in.
2. **Engage the CMMS/IT system owner** to confirm FR-05 through FR-08's technical feasibility against the site's actual platform, per Section 13.9. This discovery phase never reached that stakeholder.
3. **Set the finance-reconciliation tolerance for AC-6** with the Financial Controller — currently an open parameter, not a fabricated number, per Section 15.
4. **Confirm the FR-07 escalation threshold (three consecutive amber cycles) with the Reliability Engineer**, per Section 11 — this is a starting assumption, not a validated figure.

Once these four are closed, this document proceeds to Accountable Business Owner and Project Sponsor sign-off per Section 16.

---

## Appendix A — Red-Team Critique Log (v1 → v2)

**Technique:** adversarial persona/role-prompting + critique loop, run in a separate, memory-isolated conversation with no visibility into how this BRD was drafted — the same fresh-context isolation technique already used twice, successfully, on `01-Project-Charter.md` (see that document's Appendices A and D).

**Prompt used:** the reviewer was instructed to act as "a skeptical, experienced Program Manager sitting on the sign-off committee" for this BRD, with no involvement in producing it, and asked to find every reason the document would get bounced back before approval across six categories: ambiguous/untestable requirements, unsupported/overstated claims, missing or conflicting stakeholder needs, traceability gaps, untestable acceptance criteria, and anything reading as AI-generated filler rather than real analysis.

**Full critique received, verbatim** (30 numbered findings across the six categories):

> [The full text of the red-team critique the user pasted into this conversation is preserved in this project's session record and is not re-transcribed here in full to avoid this appendix ballooning past what a reader needs; the finding-by-finding response is in Appendix B below, organized by the same six categories and numbered to match the critique's own structure: 1.1–1.9 (ambiguous/untestable), 2.1–2.4 (unsupported claims), 3.1–3.6 (stakeholder gaps), 4.1–4.5 (traceability), 5.1–5.10 (acceptance criteria), 6.1–6.6 (filler/professionalism).]

**Bottom-line assessment from the critique, quoted directly:** *"FR-06's Must/Should self-contradiction, the missing FR-04/FR-05 traceability for BR-04 and BR-05, and AC-9's untestable 'survives scrutiny' language would each independently be enough to bounce this back before a vote. The deeper issue underneath all six categories is the same one: the document repeatedly cites 'independent' multi-stakeholder corroboration as its strongest form of evidence, without ever establishing that the underlying personas were actually generated independently of each other — and that undermines the credibility of claims that otherwise look well-evidenced on the page."*

## Appendix B — v1 → v2 Change Log

| Finding # | v1 defect | Change made in v2 |
|---|---|---|
| 1.1 | BR-01's "stated confidence range" was never defined | BR-01 now defines the mechanism explicitly: FR-04's visible tag plus a source-stated error range or an explicit High/Medium/Low qualitative tier |
| 1.2 | BR-02's "one or two... majority" had no defined rule | BR-02 reworded to a ranked-by-share requirement with no fixed threshold, explicitly tied to Charter O2's success criterion (rigor of methodology, not a percentage) |
| 1.3 | BR-03 conflated a system requirement with a business judgement | BR-03 split: the reporting capability displays figures (FR-03); "does this justify investment" is now explicitly named as a business-case recommendation against Charter O3's pre-agreed materiality threshold, not a system behavior |
| 1.4 | FR-01's window options and "trend" were undefined | FR-01 now specifies exactly three required windows (6/12/24 months) and defines trend as month-over-month % change plus a linear trend indicator |
| 1.4b | FR-04's "visibly distinguish" had no defined mechanism | FR-04 now specifies a visible badge/icon tag, not a footnote, as the required mechanism |
| 1.5/1.6 | FR-06 was labeled Must but its own body said "should," with an undefined minimum bar | FR-06 rewritten with an explicit minimum bar (mandatory) and a clearly separated stretch goal (optional) |
| 1.7 | FR-07's escalation threshold was never defined | Set to three consecutive amber cycles, explicitly flagged as a starting assumption pending Reliability Engineer confirmation (Section 11, Section 17 Action 4) |
| 1.8 | NFR-01's "strictly necessary" was a judgment call, not a spec | Rewritten as a testable rule: no net increase in mandatory fields, or explicit frontline sign-off |
| 1.9 | NFR-02/AC-10 stated an adoption outcome as a build-time NFR | Split: NFR-02 now covers technical access only (testable at launch); usage is KPI-01 in new Section 9.1, tracked post-launch |
| 2.1 | "Independent" stakeholder corroboration was asserted without describing what independence actually means for role-played personas | New Section 2.1 added, read before the rest of the document, explaining plainly what the isolated-interview process does and does not establish |
| 2.2 | Repeated superlative language ("single most corroborated," etc.) with no stated rubric | Removed throughout; replaced with plain factual counts ("requested by N of 6 interviewed stakeholders") |
| 2.3 | BR-03's tier failure rates were stated to two decimal places from a 5/14/29-asset register (false precision) | Rounded to whole numbers throughout; new Section 13.11 explains why, and discloses the precise figures remain available in the data layer |
| 2.4 | Section 10.3's mill repair-time source paper was never named/cited in the BRD body | Full citation added inline (Nugroho, Syawitri & An'am 2024, DOI included) |
| 2.4b | Section 3's "Financial Controller's six-point standard" was referenced off-page, never itemized | Section 3 now itemizes all six points directly |
| 3.1/13.8 | No frontline tradesperson was interviewed, despite FR-05/06/09 changing their workflow and NFR-01 claiming "no added burden" on their behalf | New Limitation 13.8; NFR-01 rewritten as a testable rule requiring frontline sign-off; Section 17 Action 1 |
| 3.2/13.9 | No CMMS/IT system owner was interviewed, despite FR-05–FR-08 requiring platform changes | New Limitation 13.9; Section 17 Action 2 |
| 3.3/13.10 | The opex/capex approval-pathway finding (a structural root cause) was single-sourced and presented with the same confidence as multiply-corroborated findings | New Limitation 13.10; Section 2 and Risk 1 reworded to flag single-sourcing explicitly |
| 3.4 | FR-01's "negotiating leverage" framing (Maintenance Manager) was never reconciled with NFR-02's cross-functional-trust requirement | New Risk 6 (Section 14), cross-referenced from FR-01 |
| 3.5 | BR-02/FR-02 implied the Pareto view would "settle" the Superintendent-vs-Reliability-Engineer disagreement over two different, both-valid metrics | Section 2 and FR-02 reworded: both metrics (count and downtime-hours) are displayed side by side; neither is declared authoritative |
| 3.6 | FR-09's contributing-factor field had no Operations-side stakeholder input despite assigning suspected fault in Operations' direction | New Risk 7 (Section 14); FR-09 explicitly held pending Operations-side review; Section 17 Action 1 |
| 4.1 | BR-04 had no corresponding functional requirement | New FR-11 added |
| 4.2 | BR-05 had no corresponding functional requirement (only appeared as a limitation) | New FR-12 added |
| 4.3 | BR-06 had process-support FRs (07/08) but no FR to actually surface the finding | New FR-13 added |
| 4.4 | FR-03 cited no source; FR-10's source count contradicted itself between Section 8 and Section 10.3 | FR-03 now states its actual basis (locked BR + register's Q3 mapping) instead of implying an interview source; FR-10 corrected to cite the Financial Controller only, with the Superintendent's related-but-distinct request reattributed to FR-06 |
| 4.5 | FR-03/FR-04/FR-06/FR-10 Must/Should labels didn't follow the document's own stated rule | Must/Should rule restated explicitly at the top of Section 8 with two branches (multi-source, or required to answer a locked BR), and every label re-checked against it |
| 5.1–5.10 | Section 15's acceptance criteria mixed testable and untestable items, contained redundant items, and blended a day-one gate with a six-month adoption metric | List rewritten to 7 individually testable items; redundant items (old 2/5/7) consolidated into one; "stable" split into a launch-time check (AC-4) vs. an ongoing NFR-04 check; "survives scrutiny" reworded into a defined mock-challenge-review process (AC-7); the adoption item moved to new Section 9.1 as KPI-01, explicitly not a UAT gate |
| 6.1–6.6 | Reliance on unestablished "independence," repeated superlatives, an unusually self-narrated governance-title explanation, and an internal AI-process section (old Section 17) reading as workflow documentation rather than a business deliverable | Addressed by 2.1/2.2 above; Section 16's governance explanation trimmed to essential facts with detail pushed to the charter; the AI-process content moved out of the client-facing body into this Appendix and a new Appendix C, mirroring `01-Project-Charter.md` Appendix C's existing pattern for the same problem |

## Appendix C — Portfolio Process Note (kept separate from the professional deliverable body, mirroring `01-Project-Charter.md` Appendix C)

This BRD is one deliverable within a self-directed portfolio project simulating a BA engagement in the mining sector, built to demonstrate professional-standard BA work and disciplined use of AI (Claude) as an analytical and critique collaborator. The v1 → v2 revision documented in Appendix A/B above followed the Master Plan's specified technique for this deliverable (Week 1, Day 5): draft v1, then subject it to an adversarial red-team review run in a separate, memory-isolated conversation — deliberately structured so the reviewer had no access to the reasoning behind the original draft and could not unconsciously defend choices it had itself made. This is the same critique-loop technique already used twice on `01-Project-Charter.md` (see that document's Appendices A and D) and is logged in this project's prompt library as a reusable pattern, not a one-off. The specific finding this red-team pass produced that is most worth highlighting on its own — per the Master Plan's instruction to document at least one substantive override carefully — is the challenge to this document's "independent stakeholder corroboration" framing (Appendix A/B, findings 2.1 and 6.1): a real, structural weakness the drafting process introduced without noticing, caught by a genuinely adversarial second pass rather than by the same reasoning that produced the original claim.

## Appendix D — Reusable stakeholder pull-quotes

For the video walkthrough, LinkedIn article, and one-page case study (Master Plan, Section 5), collected here rather than left scattered across six transcripts:

- *"If it's just pulling straight out of the CMMS the way it's filled in today... then you've just automated my spreadsheet problem, you haven't fixed it."* — Maintenance Manager, Q10
- *"I'm one bloke with a spreadsheet and a hunch."* — Reliability Engineer, Q3
- *"Give him the number and maybe he pushes back for once instead of waving the patch job through."* — Reliability Engineer, Q8, on the Maintenance Manager
- *"We've never sat down and actually looked at it side by side with real numbers... everyone's got their own asset they reckon is the worst and nobody's got the data to settle it."* — Maintenance Superintendent, Fixed Plant, Q5
- *"A blank cell with a documented reason behind it is something I can stand behind. A confident-looking wrong number is something that eventually gets me in front of the GM explaining myself, and I've been there, I don't want to go back."* — Financial Controller, Q6
- *"A genuine precursor trend and a drifting or fouled sensor look identical on a chart."* — Instrumentation & Controls Engineer, Q4
