# 08 — Test Cases & UAT Scenarios: Maintenance Reliability CMMS Reporting Enhancement

**Project:** Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability (mining fleet + fixed-plant maintenance function)
**Prepared by:** Gagana Suresh, Business Analyst
**Source documents:** `07-User-Stories.md` (every test case below traces to a specific story's acceptance criterion) and, through it, `03-BRD-Maintenance-Reporting.md` Section 15's own acceptance criteria.
**Date:** 30 September 2026
**Status:** DRAFT — ready for UAT planning. As with the user stories they're derived from, several test cases are explicitly marked **Not yet executable** because the underlying story is Blocked in `07-User-Stories.md` — writing a test case for a requirement doesn't make it ready to run, and pretending otherwise would misrepresent UAT readiness the same way marking a Blocked story "Ready" would have.

---

## How to read this document

**Technique used (for the prompt library):** chain-of-thought traceability mapping, plus a deliberately separate edge-case-generation pass — two distinct techniques, not one, per the Master Plan's Week 3 Day 15 specification.

The traceability mapping works by reasoning explicitly, for each acceptance criterion, from what the criterion actually asserts to what a tester would need to do to prove or disprove it — rather than jumping straight to a plausible-sounding test. The worked examples immediately below show this reasoning step made visible, exactly once for a "core" functional AC and once for a data-integrity AC, before the full test case table applies the same reasoning silently across the remaining `07-User-Stories.md` acceptance criteria.

The edge-case pass is separate and intentional: after mapping every acceptance criterion to a straightforward "happy path" test, a second pass was run asking specifically what unusual, boundary, or malformed scenario each requirement is technically supposed to handle but that no acceptance criterion explicitly describes. This is where most of this project's own real defects have actually been found before (the OSF-undercount bug, the RNF/Machine-failure mismatch) — so the edge cases below aren't generic QA examples, they're grounded in this project's own documented data-quality findings.

**Format legend:**
- **Traces to** — the exact `07-User-Stories.md` story and acceptance-criterion number(s) this test case proves.
- **Type** — Functional (happy path), Edge case (unusual/boundary input), Negative (proves the system correctly refuses or omits something), or Process (a sign-off/workflow check, not a system behavior).
- **Status** — Executable (ready for UAT once the feature is built) or **Not yet executable** (cites the exact `07-User-Stories.md` Blocked/Proposed reason it inherits).

---

## Worked examples — chain-of-thought traceability, shown explicitly

### Example 1 — from a functional acceptance criterion to a test case

**Acceptance criterion (US-01, AC1):** *"Given an asset with logged failure history, when I select that asset from the asset list, then I can choose a trailing window of exactly 6, 12, or 24 months (no other window options are presented)."*

**Reasoning:** The criterion actually makes two separate claims bundled into one sentence — (a) three specific windows must be selectable, and (b) no other window may be offered. A test that only checks claim (a) would pass a system that also, incorrectly, offers a 3-month or "custom" option, which FR-01 explicitly does not call for. So the test needs to verify presence of the three required options *and* absence of any other option — a completeness check, not just an existence check. This is also a case where "no other window options" is only checkable by looking at the full selector, not by testing one selection at a time.

**Resulting test case (TC-001):** Open the asset-history view for any asset with logged failures. Inspect the window selector control. Expected result: exactly three options are present, labeled 6, 12, and 24 months; no additional option (e.g., "custom," "all time," "3 months") exists anywhere in the control.

### Example 2 — from a data-integrity acceptance criterion to a test case

**Acceptance criterion (US-14, AC3):** *"Given RNF's documented labeling-inconsistency caveat (rows where RNF is set independently of the overall failure flag), when RNF's percentage is displayed, then this caveat is shown alongside it, not only in a separate methodology document."*

**Reasoning:** This criterion is really testing a specific historical failure mode of this exact system: the Scope-Decisions-and-Limitations-Log documents 18 real rows where `RNF = 1` but `Machine failure = 0`, and the standing rule is that these are excluded from failure counts under the "Machine failure is authoritative" source-of-truth rule. A naive test would just check that *a* caveat exists somewhere in the documentation. The acceptance criterion is stricter than that — it requires the caveat to be visible *at the point of display*, not filed away in a separate doc a user would have to go looking for. So the test needs to load the actual RNF percentage tile and check what's on that specific screen, not audit the documentation set separately.

**Resulting test case (TC-039, an edge case in its own right):** Using the known 18-row RNF/Machine-failure mismatch in the underlying dataset, load the preventable-vs-random split view. Expected result: (1) the 18 mismatched rows are excluded from the displayed RNF failure count, consistent with the source-of-truth rule; (2) a caveat referencing this exclusion is visible on the same screen as the RNF percentage, not only in a linked or separate document.

---

## Full test case set

### Epic 1 — Asset-Level Cumulative Rollup (US-01, US-02, US-03)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-001 | US-01 AC1 | Must | Functional | Open asset-history view; inspect window selector | Exactly 6/12/24-month options present, no others (see worked example above) | Executable |
| TC-002 | US-01 AC2, US-02 AC1 | Must | Functional | Select each window on an asset with known failure/cost history | Running total (count, and $ where tier is in scope) matches the underlying work-order data for that exact window | Executable |
| TC-003 | US-01 AC3 | Must | Functional | Select a window on an asset with a known month-over-month change | Month-over-month % change figure and linear trend indicator (up/flat/down) both display and match hand-calculated values | Executable |
| TC-004 | US-01 AC4, US-03 AC1 | Must | Functional | From a displayed monthly total, click into that month | Drill-down shows the exact work order(s) that sum to that month's total, per NFR-03 | Executable |
| TC-005 | US-01 AC5 | Must | Functional | Inspect the view's on-screen title/label | View is labeled "Asset History" (or equivalent shared-decision-support framing) — not "Worst Offenders" or any ranked-league-table framing | Executable |
| TC-006 | US-02 AC2 | Should | Functional (UX) | Open the view for 10+ assets in sequence, timed | Trend indicator is scannable at a glance across multiple assets in one sitting — verified by UX review, not a pass/fail numeric check | Executable |
| TC-007 | US-02 AC3 | Must | Negative | Attempt to open the view using an Operations-only login with no Maintenance-system credential | Access succeeds without requiring a Maintenance-team credential or handoff | Executable |
| TC-008 | US-02 AC4 | Must | Functional | Drill down from the Operations-facing view and from the Maintenance-facing view on the same asset/month | Both surface identical underlying work orders — one shared source of truth, not two views that could drift apart | Executable |
| TC-009 | US-03 AC1 | Must | Functional | From the work-order approval screen, attempt to reach the asset rollup | Rollup is reachable without leaving the approval workflow | Executable |
| TC-010 | US-03 AC2 | Must | Functional | View an asset with 3+ work orders in the selected window | Repeat work orders against the same asset are visually distinguished from one-off events (e.g., a repeat-count indicator) | Executable |
| TC-011 | US-03 AC3 | Must | Functional | Drill into a work order figure from the Financial Controller's view; compare to ERP figure for the same item | Figures reconcile within the tolerance to be agreed under BRD Section 17, Action 3 | **Not yet executable** — tolerance not yet defined (BRD Section 17, Action 3 still open) |
| TC-012 *(edge case)* | US-01 AC2 | Must | Edge case | Select any window on an asset with **zero** logged failures in that period | Running total displays cleanly as 0 (count and $), with no error, blank screen, or divide-by-zero artifact in the trend/% calculation | Executable |
| TC-013 *(edge case)* | US-01 AC1–AC3 | Must | Edge case | Select the 12- or 24-month window on an asset that has been in service for **less than 6 months** | System does not fabricate history for the un-elapsed period; the view either clearly labels the partial-coverage period or disables/annotates the window options that exceed the asset's actual service life — it must not silently show a misleadingly "empty-looking" full window as if 12 months of clean data were confirmed | Executable |

### Epic 2 — Failure-Mode Pareto (US-04)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-014 | US-04 AC1 | Must | Functional | Open the Pareto view | Failure modes ranked by event count using the primary-cause (mutually exclusive) rule; ranking sums to the known 339-failure total | Executable |
| TC-015 | US-04 AC2 | Must | Functional | Open the Pareto view where Medium/Low-tier cost data is in scope | Cost-weighted ranking displayed side by side with the count ranking — two visibly separate lists, not one blended score | Executable |
| TC-016 | US-04 AC4 | Must | Negative | Compare the count ranking and cost ranking where they disagree on "worst" mode | Neither list is visually marked as the authoritative answer (no "winner" badge, no single combined score) | Executable |
| TC-017 *(edge case)* | US-04 AC3 | Must | Edge case | Load the Pareto view against the known dataset where OSF was previously undercounted due to multi-flag tie-breaking (the real 10 Sept 2026 bug) | Both primary-cause count (78) and true-occurrence count (98) are visible for OSF, with the 20-event gap explicitly stated — this is a regression test against a defect that has already occurred once in this exact system | Executable |

### Epic 3 — Asset-Tier Segmentation (US-05)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-018 | US-05 AC1 | Must | Functional | Open the tier view | Failure rate shown for all three tiers, rounded to whole numbers (not 2 decimal places) per Section 13.11 | Executable |
| TC-019 | US-05 AC2 | Must | Functional | Open the tier view; inspect the High-tier row | Medium/Low tiers show a $ figure; High tier shows frequency only, with its one-line disclosed reason visible inline (not blank) | Executable |
| TC-020 | US-05 AC3 | Must | Negative | Inspect the tier view for any investment recommendation language or "recommended tier" flag | None present — the view displays figures only; no investment judgment is rendered by the system | Executable |

### Epic 4 — Confidence & Traceability Disclosure (US-06)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-021 | US-06 AC1 | Must | Functional | Inspect any reported figure across the reporting capability | A visible badge/icon (not a footnote or tooltip-only mechanism) reads Dataset-derived, Cited source, or Labeled assumption | Executable |
| TC-022 | US-06 AC2 | Must | Functional | Interact with a "Cited source" or "Labeled assumption" badge | Specific benchmark/source shown (e.g., "RS/IMechE 2023 UK/Ireland survey, ~£5,000/hr") | Executable |
| TC-023 | US-06 AC3 | Must | Functional | Use the drill-down control on any figure | Underlying work order(s) reached | Executable |
| TC-024 | US-06 AC4 | Must | Negative (full audit) | Systematically audit every screen in the reporting capability for untagged figures | Zero figures found without one of the three tags — this is a structural completeness check across the whole system, not a sample | Executable |

### Epic 5 — CMMS Data Capture & Process (US-07 through US-13)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-025 | US-07 AC1 | Must | Negative | Attempt to submit a new work order with the planned/unplanned flag left blank | Submission is blocked; flag is enforced as required | **Not yet executable** — pending BRD Section 17 Actions 1 & 2 |
| TC-026 *(edge case)* | US-07 AC2 | Must | Edge case | Raise a work order that spans both a planned inspection and an unplanned failure on the same asset (the exact scenario that produced the Financial Controller's real ~5-hour overstatement) | Two separate durations are captured, one per activity type — not one combined duration defaulted to "unplanned" | **Not yet executable** — pending BRD Section 17 Actions 1 & 2 |
| TC-027 | US-07 AC3 | Must | Process | Review the current mandatory-field count on the close-out form before and after this change | Net mandatory-field count unchanged, or explicit frontline sign-off recorded | **Not yet executable** — pending BRD Section 17 Action 1 |
| TC-028 | US-08 AC1–AC2 | Must | Functional | Flag a work order as "reassigned mid-repair"; recalculate its duration | Dead time between reassignment and return is excluded/separated from recorded repair duration | **Not yet executable** — pending BRD Section 17 Actions 1 & 2 |
| TC-029 | US-08 AC3 | Must | Functional | Run UAT against FR-06 using only the reassignment flag, without live timestamp capture | Minimum bar passes on its own — US-09's stretch goal is confirmed as not required for this pass/fail | **Not yet executable** — same blocking gap as TC-028 |
| TC-030 | US-09 AC1–AC2 | Should | Functional | Start and stop a repair on a platform confirmed to support live timestamps | Start/stop times logged automatically, no manual backfill required | **Not yet executable** — pending Section 17 Action 2 (platform feasibility unconfirmed) |
| TC-031 *(boundary)* | US-10 AC1 | Should | Edge case | Hold a sensor reading at "amber" for exactly **2** consecutive review cycles | No automatic escalation triggers — 2 cycles is below the 3-cycle threshold | **Not yet executable** — pending Section 17 Action 4 |
| TC-032 *(boundary)* | US-10 AC1 | Should | Functional | Hold the same reading at "amber" through a **3rd** consecutive cycle | Automatic flag/scheduling prompt triggers exactly at the 3rd cycle, not before | **Not yet executable** — pending Section 17 Action 4 |
| TC-033 | US-10 AC3 | Should | Process | Confirm deployment sequencing against US-16 (precursor-pattern expansion) | Escalation rule (US-10) is live before or alongside any expansion of alert volume — verified as a release-planning check, not a runtime test | Executable (as a release-checklist item) |
| TC-034 | US-11 AC1 | Should | Functional | View a condition-monitoring reading for a sensor with a known calibration date | Last verified calibration date displayed alongside the reading | Executable |
| TC-035 *(edge case)* | US-11 AC2 | Should | Edge case | View a reading from a sensor with **no calibration date ever recorded** | Field explicitly shows "calibration not recorded" — not a blank cell a user could misread as "recently calibrated" | Executable |
| TC-036 | US-11 AC3 | Should | Functional | Compare two similar-looking sensor trends, one with stale calibration and one current | A reviewer can correctly identify which is more trustworthy using the calibration field alone | Executable |
| TC-037 | US-12 AC1–AC2 | Should | Functional | Complete a work-order close-out form | Optional "suspected contributing factor" field present, visually distinct from the failure-mode field, labeled non-disciplinary | **Not yet executable** — Blocked pending Operations-side review (Risk 7) |
| TC-038 | US-12 AC3 | Should | Process | Check release records for this feature | Feature has not been released to build without a recorded Operations-side sign-off | **Not yet executable** — same block as TC-037; this is the gating check itself |
| TC-039 | US-13 AC1–AC2 | Should | Functional | Compare a High-tier asset's treatment in the reporting capability vs. parallel monthly cost reporting | Both show frequency-only treatment with matching one-line disclosed-reason wording — no contradiction | Executable |

### Epic 6 — Preventable vs. Random Failure Split (US-14)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-040 | US-14 AC1 | Must | Functional | Open the explainability view | % of failures per TWF/HDF/PWF/OSF/RNF displayed | Executable |
| TC-041 | US-14 AC2 | Must | Functional | Inspect a multi-flag failure event in the view | Display states plainly whether it's counted as primary-cause or true-occurrence, not silently picking one | Executable |
| TC-042 *(edge case, worked example above)* | US-14 AC3 | Must | Edge case | Load the view against the known 18-row RNF/Machine-failure mismatch | Mismatched rows excluded from RNF's displayed count per the source-of-truth rule; caveat visible on the same screen | Executable |

### Epic 7 — Precursor & Threshold Analysis (US-15, US-16)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-043 | US-15 AC1 | Should | Functional | Open the torque/tool-wear threshold view | Tested threshold(s) and statistical result against Charter O5's bar displayed | Executable |
| TC-044 | US-15 AC2 | Should | Negative | Inspect the view's labeling | Explicit on-screen label states this demonstrates a method on AI4I data, not a production-deployable claim for this site's real fleet | Executable |
| TC-045 | US-15 AC3 | Should | Functional | Trace the same finding as it appears in the dashboard and business case | Same production-readiness caveat travels with it in every location, not only the originating view | Executable |
| TC-046 | US-16 AC1 | Should | Functional | Open the precursor-pattern view | Each failure mode classified detectable/not detectable/inconclusive | Executable |
| TC-047 | US-16 AC2 | Should | Negative | Inspect the view's behavior when a mode is classified "detectable" | View does not itself trigger an escalation action or require a calibration check to render — display only | Executable |
| TC-048 | US-16 AC3 | Should | Functional | Inspect a "detectable" mode's display | Same drift-vs-genuine-trend caveat as US-15 AC2 appears alongside it | Executable |

### Epic 8 — Cause-Code Taxonomy Simplification (US-17, proposed)

| TC | Traces to | Priority | Type | Test summary | Expected result | Status |
|---|---|---|---|---|---|---|
| TC-049 | US-17 AC1–AC3 | Unprioritized | Functional | Review the proposed cause-code list against real close-out scenarios | Technicians can select an accurate option without defaulting to "other"; list is cross-checked against AI4I's five-mode taxonomy | **Not yet executable — Proposed, not yet in BRD.** This test case is provisional and must be revisited once (and if) FR-14 is formally adopted; do not count toward UAT completion for the current engagement scope. |

---

## Edge & boundary case summary

The Master Plan calls for 2–3 edge cases a less careful analyst would miss, generated as a deliberate, separate pass rather than folded quietly into the main traceability mapping. This document produced seven, each grounded in a real, already-documented finding from this project rather than a generic textbook example:

1. **Zero-failure asset (TC-012)** — a "successful" outcome (nothing broke) must not be mistaken for a broken calculation. A naive running-total or percentage-change formula can produce a null, an error, or a nonsensical divide-by-zero result exactly when the news is good.
2. **Asset with less than the window's full service life (TC-013)** — a straightforward test only ever selects a window the asset has fully lived through. Nobody's asset register is uniformly old; a newly registered haul truck exists on day one and must not display a misleadingly "clean" 24-month history it hasn't had time to earn.
3. **Multi-flag OSF undercount (TC-017)** — this isn't hypothetical; it's a regression test against the exact tie-break bug found and fixed in the Day 9 SQL layer (10 Sept 2026). Any future change to the Pareto logic risks reintroducing it silently.
4. **Split planned/unplanned work order (TC-026)** — the precise real incident that damaged the Financial Controller's trust in a downtime figure (Section 2, BRD). If FR-05 is built to only capture one flag per work order, this exact failure mode recurs by design.
5. **Boundary testing on the amber-escalation threshold (TC-031/TC-032)** — testing only "well past the threshold" and "well before it" misses the actual failure mode of an off-by-one bug. Testing at cycle 2 (must not fire) and cycle 3 (must fire) is what actually proves the boundary condition is implemented correctly, not just approximately.
6. **Sensor with no calibration date recorded at all (TC-035)** — distinct from "sensor has a stale calibration date." A missing value that renders identically to a blank field is the specific failure mode the Instrumentation & Controls Engineer's interview warned about — indistinguishable from "recently and reliably calibrated" unless explicitly labeled otherwise.
7. **RNF/Machine-failure mismatch (TC-042, worked example)** — a known, disclosed data-quality finding (18 rows) with a defined handling rule; the risk is a future build silently reverting to counting these rows the "obvious" way instead of per the documented source-of-truth exception.

---

## Traceability coverage check

Every acceptance criterion across all 17 user stories in `07-User-Stories.md` maps to at least one test case above; no story's acceptance criteria were left uncovered. Coverage gaps that exist are not test-design gaps but inherited blocking gaps — 10 of the 49 test cases (TC-011, TC-025 through TC-030, TC-031/TC-032, TC-037/TC-038, TC-049) are written and ready but marked **Not yet executable**, tracking exactly the same Blocked/Proposed statuses already disclosed in `07-User-Stories.md`. This document does not attempt to resolve those gaps — that's Section 17 of the BRD's job — it only makes sure the eventual UAT pass has a test case waiting the moment each gap closes, rather than needing test design done from scratch at that point.

The full BRD → User Story → Test Case matrix, cross-referenced against dashboard elements, is Week 4, Day 4's dedicated deliverable (`10-Traceability-Matrix.xlsx`) and will consume this document's TC numbering directly rather than re-deriving it.
</content>
