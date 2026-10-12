# 07 — User Stories & Acceptance Criteria: Maintenance Reliability CMMS Reporting Enhancement

**Project:** Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability (mining fleet + fixed-plant maintenance function)
**Prepared by:** Gagana Suresh, Business Analyst
**Source document:** `03-BRD-Maintenance-Reporting.md` v2 — every story below traces to a specific Functional Requirement (FR) and, through it, to a locked Business Requirement (BR). No story here introduces a capability the BRD does not already require; this document's job is to translate what the BRD specified into backlog-ready, sprint-sized items with testable acceptance criteria, not to re-derive scope.
**Format:** Jira/Trello-style backlog — one story per card, grouped into epics matching the BRD's own functional groupings (Section 8.1 Reporting & Analysis, Section 8.2 Data Capture & Process).
**Date:** 28 September 2026
**Status:** DRAFT — ready for backlog import once reviewed; several stories are explicitly held from sprint planning pending validation actions still open in the BRD (Section 17) — see each story's Status field, not a blanket caveat.

---

## How to read this document

**Priority** is inherited directly from the BRD's own Must/Should rule (Section 8), not reassigned here: **Must** = requested by more than one interview source, or required to directly answer a locked business requirement even with zero/one source; **Should** = single-source enhancement, stretch goal, or supports but doesn't itself answer a BR. Re-litigating priority in this document would silently override a decision the BRD already made and documented — so every story states which BRD rule branch produced its priority, not a fresh judgment call.

**Status** is new information this document adds that the BRD's requirement list doesn't itself carry: whether a story is actually ready to be pulled into a sprint today.
- **Ready** — no open validation gap blocks build.
- **Blocked — pending [X]** — the BRD's own Section 17 next steps, or a named Risk (Section 14), explicitly hold this requirement from build until a specific validation happens. Cite the exact action/risk, not a vague "needs review."
- **Proposed — not yet in BRD** — sourced from a requirement still in "proposed" status in the Scope-Decisions-and-Limitations-Log, not yet a numbered BRD FR. Included so the backlog reflects real upcoming scope, but must not be sprint-planned until formally added to the BRD.

**Acceptance criteria** use Given/When/Then and are written to be independently testable — each one either clearly passes or clearly fails when checked, per the same discipline the BRD's own Section 15 red-team pass enforced on its acceptance criteria. `08-Test-Cases.md` (Week 3, Day 15) will derive formal UAT test cases directly from these.

**Technique used to build this document (for the prompt library):** few-shot prompting. US-01 and US-07 below were drafted first as fully-detailed exemplars to establish the house format, tone, and acceptance-criteria rigor bar — Gagana reviewed and approved both before the remaining 16 stories were generated to match that same standard. This keeps output format consistent across a 17-story backlog without needing to specify structure from scratch for every card.

---

## Backlog summary

| ID | Epic | Story | Priority | Traces to | Status |
|---|---|---|---|---|---|
| US-01 | Asset-Level Cumulative Rollup | Maintenance Manager — negotiating leverage | Must | FR-01 → BR-01 | Ready |
| US-02 | Asset-Level Cumulative Rollup | Operations Manager — proactive planning | Must | FR-01 → BR-01 | Ready |
| US-03 | Asset-Level Cumulative Rollup | Financial Controller — sign-off drill-down | Must | FR-01 → BR-01 | Ready |
| US-04 | Failure-Mode Pareto | Reliability lead — dual-metric ranking | Must | FR-02 → BR-02 | Ready |
| US-05 | Asset-Tier Segmentation | Investment-tier comparison view | Must | FR-03 → BR-03 | Ready |
| US-06 | Confidence & Traceability | Figure-level trust disclosure | Must | FR-04 → BR-01 | Ready |
| US-07 | CMMS Data Capture | Planned/unplanned flag at entry | Must | FR-05 → BR-01 | Blocked — pending Section 17 Actions 1 & 2 |
| US-08 | CMMS Data Capture | Mid-repair reassignment flag (minimum bar) | Must | FR-06 → BR-01 | Blocked — pending Section 17 Actions 1 & 2 |
| US-09 | CMMS Data Capture | Live start/stop timestamp capture (stretch) | Should | FR-06 → BR-01 | Blocked — pending Section 17 Action 2 (platform feasibility) |
| US-10 | Condition Monitoring | Amber-trend auto-escalation | Should | FR-07 → BR-06 | Blocked — pending Section 17 Action 4 (threshold confirmation) |
| US-11 | Condition Monitoring | Calibration date against sensor ID | Should | FR-08 → BR-06 | Ready |
| US-12 | CMMS Data Capture | Contributing-factor field | Should | FR-09 → BR-01 | Blocked — pending Operations-side review (Risk 7, Section 17 Action 1) |
| US-13 | CMMS Data Capture | Fixed-plant cost/frequency reconciliation | Should | FR-10 → BR-01 | Ready |
| US-14 | Preventable vs. Random Split | Failure-mode explainability view | Must | FR-11 → BR-04 | Ready |
| US-15 | Precursor & Threshold Analysis | Torque/tool-wear threshold display | Should | FR-12 → BR-05 | Ready |
| US-16 | Precursor & Threshold Analysis | Precursor-pattern classification display | Should | FR-13 → BR-06 | Ready |
| US-17 | Cause-Code Taxonomy (proposed) | Simplified cause-code list | — (unprioritized) | FR-14 (proposed) | Proposed — not yet in BRD |

---

## Epic 1 — Asset-Level Cumulative Rollup (FR-01 → BR-01)

The dashboard's primary design element (Master Plan, Week 3), requested independently by three stakeholders in separate interviews for three different reasons (Section 2.1 of the BRD explains plainly what that convergence does and doesn't prove — read as a strong design signal, not statistical proof). One underlying view, three stories, because each persona uses it at a different moment for a different purpose — splitting them keeps each story's acceptance criteria honest about what that specific user actually needs to see, rather than one bloated card trying to satisfy three use cases at once.

### US-01 — Maintenance Manager: asset history as negotiating leverage *(exemplar — house format)*

**Priority:** Must (rule branch a — requested by 3 of 6 interviewed stakeholders)
**Traces to:** FR-01 → BR-01
**Status:** Ready

**Story:**
As a Maintenance Manager, I can view an asset's cumulative failure and cost history over a trailing window, so that I can negotiate planned downtime against Operations with a defensible number instead of a guess.

**Acceptance Criteria:**
1. Given an asset with logged failure history, when I select that asset from the asset list, then I can choose a trailing window of exactly 6, 12, or 24 months (no other window options are presented).
2. Given a selected window, when the view loads, then I see a running total of failure count, and — for Medium/Low-tier assets in cost scope — a running total dollar figure, for that window.
3. Given a selected window, when the view loads, then I see a month-over-month percentage-change figure and a simple linear trend indicator (e.g., up/flat/down), not a bare number with no directional context.
4. Given a displayed total, when I click into any individual month, then I can drill down to the specific work order(s) that make up that month's total, per NFR-03's auditability requirement.
5. Given this view will double as negotiating input against Operations, when the view is labeled in the UI, then it is framed as shared decision-support ("Asset History"), not as a ranked "worst offenders" league table — per Risk 6 (BRD Section 14), so the same view Operations is expected to trust and adopt (NFR-02, KPI-01) doesn't read as one team's ammunition against them.

**Notes:**
- Source: Interview-Transcript-Maintenance-Manager.md, Q8.
- AC5 is a framing/UX constraint, not a data requirement — flagged explicitly here because it's easy for a dev team to build the correct data view and still ship a title/label that undermines cross-functional adoption. Carry this into the Week 3 dashboard-design critique pass.
- Shares its acceptance criteria core (AC1–4) with US-02 and US-03 below — the underlying view is the same; only the framing note (AC5) and the "so that" differ per persona.

### US-02 — Operations Manager: proactive weekly planning

**Priority:** Must (rule branch a)
**Traces to:** FR-01 → BR-01
**Status:** Ready

**Story:**
As the Mining/Operations Manager, I can view an asset's cumulative failure and cost history over a trailing window, so that I can plan my week proactively around known risk assets instead of reacting after a breakdown.

**Acceptance Criteria:**
1. Given an asset with logged failure history, when I select that asset, then I can choose a 6, 12, or 24-month trailing window (identical selector to US-01 — one shared component, not a duplicate build).
2. Given a selected window, when the view loads, then the linear trend indicator is visually prominent enough to scan across multiple assets quickly (this is a planning tool used across many assets in one sitting, not a single-asset deep dive) — verified by a UX review, not a numeric test.
3. Given the view is technically accessible to Operations users (NFR-02), when an Operations user without a Maintenance-system login attempts to open it, then access does not require a Maintenance-team credential or handoff.
4. Given the same drill-down capability as US-01 AC4, when I click into a month, then I reach the same underlying work orders Maintenance sees — one shared source of truth, not a separate Operations-facing summary that could drift from Maintenance's view.

**Notes:**
- Source: Interview-Transcript-Operations-Manager.md, Q10.
- AC3 and AC4 exist specifically because this story's stakeholder is the one NFR-02 was written to protect — Operations must not be a second-class viewer of a tool built primarily around the Maintenance Manager's ask (US-01).

### US-03 — Financial Controller: catch repeat-patch patterns at sign-off

**Priority:** Must (rule branch a)
**Traces to:** FR-01 → BR-01
**Status:** Ready

**Story:**
As the Financial Controller, I can view an asset's cumulative failure and cost history over a trailing window at the point of work-order sign-off, so that a fourth patch repair on the same asset doesn't sail through unnoticed because each individual approval looked reasonable in isolation.

**Acceptance Criteria:**
1. Given a work order pending my sign-off, when I open the approval screen, then I can access that asset's cumulative rollup (US-01's view) without leaving the approval workflow to search for it separately.
2. Given a selected window, when the view loads, then repeat work orders against the same asset within the window are visually distinguishable from one-off events (e.g., a repeat-count indicator), directly addressing the specific gap named in Section 6, pain point #9 (repeat-cost invisibility).
3. Given NFR-03 (auditability) and NFR-05 (finance-system reconciliation), when I drill into a work order from this view, then the figures shown are reconcilable with what I already see in the ERP/finance system, within the tolerance to be agreed under Section 17, Action 3.

**Notes:**
- Source: Interview-Transcript-Financial-Controller.md, Q9.
- AC1's "without leaving the approval workflow" is a real UX/integration requirement, not decoration — it's the difference between a tool that actually catches the repeat-patch pattern at the moment of decision and one that exists but isn't consulted, which the BRD (Section 6, pain point #9) identifies as today's actual failure mode.
- AC3's tolerance is explicitly not invented here — same open-parameter discipline the BRD itself applies (Section 15, AC-6).

---

## Epic 2 — Failure-Mode Pareto (FR-02 → BR-02)

### US-04 — Dual-metric failure-mode ranking

**Priority:** Must (rule branch b — required to answer BR-02)
**Traces to:** FR-02 → BR-02
**Status:** Ready

**Story:**
As a Reliability Engineer or Maintenance Superintendent, I can see failure modes ranked both by event count and by cost-weighted downtime, side by side, so that the crusher-vs-mill "worst offender" disagreement can be argued with real numbers instead of gut feel.

**Acceptance Criteria:**
1. Given fleet-wide failure data, when I open the Pareto view, then failure modes are ranked by event count using the primary-cause (mutually exclusive, one-per-event) counting rule.
2. Given the same view, when Medium/Low-tier cost data is in scope, then a separate cost-weighted ranking is shown side by side with the count ranking — not merged into a single blended score.
3. Given a failure mode with more than one contributing flag on the same event (Section 10.1's multi-flag-row rule), when displayed, then both the primary-cause count and the true-occurrence count are visible, with the difference between them stated, not hidden.
4. Given two rankings that disagree on which mode is "worst" (count vs. cost), when both are displayed, then neither is visually marked as the authoritative answer — this view surfaces the disagreement for a human decision, it does not resolve it.

**Notes:**
- Source: BRD Section 2 (Superintendent-vs-Reliability-Engineer disagreement), Section 8 FR-02.
- AC4 exists because the BRD is explicit that this requirement must not appear to "settle" a genuine two-metric disagreement — a dev team building a single ranked list would violate the requirement even if the underlying numbers were correct.

---

## Epic 3 — Asset-Tier Segmentation (FR-03 → BR-03)

### US-05 — Tier-level failure rate and cost comparison

**Priority:** Must (rule branch b — required to answer BR-03)
**Traces to:** FR-03 → BR-03
**Status:** Ready

**Story:**
As a Maintenance Manager or Financial Controller, I can see failure rate and (where in scope) cost broken down by asset tier, so that I have the evidence base to evaluate whether differentiated maintenance investment across tiers is justified.

**Acceptance Criteria:**
1. Given the three asset tiers (Low/Ancillary, Medium/Mobile-fleet, High/Fixed-plant), when I open the tier view, then failure rate is displayed for all three tiers, rounded to whole numbers per Section 13.11's small-sample precision limit.
2. Given Medium and Low tiers have cost data in scope, when displayed, then a cost figure appears for those two tiers; the High tier shows failure frequency only, with its one-line disclosed reason visible inline (per FR-10), not a blank or missing cell.
3. Given this view's output feeds an investment recommendation, when displayed, then the view presents figures only — it does not display or imply a "recommended investment tier," since that judgment belongs to the Week 3 business case against Charter Objective O3's pre-agreed materiality threshold, not to this system.

**Notes:**
- Source: BRD Section 7 (BR-03), Section 13.11.
- AC3 is a deliberate scope boundary carried over from the BRD's own v1→v2 fix (Appendix B, finding 1.3) — this system reports, it does not decide.

---

## Epic 4 — Confidence & Traceability Disclosure (FR-04 → BR-01)

### US-06 — Figure-level trust and source disclosure

**Priority:** Must (rule branch a — requested by 3 of 6 interviewed stakeholders; relabeled from Should in BRD v1, see Appendix B finding 4.4)
**Traces to:** FR-04 → BR-01
**Status:** Ready

**Story:**
As a Financial Controller (or any user relying on a reported figure), I can see, at a glance, whether a number is dataset-derived, from a cited external source, or a labeled assumption, so that I never mistake an estimate for hard data and can defend any figure under scrutiny.

**Acceptance Criteria:**
1. Given any reported figure anywhere in the reporting capability, when displayed, then it carries a visible badge or icon — not a footnote or tooltip-only disclosure — reading "Dataset-derived," "Cited source," or "Labeled assumption."
2. Given a figure tagged "Cited source" or "Labeled assumption," when I interact with its badge, then the specific external benchmark and source are shown (e.g., "RS/IMechE 2023 UK/Ireland survey, ~£5,000/hr").
3. Given any figure, when I use the drill-down control, then I reach the underlying work order(s) it was built from.
4. Given a full audit of the reporting capability's screens, when checked, then zero figures are found displayed without one of the three tags — this is a pass/fail structural check, not a sampling exercise.

**Notes:**
- Source: Interview-Transcript-Financial-Controller.md, Q4, Q10 — "a confident-looking wrong number is something that eventually gets me in front of the GM explaining myself."
- AC4's "zero figures, not a sample" phrasing matches how the BRD's own Section 15, AC-2 is written — this is a completeness requirement, not a best-effort one.

---

## Epic 5 — CMMS Data Capture & Process Enhancements (FR-05, FR-06, FR-09, FR-10)

Every story in this epic is a change to the work-order lifecycle itself, not just a reporting view — which is exactly why three of the five carry a **Blocked** status below. The BRD is explicit (Section 13.8–13.9, Section 17) that no frontline tradesperson or CMMS/IT system owner was interviewed during discovery, so these requirements are validated from a management and reporting-consumer perspective only. Carrying that gap into the backlog as an honest blocked status, rather than a story marked "ready" that isn't, is the more defensible move under interview pushback.

### US-07 — Planned/unplanned flag at point of entry *(exemplar — house format)*

**Priority:** Must (rule branch a — requested by 2 of 6 interviewed stakeholders)
**Traces to:** FR-05 → BR-01
**Status:** Blocked — pending Section 17 Action 1 (frontline validation) and Action 2 (CMMS/IT platform feasibility)

**Story:**
As a Financial Controller, I need every work order to carry an explicit planned/unplanned flag captured at the moment it's raised, so that a planned inspection can never again be silently bundled into an unplanned-failure figure the way the primary-crusher work order was.

**Acceptance Criteria:**
1. Given a new work order is being raised, when the form is submitted, then an explicit planned/unplanned flag is a required field — the work order cannot be saved without it.
2. Given a work order that spans both a planned activity and an unplanned failure on the same asset, when raised, then a distinct mechanism captures both parts with their own durations, rather than one combined duration attributed entirely to "unplanned."
3. Given NFR-01's no-added-burden rule, when this field is added, then either an existing mandatory field has been removed/consolidated to hold the net mandatory-field count flat, or a frontline tradesperson representative has explicitly signed off that this specific addition is worth the added time.
4. Given this is a CMMS platform change, when build is scoped, then feasibility against the site's actual CMMS platform has been confirmed by its system owner before implementation begins.

**Notes:**
- Source: Interview-Transcript-Financial-Controller.md, Q2 (the ~5-hour overstatement incident); BRD Section 13.8, 13.9.
- **This story cannot honestly be marked Ready.** AC3 and AC4 are conditions the BRD itself says are not yet met (Section 13.8: "neither condition has been met yet for FR-05, FR-06, or FR-09"). Listing it as Ready would misrepresent the backlog's actual state to whoever picks it up next — a real product owner would bounce this back at grooming, so it's flagged here first instead.
- Do not pull into a sprint until Section 17 Actions 1 and 2 close.

### US-08 — Mid-repair reassignment flag (minimum bar)

**Priority:** Must (rule branch a)
**Traces to:** FR-06 → BR-01
**Status:** Blocked — pending Section 17 Actions 1 & 2 (same gaps as US-07)

**Story:**
As a Maintenance Manager, I need a work order to indicate when a crew was reassigned mid-repair to a higher-priority job, so that recorded repair duration reflects actual work time, not the dead time the crew spent away from the job.

**Acceptance Criteria:**
1. Given a work order in progress, when a crew is pulled off to a higher-priority job, then the technician can set a "reassigned mid-repair" flag on that work order.
2. Given the flag is set, when the work order's duration is calculated for reporting, then the dead time between reassignment and return is excluded or clearly separated from the recorded repair duration, rather than silently inflating it.
3. Given this is the BRD's defined minimum bar for FR-06 (not the stretch goal), when UAT is run, then this flag alone — without live timestamp capture — is sufficient to pass FR-06's acceptance test.

**Notes:**
- Source: Interview-Transcript-Maintenance-Superintendent-Fixed-Plant.md, Q4 — the most specific, mechanism-level finding from the entire discovery phase.
- Directly targets Section 6, pain point #3.

### US-09 — Live start/stop timestamp capture (stretch goal)

**Priority:** Should (explicitly a stretch goal, not required for go-live — BRD Section 8, FR-06)
**Traces to:** FR-06 → BR-01
**Status:** Blocked — pending Section 17 Action 2 (CMMS platform feasibility); not required for FR-06 to pass UAT

**Story:**
As a Maintenance Superintendent, I want repair start and stop times captured live against a work order, so that repair duration is measured directly instead of reconstructed from memory, sometimes days later.

**Acceptance Criteria:**
1. Given the CMMS platform supports live timestamp entry (unconfirmed — see status), when a technician starts a repair, then a start timestamp is logged without requiring a separate manual entry step after the fact.
2. Given a repair is completed, when the technician closes the work order, then the stop timestamp is captured at that moment, not backfilled later.
3. Given US-08 already satisfies FR-06's minimum bar, when prioritizing the backlog, then this story is understood as additive polish, not a blocker to FR-06 being considered "done."

**Notes:**
- Explicitly the lower-priority half of FR-06 — do not let this stretch goal delay US-08's minimum bar into a later release.

### US-10 — Amber-trend automatic escalation

**Priority:** Should (single-sourced)
**Traces to:** FR-07 → BR-06
**Status:** Blocked — pending Section 17 Action 4 (Reliability Engineer confirmation of the 3-cycle threshold)

**Story:**
As a Reliability Engineer, I want a condition-monitoring reading that stays in "amber" status for a defined number of consecutive review cycles to trigger an automatic flag, so that early-warning signals stop depending on someone remembering to manually re-check historical reports.

**Acceptance Criteria:**
1. Given a sensor reading remains "amber" for 3 consecutive review cycles (the BRD's stated starting assumption, not yet validated), when the 3rd cycle closes, then an automatic flag or scheduling prompt is generated without manual review.
2. Given the threshold value itself, when this story is groomed, then the 3-cycle figure is confirmed or revised with the Reliability Engineer before implementation — it is explicitly not to be hardcoded from this document without that confirmation.
3. Given FR-13's sequencing dependency, when this escalation rule is deployed, then it is live before or alongside any expansion of precursor-pattern alert volume (US-16) — more alerts without a working escalation gate adds noise, not value, per the Reliability Engineer's own caution.

**Notes:**
- Source: Interview-Transcript-Reliability-Engineer.md, Q7–Q8. Estimated current programs catch "maybe a third" of what they could without this.

### US-11 — Calibration date logged against sensor ID

**Priority:** Should (single-sourced)
**Traces to:** FR-08 → BR-06
**Status:** Ready

**Story:**
As an Instrumentation & Controls Engineer, I want the last verified calibration date displayed against every sensor feeding a condition-monitoring or precursor finding, so that a future reviewer can tell a genuine trend apart from instrumentation drift or fouling.

**Acceptance Criteria:**
1. Given a sensor feeding any condition-monitoring or precursor-pattern display, when that display is shown, then the sensor's last verified calibration date is visible alongside it.
2. Given a sensor with no recorded calibration date, when displayed, then this is shown as an explicit, visible gap ("calibration not recorded"), not a blank field a user could mistake for "recently calibrated."
3. Given two readings that look like the same trend, when one sensor's calibration is stale and the other's is current, then a reviewer can distinguish which is more trustworthy using this field alone, without needing to ask the Instrumentation team directly.

**Notes:**
- Source: Interview-Transcript-Instrumentation-Controls-Engineer.md, Q5 — directly closes the calibration-provenance gap described in BRD Section 13.3.

### US-12 — Contributing-factor field at close-out

**Priority:** Should (single-sourced)
**Traces to:** FR-09 → BR-01
**Status:** Blocked — pending Operations-side stakeholder review and sign-off (Risk 7, Section 17 Action 1)

**Story:**
As a Maintenance Manager, I want a lightweight "suspected contributing factor" field at work-order close-out, separate from the technical failure-mode field, so that operator-influenced damage isn't silently absorbed into maintenance's own reliability numbers.

**Acceptance Criteria:**
1. Given work-order close-out, when completing the form, then an optional "suspected contributing factor" field is available (e.g., normal wear, suspected operator-influenced, overload/misuse suspected), visually distinct from the failure-mode field.
2. Given the field's sensitivity, when presented in the UI, then it is explicitly labeled as being for reliability-analysis purposes only and not a disciplinary record — this labeling is itself part of the acceptance test, not just a design suggestion.
3. Given this field assigns suspected fault in Operations' direction, when this story reaches grooming, then it does not proceed to build until an Operations-side stakeholder has reviewed and signed off on its design and wording.

**Notes:**
- Source: Interview-Transcript-Maintenance-Manager.md, Q11 (raised unprompted).
- **This is the single most sensitive story in the backlog.** The BRD names two compounding risks here (Risk 3: reporting-as-blame-tool degrades data quality from the input side; Risk 7: zero Operations-side input on a field that points at Operations). Do not let this story's low priority label ("Should") understate how carefully it needs to be handled before build — priority reflects sourcing count, not risk.

### US-13 — Fixed-plant cost/frequency reporting reconciliation

**Priority:** Should (single-sourced)
**Traces to:** FR-10 → BR-01
**Status:** Ready

**Story:**
As a Financial Controller, I want fixed-plant assets reported by frequency only in this system to show the same treatment in parallel monthly cost reporting, so that the two documents never present conflicting figures for the same equipment.

**Acceptance Criteria:**
1. Given a High-tier (fixed-plant) asset reported by frequency only under Option B, when the same asset appears in monthly cost reporting, then that report also omits a dollar/hours figure for it, rather than showing one sourced differently.
2. Given a frequency-only row in either report, when displayed, then it carries the same one-line disclosed reason in both places (consistent wording, not just consistent absence of a number).
3. Given a reviewer cross-checks both reports for the same asset in the same period, when compared, then no contradiction exists between them.

**Notes:**
- Source: Interview-Transcript-Financial-Controller.md, Q6 — her explicit condition for Option B to hold up under scrutiny.
- Distinct from US-08/US-09: the Fixed-Plant Superintendent's related "pair frequency with downtime hours" request (Q3) is addressed by FR-06's duration-capture work, not this story — kept separate per the BRD's own correction of a v1 mis-attribution (Appendix B, finding 4.4).

---

## Epic 6 — Preventable vs. Random Failure Split (FR-11 → BR-04)

### US-14 — Failure-mode explainability view

**Priority:** Must (rule branch b — required to answer BR-04)
**Traces to:** FR-11 → BR-04
**Status:** Ready

**Story:**
As a Reliability Engineer, I can see what proportion of failures fall into each mechanically explainable mode versus the dataset's random-failure category, so that I can distinguish preventable failure patterns from inherently unpredictable ones.

**Acceptance Criteria:**
1. Given failure records, when the view loads, then the percentage of total failures attributable to each of TWF, HDF, PWF, OSF individually, and to RNF, is displayed.
2. Given the multi-flag-row counting rule (Section 10.1), when a failure event has more than one mode flag set, then the display states plainly how that event is counted (primary-cause vs. true-occurrence), rather than presenting one number as if no such ambiguity existed.
3. Given RNF's documented labeling-inconsistency caveat (rows where RNF is set independently of the overall failure flag), when RNF's percentage is displayed, then this caveat is shown alongside it, not only in a separate methodology document.

**Notes:**
- Source: BRD Section 7 (BR-04), directly answerable from AI4I's own taxonomy — no external benchmark needed for this one.

---

## Epic 7 — Precursor & Threshold Analysis (FR-12, FR-13 → BR-05, BR-06)

### US-15 — Torque/tool-wear overstrain threshold display

**Priority:** Should (demonstrates a method per Charter Objective O5; not yet production-deployable — Section 13.3)
**Traces to:** FR-12 → BR-05
**Status:** Ready

**Story:**
As a Reliability Engineer, I can see the tested torque/tool-wear threshold(s) associated with overstrain risk, so that I have an evidence base for evaluating a proactive replacement policy.

**Acceptance Criteria:**
1. Given AI4I's sensor data, when the threshold analysis is displayed, then the tested threshold(s) and the statistical result against the pre-agreed bar (Charter Objective O5) are shown.
2. Given this is a method demonstration rather than a production capability, when displayed, then an explicit on-screen label states this demonstrates a method on AI4I's real sensor data, not a claim that this site's actual fleet is currently instrumented to support the same finding in production.
3. Given the calibration-provenance limitation (Section 13.3), when this finding is presented anywhere outside this view (dashboard, business case), then the same production-readiness caveat travels with it — not only shown here and dropped elsewhere.

**Notes:**
- Source: BRD Section 7 (BR-05); Interview-Transcript-Reliability-Engineer.md, finding 7.

### US-16 — Precursor-pattern classification display

**Priority:** Should (rule branch b — required to surface BR-06's finding)
**Traces to:** FR-13 → BR-06
**Status:** Ready

**Story:**
As a Reliability Engineer, I can see which failure modes show detectable precursor patterns in sensor data versus which don't, so that I know where early-warning monitoring is worth investing in and where it isn't.

**Acceptance Criteria:**
1. Given each failure mode, when the view loads, then it is classified as detectable, not detectable, or inconclusive for sensor precursor patterns, per Charter Objective O6.
2. Given this view is distinct from FR-07 (escalation) and FR-08 (calibration), when built, then it displays classification only — it does not itself trigger an escalation action or require a calibration check to function.
3. Given the calibration-provenance limitation, when a mode is classified "detectable," then the same drift-vs-genuine-trend caveat as US-15's AC3 is visible alongside it.

**Notes:**
- Source: BRD Section 7 (BR-06). Feeds directly into US-10's escalation logic once both exist, but is scoped here as a separate, standalone display requirement.

---

## Epic 8 — Cause-Code Taxonomy Simplification (FR-14, proposed)

### US-17 — Simplified, consistent cause-code list

**Priority:** Unprioritized — this requirement has no Must/Should label because it is not yet a numbered BRD functional requirement, so the BRD's own priority rule (Section 8) doesn't formally apply to it yet.
**Traces to:** FR-14 (proposed, `04-Process-Maps.md` Section 10; Scope-Decisions-and-Limitations-Log, 4 Sept 2026)
**Status:** **Proposed — not yet in BRD.** Included in this backlog at Gagana's explicit decision (28 Sept 2026) so the epic is visible for future planning, but must not be pulled into a sprint or counted toward this engagement's committed scope until formally added via a BRD v3 revision.

**Story:**
As a maintenance technician closing out a work order, I want a smaller, mutually-exclusive list of cause codes that actually match what happened, so that I stop defaulting to "other" and the real failure mechanism gets captured.

**Acceptance Criteria (draft — pending validation before this story can be considered testable):**
1. Given the current ~40-option cause-code dropdown, when redesigned, then the replacement list is small enough and specific enough that a technician can select an accurate option without defaulting to "other" or a near-miss category.
2. Given AI4I's five-failure-mode taxonomy (TWF/HDF/PWF/OSF/RNF), when the new cause-code list is designed, then it is explicitly cross-checked against that taxonomy for a sensible mapping — not designed in isolation from the data model the rest of this backlog depends on.
3. Given this is a CMMS platform change, when scoped, then a CMMS/IT system owner has validated feasibility — the same open gap already named for FR-05 through FR-08 (Section 13.9), not yet closed for this proposed requirement either.

**Notes:**
- Source: Maintenance Superintendent – Fixed Plant, Q2; Scope-Decisions-and-Limitations-Log, "New requirement surfaced during process mapping — FR-14 (proposed)," 4 September 2026.
- This is the one story in the backlog with genuinely provisional acceptance criteria — they're written to the same Given/When/Then discipline as every other story so the format stays consistent, but they should be revisited once (and if) FR-14 is formally adopted into the BRD, since a real requirements conversation with the CMMS/IT owner could reasonably change what "small enough" or "sensible mapping" actually means in practice.

---

## Traceability note (for Day 18's full matrix)

Every BRD functional requirement (FR-01 through FR-13) has at least one corresponding story above; none were left out and none were invented without a BRD source. FR-01 and FR-06 each produced multiple stories (three and two, respectively) because the underlying requirement genuinely serves multiple distinct use cases or has a formally separated minimum-bar/stretch-goal split in the BRD itself — this is a deliberate one-to-many mapping, not scope inflation. FR-14 is the one exception: included as US-17 despite not yet being a numbered BRD requirement, clearly labeled as such, per Gagana's explicit decision to keep the backlog visible rather than silently omit a requirement already identified and under consideration. The full BRD → story → (eventual) test-case matrix is Week 3, Day 18's dedicated deliverable (`10-Traceability-Matrix.xlsx`) and will reference this document directly rather than duplicate its content here.
</content>
