# 02 — Stakeholder Register

**Project:** Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability (mining fleet + fixed-plant maintenance function)
**Owner:** Gagana Suresh
**Status:** v1.1 — locked 1 September 2026; governance model resolved 1 September 2026
**Data note:** All roles below are synthetic, drawn from realistic mining-site org structures — no real company or individual is represented. Named per the project's data-integrity rule (Master Plan §1.2 / Scope-Decisions-and-Limitations-Log).

---

## 1. Methodology

Two independent techniques were used and then cross-checked against each other, rather than relying on one pass:

**Technique A — Chain-of-thought lifecycle walk-through.** Reason through the breakdown-to-repair work-order lifecycle end-to-end first, then derive every role that touches each step. This is the technique specified in the Master Plan (Week 1, Day 2) and catches operational/process stakeholders — the people who *do* the work.

**Technique B — Decision-driven stakeholder mapping.** For each of the six locked business questions (Scope-Decisions-and-Limitations-Log, "FINAL business question set"), ask "whose decision changes once this question is answered?" rather than "who touches the process?" This catches analytical/governance stakeholders that a pure process walk-through misses — people who never touch a work order but who use the *answer*.

Running both and comparing the results is itself the point: Technique A over-indexes on frontline/operational roles, Technique B over-indexes on people who consume outputs. Where a role appears in both, it's a strong signal of centrality; where a role appears in only one, that's worth noting explicitly rather than silently merging the lists. (Log this dual-technique triangulation in the prompt library — it's a reusable pattern beyond this project.)

---

## 2. Technique A — Process Lifecycle Walk-Through

| Step | What happens | Roles that touch this step |
|---|---|---|
| 1. Failure occurs / detected | Asset breaks down or an operator notices abnormal performance | Equipment Operator, Production/Mine Dispatch Coordinator |
| 2. Breakdown reported & logged | Fault is called in and captured as a record | Equipment Operator, Dispatch Coordinator, CMMS Owner (system of record) |
| 3. Work order raised & triaged | Fault is converted into a work order and assessed for urgency | Maintenance Planner, Maintenance Superintendent (Mobile or Fixed Plant, by asset type) |
| 4. Prioritized & scheduled | Work is slotted against other jobs and production's equipment-access windows | Maintenance Planner, Maintenance Superintendent, Production/Dispatch Coordinator |
| 5. Diagnosed | Root symptom identified before repair starts | Maintenance Technician/Fitter, Condition Monitoring Technician, Reliability Engineer (complex/recurring cases) |
| 6. Repaired | Physical repair executed | Maintenance Technician/Fitter, Supply & Logistics Superintendent (parts availability) |
| 7. Returned to service | Asset handed back and accepted | Maintenance Supervisor, Mining/Operations Manager or Processing Manager (accepting party, by asset type) |
| 8. Root cause analysis (significant/repeat failures) | Why it happened, not just what broke | Reliability Engineer, Maintenance Planner |
| 9. Closed out & data captured | Work order closed, failure mode and cost recorded in the CMMS | CMMS Owner, Maintenance Planner |
| 10. Reported & reviewed | Downtime, cost, and KPI trends rolled up | Maintenance Manager, Asset Manager (corporate), General Manager, Financial Controller |
| 11. Strategy & continuous improvement | Findings feed maintenance strategy, spares policy, monitoring investment | Reliability Engineer, Maintenance Manager, Asset Manager (corporate), Digital/Automation Lead |

**Roles this method surfaces that the decision-driven method (Section 3) does not:** Equipment Operator, Maintenance Technician/Fitter, Maintenance Supervisor, Dispatch Coordinator (as a scheduling actor rather than a data consumer). These are frontline execution roles — real stakeholders, but ones whose *day-to-day work* changes as a result of this project rather than their *decisions*. They're carried into the register below as a distinct tier rather than dropped.

---

## 3. Technique B — Decision-Driven Stakeholder Mapping

For each locked business question, the roles whose decision, budget, or accountability actually changes based on the answer (not just "who might find this interesting").

**Q1 — How much production time and cost is lost to unplanned breakdowns?**
Maintenance Manager (this is the number his performance is scored against), Financial Controller (it lands in the monthly cost report), Mining/Operations Manager and Processing Manager (downtime is lost production against their own targets), General Manager (rolls it up to head office), Asset Manager – corporate (site-to-site comparison), Mine Planning Engineer (schedules assume equipment availability).

**Q2 — Which failure modes account for the majority of the loss (Pareto)?**
Reliability Engineer (sets improvement priorities), Maintenance Superintendent – Mobile and Maintenance Superintendent – Fixed Plant (each directs their own crew's effort), Maintenance Planner (builds the repair schedule around it), Supply & Logistics Superintendent (spares stocking), Financial Controller (wants spend targeted at the real loss driver).

**Q3 — Does asset-tier failure rate/cost justify differentiated maintenance investment?**
Asset Manager – corporate and Maintenance Manager (own the investment decision directly), Financial Controller (funds it), Mine Planning Engineer (schedules around whichever tier gets prioritized), Reliability Engineer (supplies the technical justification).

**Q4 — What proportion of failures is mechanically preventable vs. inherently random?**
Reliability Engineer (chooses strategy — fix root causes vs. accept the randomness), Maintenance Manager (can't promise a target uptime number if failures are genuinely random), Financial Controller (budgets contingency for unavoidable breakdowns), General Manager (sets realistic expectations upward), a corporate maintenance-strategy role (standardizes this thinking across sites), HSE Manager (unpredictable failures carry safety risk, not just cost).

**Q5 — Is there a torque/tool-wear threshold that justifies proactive replacement?**
Reliability Engineer (sets the rule), Maintenance Planner (turns it into scheduled work), Maintenance Superintendent – Mobile (mostly applies to fleet assets, executes the work), Supply & Logistics Superintendent (stocks more parts if replacement moves earlier), Financial Controller (weighs part cost against downtime cost avoided), Production/Dispatch Coordinator (prefers planned downtime to a surprise breakdown), Condition Monitoring Technician (does the physical checking).

**Q6 — Which failure modes show detectable sensor precursor patterns (early warning)?**
Reliability Engineer (decides what gets monitored and what counts as a warning), Condition Monitoring Technician (a new warning changes his daily routine), Instrumentation & Controls Engineer (owns the sensors themselves — without reliable instrumentation none of this is possible), Maintenance Manager (approves spend), Digital/Automation Lead (would build any resulting tool), CMMS Owner (decides how a warning becomes a work order), Production/Dispatch Coordinator (only if a warning needs an immediate operational response).

**What this method surfaces that Technique A does not:** the Financial Controller, General Manager, Asset Manager (corporate), and Instrumentation & Controls Engineer never appear in the process walk-through at all — they don't touch a work order, but every one of them owns a decision this project's output feeds directly. Instrumentation & Controls Engineer in particular was **not on the original stakeholder longlist** before this pass — flagged and added below, since Q6 (and the optional ML module) has no usable data without them.

---

## 4. Governance model — resolved 1 September 2026, title clarified 3 September 2026

The decision-driven analysis in Section 3 surfaced a real inconsistency: the project charter names the Operations Superintendent as sole sponsor, but the Maintenance Manager is the actual decision-owner on four of the six business questions. Three options were weighed (leave as-is; hand sponsorship fully to Maintenance; split the role) — full trade-off discussion in the Scope-Decisions-and-Limitations-Log. **Decision: split sponsor model**, locked by Gagana 1 September 2026:

- **Project Sponsor — Operations Superintendent.** Commissions the engagement, holds final go/no-go authority, primary point of cross-functional escalation. (Represented in the register below by the Mining/Operations Manager row, #7 — see naming note.) **Title clarified 3 September 2026:** this role is titled "Project Sponsor," not "Executive Sponsor" — see the resolution note below and the Scope-Decisions-and-Limitations-Log's governance decision entry for the full reasoning.
- **Accountable Business Owner — Maintenance Manager (#1).** Owns the budget and the KPI the project is built to move; holds day-to-day sign-off authority on the BRD, the business case, and the CMMS reporting-enhancement requirements.

**Naming note, still open — charter now available, question still not settled.** The charter's "Operations Superintendent" and this register's existing "Mining/Operations Manager" (#7) are treated as the same function for this decision, on the assumption that a Superintendent reports to a Manager on a typical mine-site org chart. **`01-Project-Charter.md` was brought into the project workspace 4 September 2026 (now at v5) — see its Appendix G.** Direct reconciliation was possible for the first time, and did not settle the question: the charter's own §5 high-level stakeholder list never uses the title "Mining/Operations Manager" anywhere (it separately names "Processing Manager," with no equivalent line for a Mining/Operations Manager). This is consistent with either reading — the charter's list is explicitly non-exhaustive and defers to this full register — so it neither confirms nor overturns the partial evidence below. **Partial evidence added 3 September 2026:** the Mining/Operations Manager interview (`Interview-Transcript-Operations-Manager.md`) never uses the title "Operations Superintendent" and describes him reporting directly to "head office" and writing lines for "the board pack" — consistent with a genuinely senior, board-adjacent role and leaning toward fix option (a) in the Scope-Decisions-and-Limitations-Log's open sub-item (elevate the Sponsor / keep the Mining/Operations Manager senior to an Operations Superintendent). **Status as of 4 September 2026: still open.** Closing it with full confidence would need a real org chart, which this simulated engagement doesn't have; the alternative is an explicit editorial decision by Gagana to simply declare the two titles equivalent for this portfolio's purposes. Not required before BRD sign-off — `03-BRD-Maintenance-Reporting.md` Section 16 already treats this as a separate question that doesn't block either role's sign-off authority.

**Title question resolved separately, 3 September 2026:** rather than wait on the charter to resolve the seniority-inversion concern, Gagana chose to retitle the role "Project Sponsor" instead of "Executive Sponsor" (Scope-Decisions-and-Limitations-Log fix option b), keeping the Operations Superintendent as the person in the role. This removes the implication that the sponsor sits at the very top of the org chart, so the title no longer overstates the role regardless of how the identity question above is eventually resolved. The identity question itself (whether "Operations Superintendent" and "Mining/Operations Manager" are the same person) remains open and unaffected by this change — it still needs `01-Project-Charter.md` for direct reconciliation.

---

## 5. Consolidated Register

Tiered using the standard Power/Interest (Mendelow) grid: **Manage Closely** (high power, high interest — engage directly, involve in sign-off), **Keep Satisfied** (high power, lower day-to-day interest — summary updates, escalate only material findings), **Keep Informed** (high interest, lower power — detailed updates, no sign-off authority), **Monitor** (lower power, lower interest — light-touch, informed at milestones only).

| # | Stakeholder (role) | Department | Surfaced by | Power/Interest tier | Why they're a stakeholder | Engagement approach |
|---|---|---|---|---|---|---|
| 1 | Maintenance Manager | Maintenance | A + B | Manage Closely | Owns the maintenance budget and is scored on the downtime/cost outcome this project quantifies. Holds the **Accountable Business Owner** role under the governance model resolved 1 Sept 2026 (Section 4) | Direct engagement at every milestone; day-to-day sign-off authority on the BRD, business case, and reporting-enhancement requirements |
| 2 | Reliability Engineer | Maintenance (Reliability) | A + B | Manage Closely | Every one of the six business questions either sets his priorities or changes his technical strategy — the single most central role in the register | Direct engagement throughout; primary technical SME for interviews, RCA, and threshold/precursor analysis |
| 3 | Maintenance Planner | Maintenance | A + B | Manage Closely | Converts every finding (Pareto, preventable-failure split, threshold policy) into the actual work-order schedule | Direct engagement; consulted on process maps and schedule-impact of recommendations |
| 4 | Maintenance Superintendent – Mobile Fleet | Maintenance | A + B | Manage Closely | Directs crew effort on haul trucks/excavators; owns execution of most Q2/Q5 findings | Direct engagement; interview subject |
| 5 | Maintenance Superintendent – Fixed Plant | Maintenance | A + B | Keep Satisfied | Directs crew effort on crushers/mill/conveyor/thickener — but this is also the asset class where the project has the *least* quantified answer (frequency only, no cost figure — see Scope-Decisions-and-Limitations-Log, Option B) | Direct engagement; findings framed honestly around the fixed-plant data gap rather than a forced dollar figure |
| 6 | Financial Controller (site) | Finance | A + B | Keep Satisfied | Owns the monthly cost report and approves the business case's dollar figures; only truly decision-making on the cost/investment questions (Q1, Q3, Q5), not centrally involved elsewhere | Milestone updates; direct sign-off only on the business case |
| 7 | Mining/Operations Manager | Operations | A + B | Manage Closely | Downtime is lost production against his own target; asset return-to-service runs through operations. Holds the **Project Sponsor** role under the governance model resolved 1 Sept 2026, title clarified 3 Sept 2026 (Section 4) — commissions the engagement and holds final go/no-go authority | Direct engagement; interview subject; sponsor briefing at each milestone gate |
| 8 | Processing Manager | Processing/Plant | A + B | Manage Closely | Same as above for fixed-plant throughput; most affected by the fixed-plant data gap alongside Superintendent (fixed plant) | Direct engagement; interview subject |
| 9 | General Manager (site) | Site leadership | B | Keep Satisfied | Reports the headline downtime number to head office; sets expectations using the preventable-vs-random split (Q4) | Executive summary at milestones only; not involved in day-to-day working sessions |
| 10 | Asset Manager (corporate) | Corporate | B | Keep Satisfied | Compares this site's downtime/cost performance against other sites; owns the tier-differentiated investment decision (Q3) | Milestone summaries; consulted on Q3 recommendation specifically |
| 11 | Supply & Logistics Superintendent | Procurement/Supply | A + B | Keep Informed | Spares stocking decisions follow directly from the Pareto (Q2) and threshold-replacement (Q5) findings | Informed at findings stage; consulted before the proactive-replacement recommendation is finalized |
| 12 | HSE Manager | HSE | B | Monitor | Appears on only one question (Q4 — unpredictable failures carry safety risk) — genuinely a secondary stakeholder here, not a central one. Kept on the register (and the project charter treats HSE as prominent) but deliberately **not** tiered as high-influence for this specific project, to avoid over-stating their role | Informed at milestones; no working-session involvement unless a safety-relevant finding emerges |
| 13 | Instrumentation & Controls Engineer | Maintenance / Engineering | B (newly identified) | Keep Informed | Owns the sensors the entire Tier 3 analysis (Q5, Q6) and the optional ML module depend on — without reliable instrumentation there is no data to analyze. **Not on the original longlist; added as a direct result of the Q6 decision-driven pass** | Consulted specifically on data-quality/instrumentation reliability for Tier 3 findings |
| 14 | Condition Monitoring Technician | Maintenance | A + B | Keep Informed | Physically performs the condition-monitoring checks that Q5/Q6 findings would change | Informed of new monitoring routines resulting from findings |
| 15 | CMMS Owner / IT Systems Administrator | IT / Maintenance Systems | A + B | Keep Informed | Owns the system of record; any reporting-enhancement recommendation is built on top of what the CMMS can actually capture | Consulted on the CMMS reporting-enhancement requirements specifically (Week 3 user stories) |
| 16 | Mine Planning Engineer | Mine Planning | A + B | Keep Informed | Schedules assume equipment availability — a real downtime number changes planning assumptions | Informed at the Q1/Q3 findings stage |
| 17 | Digital/Automation Lead | Digital/IT | B | Monitor | Would build any tool arising from the early-warning finding (Q6) or the optional ML module — relevant only if that scope is reached | Informed only if the optional ML/precursor-monitoring recommendation proceeds |

**Frontline execution roles — tracked as a group, not individually registered:** Equipment Operator, Maintenance Technician/Fitter, Maintenance Supervisor, Production/Mine Dispatch Coordinator. These surfaced only through the lifecycle walk-through (Technique A) and represent the people whose daily work changes as a result of the to-be process redesign, rather than people who make decisions based on this project's findings. They belong in the process maps (Week 2, Day 6–7) as swimlane actors, not as individual register entries — registering four individual frontline roles at the same tier as the Maintenance Manager would overstate their decision-making stake and pad the register past the point of being useful. This is a deliberate scoping call, consistent with the "you don't answer every question you raise" principle already established in this project (Scope-Decisions-and-Limitations-Log).

---

## 6. Judgment calls and flags raised by this analysis

**1. Sponsor ambiguity — RESOLVED 1 September 2026, title clarified 3 September 2026.** The project charter framed the Operations Superintendent as sole sponsor, but the decision-driven analysis showed the Maintenance Manager as the actual decision-owner across four of the six business questions. Resolved via a split governance model (Section 4): Operations Superintendent as **Project Sponsor** (retitled from "Executive Sponsor" 3 Sept 2026 to remove an unintended seniority implication — see Scope-Decisions-and-Limitations-Log), Maintenance Manager as Accountable Business Owner. Full trade-off analysis of the three governance options, and of the two title-fix options, is logged in the Scope-Decisions-and-Limitations-Log. **Remaining action:** update `01-Project-Charter.md` to match, once that file is available in the project workspace, and confirm the "Operations Superintendent" / "Mining/Operations Manager" naming question (Section 4) — this is a separate, still-open question, unaffected by the title fix.

**2. HSE Manager's role is smaller than the charter implies.** They are kept on the register, but tiered as **Monitor** rather than high-influence, because in this specific scope (downtime/reliability, not a safety-incident engagement) they show up on only one of six business questions. This is disclosed rather than quietly downgraded, so it reads as a considered call, not an oversight.

**3. Fixed-plant stakeholders get the least quantified answer, and that's named honestly.** The Maintenance Superintendent – Fixed Plant and the Processing Manager both depend most on Tier 1/Tier 3 findings, but fixed-plant assets are exactly where the business case reports frequency only, with no cost figure (Scope-Decisions-and-Limitations-Log, Option B, locked 1 Sept 2026). The engagement approach for both roles is written to surface that gap as a finding in front of them, not obscure it.

**4. Instrumentation & Controls Engineer was missing from the original stakeholder longlist.** Only the decision-driven pass on Q6 caught this — the lifecycle walk-through never surfaces them because they don't touch a work order. Added as stakeholder #13. This is a concrete example of why the two techniques were run separately rather than jumping straight to one list, and is worth documenting in the prompt library as the "what I changed after reviewing it" evidence for this task's entry.

---

## 7. Cross-references

- Business question numbering (Q1–Q6) matches the FINAL locked set in `Scope-Decisions-and-Limitations-Log.md`.
- Fixed-plant cost-figure gap referenced in Sections 5/6 is fully explained in the same log's "DECISION — RESOLVED 1 September 2026: Option B" entry.
- Governance model in Section 4 is fully explained, with rejected alternatives, in the same log's "Sponsor/governance decision — RESOLVED 1 September 2026" entry.
- Frontline roles carried forward into the As-Is/To-Be process maps, `04-Process-Maps.md` (Week 2, Day 6–7).
- CMMS Owner and Instrumentation & Controls Engineer feed directly into `07-User-Stories.md` (Week 3, Day 14) for the CMMS reporting-enhancement requirements.
