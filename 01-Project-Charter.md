# Project Charter — Maintenance Reliability Reporting Enhancement

**Document status:** v5 — Sponsor title clarified: **"Project Sponsor,"** not "Executive Sponsor" (role and person unchanged — still the Operations Superintendent). Resolves the organisational-seniority sub-item raised in Appendix F. See Appendix G.
**Prepared by:** Gagana Suresh, Business Analyst
**Date:** 20 August 2026
**Simulated client:** Corvus Resources Ltd

> **Disclosure:** Corvus Resources Ltd is a fictional, composite organisation invented for this simulated engagement. It is not based on, and should not be inferred to represent, any real ASX-listed or private mining company. All figures, stakeholders, and quotes in this and related documents are synthetic or clearly-labelled assumptions unless a public source is cited. See `data/data-lineage-note.md` for the underlying dataset's real provenance.

## Revision History

| Version | Date | Change |
|---|---|---|
| v1 | 20 Aug 2026 | Initial draft |
| v2 | 20 Aug 2026 | Revised following principal-BA red-team review — see Appendix A for findings and Appendix B for the change log |
| v3 | 21 Aug 2026 | Objectives (§2) and Success Criteria (§4) rebuilt around the finalized Diagnose → Explain → Act business questions, each made measurable and traceable; scope (§3) tightened to distinguish statistical threshold-testing from ML model-building; revised following a second red-team pass — see Appendix D for findings and Appendix E for the change log |
| v4 | 1 Sept 2026 | Governance split confirmed: Operations Superintendent as Executive Sponsor, Maintenance Manager as Accountable Business Owner. Resolves the open sponsor-ambiguity item raised in `02-Stakeholder-Register.md` §5. Affects §3 (two-tier change control), §4 (O0 and O6 sign-off), §5 (governance table replaces the single-sponsor line), §11 (approval block). See Appendix F |
| v5 | 4 Sept 2026 | Sponsor title changed from "Executive Sponsor" to "**Project Sponsor**" — same person/role (Operations Superintendent), title only, resolving the seniority-inversion sub-item Appendix F left open. Affects §3, §4 (O6), §5, §11. See Appendix G. **Does not resolve** the separate, still-open question of whether "Operations Superintendent" and the interviewed "Mining/Operations Manager" role are the same individual — see Appendix G |

## 1. Business Background

Corvus Resources operates a single open-pit gold mine and processing plant (the "Kestrel Pit" operation) in the WA Goldfields, running a mixed mobile and fixed-plant fleet (haul trucks, excavators, crushers, conveyors, pumps). Over the past two reporting periods, unplanned equipment downtime has increased, and the Operations Leadership Team has raised concerns that the maintenance function cannot currently explain, in a single report, which asset classes, failure modes, or shifts are driving the loss. Maintenance data exists in the site's CMMS, but reporting is manual, inconsistent between planners, and does not support root-cause or trend analysis.

## 2. Project Objectives

Structured as a **Diagnose → Explain → Act** narrative. Every objective below is traceable to one finalized business question and one success criterion in Section 4 — none are freestanding.

**Foundational (process/requirements — supports all tiers below):**
- O0: Understand and document the current breakdown-to-repair process and its reporting gaps; define the business and functional requirements for an enhanced maintenance reliability reporting capability; deliver a data model and prototype dashboard demonstrating it.

**Tier 1 — Diagnose (quantify the problem):**
- **O1** *(Q: How much production time and cost is being lost to unplanned breakdowns?)* — Quantify total unplanned-downtime hours and associated cost lost across the historical data period.
- **O2** *(Q: Which one or two failure modes, via Pareto analysis, account for the majority of that loss?)* — Identify, via Pareto analysis, which one or two failure modes account for the largest share of total downtime/cost.

**Tier 2 — Explain (why, and where):**
- **O3** *(Q: Which asset tier drives the highest failure rate and cost — does it justify differentiated maintenance investment?)* — Determine which asset criticality tier (Low/Medium/High) has the highest failure rate and cost impact, and assess whether the evidence justifies differentiated maintenance investment.
- **O4** *(Q: What proportion of failures are mechanically preventable versus inherently random?)* — Quantify the proportion of failures that are mechanically explainable (TWF/HDF/PWF/OSF) versus inherently random (RNF), and state the limits of that distinction given the dataset's construction.

**Tier 3 — Act & Prevent (recommendation + forward view):**
- **O5** *(Q: Is there a torque/tool-wear threshold that predicts overstrain risk clearly enough to justify a proactive replacement policy?)* — Test whether a torque/tool-wear threshold predicts overstrain (OSF) risk with enough statistical strength to justify a proactive replacement-policy recommendation.
- **O6** *(Q: Which failure modes show detectable precursor patterns that could enable early warning?)* — Identify which failure modes show detectable sensor precursor patterns, as an input to a scoped, future-phase predictive-maintenance recommendation. **This is a diagnostic finding, not a commitment to build or validate a predictive model in this engagement** — see Section 3.

## 3. Scope

**In scope:** the maintenance reporting and analysis process for the mobile fleet and the maintenance-critical fixed-plant assets (primary crusher, main conveyor line, process water pumps) at the Kestrel Pit site; requirements for enhanced downtime, failure-mode, and cost reporting; a **standalone prototype dashboard** built against a static extract of historical data (explicitly not a live, CMMS-integrated production tool — see Out of Scope); a benefit-realization business case.

**Out of scope:** replacement or reconfiguration of the underlying CMMS platform itself; live/real-time integration of the prototype dashboard into any production system; **building, training, or validating a machine-learning predictive model** (out of scope for this engagement — flagged as a candidate future-phase recommendation in the benefit realization report per Objective O6). For clarity, this is distinct from Objective O5, which is in scope: testing a simple, pre-defined statistical threshold rule against historical data is descriptive analysis, not model-building, and does not cross this boundary; safety incident reporting (tracked separately, referenced only for context); non-maintenance-critical fixed-plant assets not listed above; rostering and workforce management; sites other than Kestrel Pit.

**Scope variation / change control:** any request to extend scope beyond the boundaries above will be logged in the Assumptions Log and assessed for schedule and effort impact by the **Accountable Business Owner (Maintenance Manager)**, who recommends accept or reject. Material variations — anything altering the objectives in Section 2, the phase durations in Section 10, or the boundaries above — additionally require **Project Sponsor (Operations Superintendent)** approval before work begins. No scope addition is actioned informally at either level.

## 4. Success Criteria

Each objective in Section 2 is met only when its stated criterion is satisfied **and** the named reviewer has signed off — "the analysis exists" is not sufficient on its own. Where a criterion involves judgement (e.g. "does this justify investment?"), the threshold for that judgement is fixed here, in advance, so it cannot be quietly adjusted to fit whatever the data turns out to say.

**Foundational:**
- **O0 met when:** a BRD is formally signed off by the Accountable Business Owner (content and requirements) and accepted by the Project Sponsor at the Phase 1 gate; the prototype dashboard reconciles 100% against the underlying dataset; every functional requirement in the BRD has a corresponding test case and dashboard element in the traceability matrix, with zero orphaned requirements at hand-over.

**Tier 1 — Diagnose:**
- **O1 met when:** total unplanned-downtime hours and $ cost for the full historical period are reported, with the $/hour rate and its source (real published benchmark or explicit, labelled assumption) documented in the Assumptions Log before the figure is used anywhere else. *Reviewed by: Finance/Cost Controller.*
- **O2 met when:** a Pareto ranking of all five failure modes by downtime/cost contribution is produced and the top 1–2 modes' share of total loss is explicitly stated as a percentage. Success is the rigor and completeness of the ranking and its methodology (including how multi-failure rows are handled — see O4), **not** any predetermined percentage needing to be hit. *Reviewed by: Reliability Engineer.*

**Tier 2 — Explain:**
- **O3 met when:** failure rate and cost are reported per asset tier (L/M/H) side by side, **and** the business case states an explicit yes/no recommendation on differentiated investment, judged against a materiality threshold agreed *before* the analysis is run (e.g., "a failure-rate gap of X percentage points or more between tiers is considered material") rather than decided after seeing the result. *Reviewed by: Reliability Engineer and Finance/Cost Controller.*
- **O4 met when:** the report states the % of total failures attributable to each of TWF/HDF/PWF/OSF individually and to RNF; explicitly documents how multi-flag rows (a failure triggering more than one mode) are counted so the percentages don't overstate the total; and includes an explicit caveat that "random" reflects this dataset's own labelling convention (and its known internal inconsistencies — see the data quality findings), not an independently verified real-world failure taxonomy. *Reviewed by: Reliability Engineer.*

**Tier 3 — Act & Prevent:**
- **O5 met when:** the specific torque/tool-wear threshold(s) tested are stated, together with a statistical bar for "predictive enough" that is defined *before* the analysis runs (e.g., a target precision/recall or hit-rate figure), and a clear go/no-go recommendation on a proactive replacement policy follows from it. A bare correlation, without a pre-agreed bar and a stated recommendation, does not meet this criterion. *Reviewed by: Reliability Engineer.*
- **O6 met when:** each failure mode is classified as detectable / not detectable / inconclusive for sensor precursor patterns, and the finding is written up strictly as an input to a future-phase recommendation in the Benefit Realization Report — not presented as, or implying, a built or validated predictive model. *Reviewed by: Reliability Engineer (technical) and Project Sponsor (scope boundary check against Section 3 — this is a sponsor-level call because it guards the engagement's outer boundary, not a within-scope delivery decision).*

## 5. High-Level Stakeholders

**Governance roles (split confirmed 1 September 2026; sponsor title clarified 4 September 2026 — see Appendix G):**

| Role | Held by | Authority |
|---|---|---|
| **Project Sponsor** *(retitled from "Executive Sponsor," same person/role — see Appendix G)* | Operations Superintendent | Commissions the engagement and provides its mandate; approves material scope variations (Section 3); accepts the project at each phase gate and at close; escalation point for cross-functional blockers between Maintenance and Operations |
| **Accountable Business Owner** | Maintenance Manager | Owns the business outcome and the downtime/cost KPIs the project moves; signs off deliverable content (BRD, requirements, business case); assesses and recommends on scope variations; accountable for benefit realization after hand-over |

The split reflects where authority actually sits: the Operations Superintendent commissions the work because unplanned downtime lands on production, while the Maintenance Manager owns the budget, the scorecard, and the decisions four of the six business questions feed (see `02-Stakeholder-Register.md` §3). Sponsor approves *whether the work continues and within what boundary*; Business Owner approves *what the work says*.

**Other key stakeholders:** Reliability Engineer (primary technical SME), Maintenance Planner, Maintenance Superintendent – Mobile, Maintenance Superintendent – Fixed Plant, Financial Controller, Processing Manager, CMMS/IT System Owner, Instrumentation & Controls Engineer, HSE Manager. Full register with power/interest tiering follows as a separate deliverable (`02-Stakeholder-Register.md`).

*Note added v5 (4 Sept 2026): this list, deliberately kept high-level in the charter, does not use the title "Mining/Operations Manager" anywhere — see Appendix G for why this is relevant to a still-open naming question and should not be over-read as resolving it.*

## 6. Key Deliverables

Stakeholder register; business requirements document; as-is/to-be process maps; data dictionary; reliability dashboard prototype; cost-of-downtime business case; benefit realization report; requirements traceability matrix; job-fit matrix (portfolio-specific — see Appendix C).

## 7. Assumptions

The site's CMMS is assumed to be a mid-tier platform with basic work-order logging but no cross-asset reporting or dashboarding capability. Historical maintenance and sensor data is assumed to be available in a structure comparable to the dataset used in this project (Section 9). **These assumptions carry real risk if incorrect and will be explicitly revisited at the Phase 2 kickoff**, not treated as settled facts — see the Assumptions Log for the full register and validation status of each one.

## 8. Constraints

No access to a real client or real CMMS export exists for this simulated engagement; synthetic/adapted public data is used throughout, as disclosed above. See Appendix C for how the portfolio-project context (as distinct from the simulated client engagement itself) is handled — it is kept out of the client-facing body of this document by design.

## 9. Data & Confidentiality Note

Underlying operational data is adapted from the AI4I 2020 Predictive Maintenance Dataset (UCI Machine Learning Repository), a real but generic industrial dataset, re-skinned onto a synthetic Corvus Resources asset register. This adaptation is fully documented in the data lineage note.

## 10. High-Level Timeline

| Phase | Focus | Duration |
|---|---|---|
| Phase 1 | Discovery & Requirements (charter, stakeholder register, BRD) | ~1 week |
| Phase 2 | Process & Data Design (process maps, data dictionary, data prep) | ~1 week |
| Phase 3 | Build (dashboard, business case, user stories, test cases) | ~1 week |
| Phase 4 | Benefit Realization, Traceability & Sign-off | ~1 week |

## 11. Approval

| Role | Name | Sign-off |
|---|---|---|
| Project Sponsor (simulated — Operations Superintendent) | — | Pending |
| Accountable Business Owner (simulated — Maintenance Manager) | — | Pending |
| Business Analyst | Gagana Suresh | v2 submitted for sign-off |

---

## Appendix A — Principal BA Critique Log (Red-Team Pass)

**Technique:** Role/persona prompting + critique loop.

**Prompt used:**
> "You are a principal Business Analyst with 15+ years in mining and resources engagements, reviewing a junior BA's draft project charter before it goes to a client sponsor for sign-off. You are direct and slightly skeptical — your job is to catch what will bounce back from the sponsor, not to be encouraging. Review the attached charter specifically for: (1) ambiguity — any statement a sponsor could reasonably read two different ways, (2) missing or unmeasurable success criteria — anything not specific, measurable, and time-bound, (3) scope creep risk — any boundary not tightly drawn enough to stop 'while you're at it' requests later. For each issue, quote the exact charter text, state what's wrong, and state what you'd demand before signing off. Do not soften the feedback."

**Findings against v1:**

1. **Success criteria (old Section 4)** — "will be considered successful if it delivers X" describes *deliverables*, not measurable *outcomes*. No baseline, target, or timeframe. Demand: rewrite as testable pass/fail conditions.
2. **Scope boundary (old Section 3)** — "mobile and fixed-plant equipment" doesn't say *which* fixed-plant assets. An unbounded fixed-plant scope on a real site could mean dozens of asset types. Demand: name the specific assets in scope.
3. **Prototype deliverable ambiguity** — nothing states whether the dashboard is a static demonstration or expected to become a live production tool. This is the single most common source of "can you just also hook it up to..." scope creep. Demand: state explicitly that it's a standalone, non-production prototype.
4. **Predictive maintenance not addressed** — the sensor data (tool wear, temperature) makes an ML failure-prediction ask highly likely from an engaged Reliability Engineer stakeholder. Silence in the out-of-scope list isn't the same as excluding it. Demand: name it explicitly as out of scope for this phase.
5. **No change-control mechanism** — nothing in v1 says what happens when someone asks for more once the charter is signed. This is the biggest scope-creep gap of the whole document. Demand: an explicit scope-variation clause.
6. **Assumptions treated as settled facts** — v1 lists assumptions but never says what happens if they're wrong, or when they'll be checked. Demand: a validation checkpoint.
7. **No accountable decision-maker named** — the charter lists stakeholders but never says who actually has authority to approve a scope change or sign off success criteria. Demand: name the Project Sponsor explicitly.
8. **Portfolio-project framing bleeding into client-facing content (old Section 8)** — mixing "this is a self-imposed portfolio timeline" language into what should read as a professional client artifact undermines credibility for anyone reading it as a work sample. Demand: separate the meta-context from the charter body.
9. **Timeline has no durations (old Section 10)** — phases with no effort estimate can't be held accountable to a schedule. Demand: add indicative durations.

## Appendix B — v1 → v2 Change Log

| Finding # | Change made in v2 |
|---|---|
| 1 | Section 4 rewritten as 4 testable, sponsor-verifiable conditions |
| 2 | Section 3 now names the specific in-scope fixed-plant assets |
| 3 | Section 3 explicitly labels the dashboard a standalone, non-production prototype |
| 4 | Section 3 out-of-scope list now explicitly names predictive/ML failure prediction |
| 5 | Section 3 adds an explicit scope-variation/change-control clause |
| 6 | Section 7 adds an explicit assumption-validation checkpoint at Phase 2 kickoff |
| 7 | Section 5 names the Operations Superintendent as Project Sponsor with sole scope authority |
| 8 | Section 8 now points to Appendix C instead of embedding portfolio-context language in the client-facing body |
| 9 | Section 10 timeline now carries indicative durations per phase |

## Appendix C — Note on Project Format (portfolio context, kept separate from the client-facing charter body per Finding 8)

This charter is one deliverable within a self-directed portfolio project simulating a BA engagement in the mining sector, built to demonstrate professional-standard BA work and disciplined use of AI (Claude) as an analytical collaborator. The "Job-Fit Matrix" deliverable referenced in Section 6 is a portfolio-specific artifact (not something a real client would receive) mapping this project's deliverables to real, current Perth mining/resources BA job requirements — see the project's Master Plan for detail.

## Appendix D — Principal BA Critique Log, Round 2 (Objectives & Success Criteria)

**Technique:** Role/persona prompting + critique loop, re-run specifically against the rebuilt §2/§4 once the business questions were finalized.

**Prompt used:**
> "You are a principal Business Analyst reviewing a junior's project charter before client sign-off. The Objectives and Success Criteria sections have just been rewritten around six finalized business questions. Red-team specifically for: (1) ambiguity, (2) missing or unmeasurable success criteria, (3) scope-creep risk. Be direct."

**Findings against the v3 draft (before the fixes now reflected in the body above):**

1. **O1's cost figure had no committed methodology.** The objective demands a $ cost figure, but nothing said where the $/hour rate would come from or who'd validate it — the exact kind of number a Finance stakeholder disputes at sign-off. Fixed: O1's success criterion now requires the rate and its source to be documented in the Assumptions Log *before* it's used anywhere else.
2. **O2's "majority of that loss" presupposes the answer.** If the top two failure modes only account for 40%, does the objective simply fail? A charter shouldn't pre-commit to a specific data outcome it doesn't yet know. Fixed: success redefined as the rigor of the ranking and methodology, not a percentage threshold.
3. **O3's "justify differentiated investment" is a judgement call with no defined bar.** Without a materiality threshold fixed in advance, it's tempting to declare "yes, justified" or "no, not justified" after seeing the numbers, which isn't a defensible finding. Fixed: success criterion now requires the materiality threshold to be agreed before the analysis runs.
4. **O4 treats RNF as a clean stand-in for "inherently random," but we already found it isn't clean.** The earlier data-quality check found 18 rows where RNF=1 but the overall Machine failure flag is 0 — RNF doesn't behave as a fully consistent category in this dataset. Presenting the preventable-vs-random split without that caveat would overstate confidence in the finding. Fixed: O4's criterion now explicitly requires disclosing the multi-flag handling and RNF's own labelling limitations.
5. **O5's "clearly enough to justify a policy" is unfalsifiable as written.** Without a pre-agreed statistical bar, any correlation could be argued as "clear enough" after the fact — this is the same spurious-correlation risk flagged for the Week 4 safety module in the Master Plan, and it applies here too. Fixed: success criterion now requires the statistical bar to be defined before the analysis runs, and a bare correlation explicitly does not qualify.
6. **O6 risks contradicting Section 3's existing out-of-scope clause on predictive/ML work.** "Detectable precursor patterns... early warning" reads, to a stakeholder skimming quickly, like a commitment to build a predictive capability — exactly the kind of language that invites "great, so let's build it" mid-engagement. Fixed: O6 now states explicitly, in the objective itself (not just in Section 3), that it's a diagnostic finding and not a model-building commitment; Section 3 was also tightened to distinguish threshold-testing (in scope) from ML model-building (out of scope).
7. **No objective named who signs off that it's actually met.** Six new objectives were added with no accountable reviewer per objective, which quietly reopens the "who has authority" gap that v2 had already closed at the whole-charter level. Fixed: every objective in Section 4 now names a specific reviewer role.

## Appendix E — v2 → v3 Change Log

| Finding # | Change made in v3 |
|---|---|
| 1 | O1 success criterion requires rate + source documented in Assumptions Log before use |
| 2 | O2 success criterion redefined around ranking rigor, not a percentage outcome |
| 3 | O3 success criterion requires a pre-agreed materiality threshold |
| 4 | O4 success criterion requires disclosure of multi-flag handling and RNF's labelling limitations |
| 5 | O5 success criterion requires a pre-agreed statistical bar; a bare correlation explicitly insufficient |
| 6 | O6 objective statement and Section 3 both now explicitly separate threshold-testing (in scope) from ML model-building (out of scope) |
| 7 | Every objective (O0–O6) now names an accountable reviewer role in Section 4 |

## Appendix F — v3 → v4 Change Log (governance split)

**Trigger:** `02-Stakeholder-Register.md` §5 flag 1 — the charter named the Operations Superintendent as sole scope authority, but the decision-driven stakeholder pass showed the Maintenance Manager owns the budget, the KPI, and the primary decision on four of the six business questions. Flagged as an open item requiring a deliberate decision rather than a silent merge; resolved 1 September 2026.

**Decision:** split the role rather than reassign it — Operations Superintendent as Executive Sponsor, Maintenance Manager as Accountable Business Owner.

| Section | Change |
|---|---|
| §3 | Change control is now two-tier: Business Owner assesses and recommends on all variations; Sponsor approval additionally required for material variations (objectives, phase durations, or scope boundaries) |
| §4, O0 | BRD sign-off split — Business Owner signs off content and requirements; Sponsor accepts at the Phase 1 gate |
| §4, O6 | Scope-boundary check named as a Sponsor-level call, with the reason stated (it guards the engagement's outer boundary, not a within-scope delivery decision) |
| §5 | Single-sponsor line replaced with a governance table defining both roles and their distinct authority, plus the reasoning for the split |
| §11 | Approval block now carries both signatories |

**Rejected alternative:** reassigning sole sponsorship to the Maintenance Manager. Rejected because unplanned downtime lands on production, not maintenance — a maintenance-only mandate would leave the engagement without standing to ask Operations for equipment access, production data, or schedule impact, which is precisely the cross-functional friction a sponsor exists to resolve.

**Open sub-item — organisational seniority.** On a conventional mine-site structure, an Operations Superintendent reports to the Mining/Operations Manager, who sits at the same level as the Maintenance Manager. As written, the Sponsor is therefore junior to the Business Owner, which inverts the usual sponsor/owner relationship. Two clean resolutions, either defensible: (a) elevate the Sponsor to Mining/Operations Manager or General Manager, keeping the Superintendent as a Manage-Closely stakeholder; or (b) retain the Operations Superintendent but describe the role as "Project Sponsor" rather than "Executive Sponsor," which carries no seniority implication. Parked for decision before the BRD draft (Week 1, Day 4).

## Appendix G — v4 → v5 Change Log (sponsor title clarified; charter brought into the project workspace)

**Context — why this appendix exists now.** This charter file (v4) was drafted in a separate work session on 1 September 2026 and was, until 4 September 2026, not present in this Project's shared workspace — `Scope-Decisions-and-Limitations-Log.md` and `02-Stakeholder-Register.md` both explicitly flagged it as missing and unable to be reconciled directly. Gagana uploaded it on 4 September 2026, after the BRD (v1) had already been drafted using the log's paraphrased record of Appendix F rather than this source document directly. Cross-checking confirms the log's paraphrase was accurate — Appendix F above matches what the log recorded, including the exact two fix options and the "parked for decision before the BRD draft" instruction. No retroactive correction to the BRD is needed on this point; this appendix documents bringing the source of truth in and closing the loop.

**Trigger:** the "Open sub-item — organisational seniority" left open at the end of Appendix F, above. On 3 September 2026 — before this charter file itself was available, working only from the log's record of it — Gagana chose fix **option (b)**: retain the Operations Superintendent as the person/role, change only the title, from "Executive Sponsor" to "**Project Sponsor**," to remove the unintended implication that the role sits at the top of the site's org chart. Rationale (recorded in `Scope-Decisions-and-Limitations-Log.md`): option (a) would have required inventing a more senior stakeholder who was never interviewed or scoped into this engagement — a change to *who* holds the role, not just its title — while option (b) is a smaller, more honest fix that corrects the title's implied seniority without pretending a different person was involved.

| Section | Change |
|---|---|
| Header / Revision History | Status line and history table updated to v5 |
| §3 | "Executive Sponsor" → "Project Sponsor" in the material-scope-variation approval clause |
| §4, O6 | Reviewer role renamed "Project Sponsor" |
| §5 | Governance table's sponsor row retitled "Project Sponsor," with an inline note that this is the same person/role as before; a note added flagging that this section's stakeholder list does not use the title "Mining/Operations Manager" anywhere (see below) |
| §11 | Approval block's sponsor row retitled "Project Sponsor" |

**What this charter's arrival does — and does not — resolve.** Bringing this file into the workspace closes the specific gap both the log and the register flagged ("charter not yet available for direct reconciliation"). It does **not** resolve the separate identity question those two documents also carry: whether "Operations Superintendent" (this charter's language throughout) and "Mining/Operations Manager" (the title used in `02-Stakeholder-Register.md` row 7 and in `Interview-Transcript-Operations-Manager.md`) refer to the same individual. This charter's own Section 5 stakeholder list is worth noting as new, relevant evidence: it never uses the title "Mining/Operations Manager" at all — it names "Processing Manager" as a separate stakeholder but has no equivalent line for a "Mining/Operations Manager." That is consistent with either reading (the charter's list is explicitly high-level and defers to the full register for completeness, so an omission here is not conclusive either way) and does not tip the balance established in the register's 3 September 2026 partial-evidence note (which leans toward the Operations Manager persona being senior enough to sit above a Superintendent, based on his own "head office" and "board pack" language). **Status: still open.** Closing it with confidence would require either a real org chart (which this simulated engagement does not have) or an explicit editorial decision to simply declare the two titles equivalent for this portfolio project's purposes — a decision only Gagana can make, and one that does not need to be made before the BRD, since the BRD's governance section (Section 16) already correctly treats this as a separate, still-open question that doesn't block sign-off authority either way.
