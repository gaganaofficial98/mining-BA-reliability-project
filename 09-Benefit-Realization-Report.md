# 09 — Benefit Realization Report

**Project:** Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability (mining fleet + fixed-plant maintenance function)
**Prepared by:** Gagana Suresh, Business Analyst
**Version:** v1
**Status:** DRAFT — pending Reliability Engineer and Finance calibration of the illustrative savings range (Section 5); pending Accountable Business Owner and Project Sponsor review
**Date:** 30 September 2026
**Data note:** This engagement is a simulated portfolio project. The operational dataset is a real, published industrial dataset (AI4I 2020) re-skinned onto a synthetic mining asset register. All dollar figures in this report trace to `06-Business-Case.xlsx`, which is the source of truth for every number quoted below — this report interprets and frames that workbook's figures against a benefits-realization framework; it does not recompute them independently. See `Scope-Decisions-and-Limitations-Log.md` for the full data-lineage record and Section 8 of this report for every limitation carried forward.

**Related documents:** `00-Master-Plan.md` · `01-Project-Charter.md` (v5) · `03-BRD-Maintenance-Reporting.md` (v2) · `04-Process-Maps.md` · `06-Business-Case.xlsx` · `07-User-Stories.md` · `12-ML-Proof-of-Concept.md` (added 6 Oct 2026 — see Section 4.5) · `Scope-Decisions-and-Limitations-Log.md`

---

## 1. Purpose and Framework

### 1.1 Why a Benefits Dependency Network

This report does not simply list projected savings. It uses Ward & Daniel's **Benefits Dependency Network (BDN)** — a recognized benefits-realization framework from the benefits-management literature (Ward, J. & Daniel, E., *Benefits Management: Delivering Value from IS & IT Investments*, Wiley) — to show the causal chain a claimed benefit actually depends on, rather than asserting the benefit as a standalone fact.

The network is read left to right but **built right to left**: starting from each Investment Objective (Section 2, traced to `01-Project-Charter.md` Objectives O0–O6), the method asks four questions in sequence:

1. What **benefit** would tell us this objective has been achieved?
2. What **business change** — a change in how people actually work or decide — has to happen for that benefit to appear?
3. What **enabling change** — training, a new role, a policy, a data-quality fix — has to be in place before that business change is even possible?
4. What **IT/reporting enabler** — the specific system capability this project is building — has to exist before that enabling change can happen?

A benefit that skips straight from "we built a dashboard" to "we saved money," with no business change in between, is the single most common failure mode in real benefits cases — and it is exactly what Section 6's attribution critique exists to catch.

### 1.2 Why an attribution critique, and how it's run

Per the Master Plan's Day 16 instruction, this report stress-tests whether each claimed benefit is genuinely attributable to this project's recommended changes, or whether it is wishful attribution dressed up as analysis. **Technique used: attribution critique**, applied identically to every benefit in Section 4's network — not selectively to the ones that look weakest. Each benefit is scored for attribution confidence (High / Medium / Low) using three tests, stated once here rather than repeated for each benefit:

- **Mechanism test:** is there a specific, named business change that plausibly causes the benefit, or is the benefit just "better information exists, therefore things will improve"?
- **Counterfactual test:** could this benefit have occurred anyway, for a reason unrelated to this project (e.g., a commodity price shift changing the dollar figure, a supervisor coincidentally tightening reporting discipline)?
- **Evidence test:** is the benefit's magnitude backed by a dataset figure, a cited external source, or is it an unbenchmarked assumption carried over from `06-Business-Case.xlsx`'s own disclosure?

### 1.3 Note on this report's relationship to the Business Case workbook

`06-Business-Case.xlsx` was supplied directly on 30 September 2026 and read in full (all five tabs: Summary, Assumptions & Sources, Current-State Cost, Projected Savings, Limitations). Every dollar figure in Sections 3–5 below is quoted verbatim from that workbook's cells, with the source cell referenced. As a cross-check on data integrity (worth recording explicitly, not silently): before receiving the file, this report's author independently recomputed the same figures from the same locked benchmarks recorded in `Scope-Decisions-and-Limitations-Log.md` and `EDA-Findings.md`. The independent recomputation matched the workbook's actual cell values to the cent (e.g., $1,720,639.80 low-scenario mobile-fleet loss, both computed and actual). This is reported here as a genuine, if modest, integrity data point — a second, differently-derived path converged on the same number — not as proof the underlying benchmarks themselves are correct, which is a separate question Section 8 addresses.

---

## 2. Investment Objectives (traced to `01-Project-Charter.md` §2)

| Objective | Statement | Reviewer | Benefit tier this report addresses it under |
|---|---|---|---|
| O0 | Document the current process and reporting gaps; define requirements; deliver a data model and prototype dashboard | Accountable Business Owner + Project Sponsor | Foundational — Section 4.0 |
| O1 | Quantify total unplanned-downtime hours and cost lost | Finance/Cost Controller | Section 4.1 |
| O2 | Rank failure modes by downtime/cost share (Pareto) | Reliability Engineer | Section 4.2 |
| O3 | Determine which asset tier drives the highest failure rate/cost; assess differentiated-investment case | Reliability Engineer + Finance/Cost Controller | Section 4.2 |
| O4 | Quantify preventable vs. random failure proportion | Reliability Engineer | Section 4.2 |
| O5 | Test a torque/tool-wear threshold for a proactive replacement policy | Reliability Engineer | Section 4.3 (future-phase) |
| O6 | Identify failure modes with detectable sensor precursor patterns | Reliability Engineer + Project Sponsor | Section 4.3 (future-phase) |

Per the Charter's own success-criteria discipline (Section 4), this report does not treat "the analysis exists" as a benefit in itself. A benefit is only counted below where a named business change, distinct from the reporting output itself, converts the finding into an operational or financial outcome.

---

## 3. Quantified Financial Benefits — source: `06-Business-Case.xlsx`

### 3.1 Current-state annual loss (baseline)

| Metric | Value | Source cell | Tag |
|---|---|---|---|
| Mobile-fleet real failures | 83 of 339 (24.5% of the fleet) | `Current-State Cost'!B5` | DATASET |
| Mobile-fleet hours lost/yr | 182.6 hrs | `Current-State Cost'!D5` | DATASET × CITED SOURCE |
| Mobile-fleet $ loss — Low scenario | **$1,720,639.80 AUD/yr** | `Current-State Cost'!E5` | DATASET × CITED SOURCE × derived |
| Mobile-fleet $ loss — High scenario | **$6,500,103.50 AUD/yr** | `Current-State Cost'!F5` | DATASET × CITED SOURCE × derived |
| Fixed plant (High tier) | 21 failures — **frequency only, no dollar figure** | `Current-State Cost'!G6` | DATASET (frequency); dollar figure disclosed as absent, not zero |
| Ancillary (Low tier) | 235 failures — **frequency only, no dollar figure** | `Current-State Cost'!G7` | DATASET (frequency); dollar figure disclosed as absent, not zero |

**Coverage caveat, load-bearing:** only 24.5% of the fleet's 339 real failures carry a dollar figure. The remaining 75.5% (256 failures, including the fleet's single highest-criticality tier) are undisclosed cost, not zero cost. Every benefit below that is expressed in dollars is therefore a benefit against **less than a quarter of the fleet's actual failure volume** — this bounds every financial claim in this report and is restated in Section 8.

The ~3.8x spread between the Low ($9,423/hr) and High ($35,597.50/hr) scenarios reflects genuine cross-industry rate variance in the two cited general-industrial surveys (RS/IMechE 2023 UK/Ireland; MaintainX 2024 US) — neither is mining-specific, because no publicly verifiable mining-specific downtime-cost-per-hour figure exists. This range is carried through everywhere as a range, never collapsed to a single point estimate.

### 3.2 Projected annual savings — illustrative sensitivity range, Mobile fleet only

| Reduction scenario | Hours avoided/yr | Savings — Low rate | Savings — High rate | Source |
|---|---|---|---|---|
| 5% | 9.13 hrs | $86,031.99 | $325,005.18 | `Projected Savings'!row 5` |
| **10% (working-planning midpoint)** | **18.26 hrs** | **$172,063.98** | **$650,010.35** | `Projected Savings'!row 6` |
| 15% | 27.39 hrs | $258,095.97 | $975,015.53 | `Projected Savings'!row 7` |

**This range is explicitly NOT a cited benchmark.** The workbook's own Assumptions & Sources tab (row 14) and Limitations tab (item 5) state plainly that no defensible external source exists for this specific intervention type — a search returned only vendor-blog-level material, which this project's sourcing standard already treats as inadequate (the same standard that produced the Fixed-plant Option B and repair-cost-dropped decisions). **This report treats the 10% figure as a working-planning midpoint only, not a committed target, until the Reliability Engineer confirms a real figure against site experience and Finance signs off — per Charter Objective O3's own rule that a materiality threshold must be agreed in advance, not adjusted to fit the answer.** No business case slide, LinkedIn article, or video walkthrough should present $172,064–$650,010 as an achieved or promised saving; Section 6.3 stress-tests this range specifically.

### 3.3 What is not quantified, and why that matters more than what is

Repair cost (labour + parts) is excluded from every tier, for every scenario, in this workbook — not a rounding choice but a full scope decision, disclosed in the Financial Controller's own words (`06-Business-Case.xlsx`, Limitations item 1): *"This analysis does not include potential reductions in maintenance labour and parts cost, which represents additional unquantified upside."* Combined with the 75.5% frequency-only coverage gap (Section 3.1), the honest summary is: **this business case very likely understates the site's true downtime cost and the true addressable savings opportunity** — a defensible, conservative position, and one worth stating explicitly rather than letting the reported numbers read as the whole picture.

---

## 4. Benefits Dependency Network

Each row below is one dependency chain, read left to right, each benefit tagged with an attribution-confidence rating carried forward from Section 6.

### 4.0 Foundational chain (O0)

| IT/Reporting Enabler | Enabling Change | Business Change | Benefit | Investment Objective | Attribution confidence |
|---|---|---|---|---|---|
| Reliability dashboard prototype (FR-01–FR-04, FR-11); three-tag disclosure system | Stakeholders trained to read the dataset/cited-source/assumption tags and drill-down mechanic (NFR-03) | Leadership and Finance stop treating every downtime figure as equally certain; a "Dataset-derived" figure is trusted differently from a "Labeled assumption" one | Fewer disputed figures reaching a GM-level review unchallenged; the Financial Controller's own "false precision is the fastest way to lose my trust" standard (BRD §3) is directly addressed | O0 | High |

### 4.1 Cost-of-downtime visibility chain (O1)

| IT/Reporting Enabler | Enabling Change | Business Change | Benefit | Investment Objective | Attribution confidence |
|---|---|---|---|---|---|
| FR-01 asset-level cumulative rollup; FR-05 planned/unplanned flag at point of entry | Frontline/CMMS validation of FR-05 (BRD §17, Action 1 — **not yet done**) | Work-order entry captures planned vs. unplanned at the point of raising, not reconstructed after the fact | Elimination of the specific error class the Financial Controller caught manually (a ~5-hour planned inspection bundled into an unplanned-failure work order, BRD §2) | O1 | Medium — mechanism is direct, but depends on an enabling change (frontline validation) that has not yet happened |
| FR-01 asset-level rollup, drillable to source work orders | None required beyond system availability | Maintenance Manager stops manually eyeballing CMMS descriptions the night before a GM review (his own described practice, "plus or minus twenty, twenty-five percent" confidence — BRD §2) | Reduced report-preparation time and reduced risk of a materially wrong figure reaching leadership | O1 | Medium — plausible and specific, but not yet timed; see Section 7, KPI-04 |

### 4.2 Prioritization chain (O2, O3, O4)

| IT/Reporting Enabler | Enabling Change | Business Change | Benefit | Investment Objective | Attribution confidence |
|---|---|---|---|---|---|
| FR-02 dual-metric Pareto (count vs. true-occurrence); FR-11 preventable/random split | Reliability Engineer and Maintenance Superintendent – Fixed Plant both briefed on the dual-metric methodology (so neither metric is read as "the" answer to their standing disagreement — BRD §2) | Improvement effort and RCA prioritization is directed at HDF (34%) and OSF (28.9% true-occurrence) first, replacing the two stakeholders' competing gut-feel candidates (jaw crusher by count vs. mill by hours) | Maintenance effort targeted at the fleet's actual largest loss drivers, not the most memorable or most recently disruptive failure — directly countering the cognitive bias both the Mining/Operations Manager and the Maintenance Superintendent, Fixed Plant independently named in themselves (BRD §2) | O2 | Medium-High — the bias this counters is well-evidenced in the interviews; the size of the resulting efficiency gain is not separately quantified anywhere |
| FR-03 asset-tier segmentation view | Business-case-level materiality threshold agreed in advance (Charter O3) — **not yet set**; see Section 8 | Investment decisions move from "the tier that fails most often gets funded" (Ancillary, 3.92%) to "the tier that costs most per failure gets prioritized differently from the tier that fails most often" (Fixed plant is highest-consequence despite the lowest failure rate, 2.09%) | Avoided misallocation of maintenance investment toward the wrong tier | O3 | Low-Medium — the underlying tier-failure-rate finding is solid DATASET evidence, but O3's own success criterion explicitly requires a pre-agreed materiality threshold before any investment recommendation is defensible, and that threshold has not yet been set |
| FR-11 preventable/random split (97.3% preventable, primary-cause basis) | None required | General Manager and Maintenance Manager stop absorbing genuinely random failure risk into a performance target that assumes near-total preventability, or vice versa | More realistic uptime targets and contingency budgeting | O4 | Medium — the 97.3% figure is solid DATASET evidence; whether targets/budgets actually get revised is a downstream management decision this project cannot observe or guarantee |

### 4.3 Act & Prevent chain (O5, O6) — future-phase, not yet realized

| IT/Reporting Enabler | Enabling Change | Business Change | Benefit | Investment Objective | Attribution confidence |
|---|---|---|---|---|---|
| FR-12 torque/tool-wear threshold display; FR-13 precursor-pattern classification | FR-08 calibration-date logging against sensor ID (**not yet built**) — without this, a genuine precursor trend and sensor drift/fouling "look identical on a chart" (Instrumentation & Controls Engineer, BRD §13.3) | A proactive replacement policy or early-warning escalation rule is adopted in production | Avoided catastrophic overstrain failures; more of the "maybe a third" of condition-monitoring signal the Reliability Engineer estimates is currently missed (BRD §6, pain point 6) gets acted on | O5, O6 | **Not scored — explicitly not claimable yet.** This chain demonstrates a valid statistical method on AI4I's real sensor data (Charter O5/O6 success criteria); it is not a claim that any dollar or safety benefit currently exists, since the enabling change (calibration provenance) and the IT enabler beneath it (FR-08) are both unbuilt. Listed here for completeness of the network, not as a benefit this report is claiming |

### 4.4 Process-governance chain (Step 4 redesign, Option B — the source of Section 3.2's savings estimate)

| IT/Reporting Enabler | Enabling Change | Business Change | Benefit | Investment Objective | Attribution confidence |
|---|---|---|---|---|---|
| FR-01 asset-level rollup (evidence base) | Joint Maintenance Manager + Reliability Engineer sign-off workflow defined and adopted (Process Maps §8, Option B, locked 7 Sept 2026) | A further fast-fix on a repeat failure (same mode, same asset, within a defined window) requires documented joint sign-off before Production can proceed with another patch instead of a proper repair | Reduction in Mobile-fleet downtime hours from repeat patch-repairs that would otherwise recur — the illustrative 5/10/15% range in Section 3.2 | O1 (realized value) | **Low.** This is the report's single largest financial claim and its weakest-attributed one — see Section 6.3 for the full stress-test. The mechanism is plausible (repeat-failure escalation is a real lever), but the magnitude has no external benchmark, no pilot data, and depends entirely on whether the sign-off gate is actually enforced under production pressure — the same pressure Risk 1 in the BRD already names as capable of defeating better information on its own |

### 4.5 Phase-2 predictive-maintenance candidate (Module A — informational only, added 6 October 2026)

**This row is deliberately unscored, same discipline as 4.3, and for the same reason: nothing in it is claimable as a benefit of this engagement.** `12-ML-Proof-of-Concept.md` (Module A, an optional stretch module explicitly outside this engagement's locked scope per `01-Project-Charter.md` §3) built a general-purpose classifier on AI4I's five raw sensor readings — no hand-specified threshold rules, no per-mode engineering — and it independently rediscovered the same split the real Q5/Q6 analysis (Section 4.3) already found: strong, mechanistically explainable detection on OSF/PWF/HDF, and a complete blind spot on TWF, the one mode Q5/Q6 had already shown fails a 90%/90% precision bar.

| IT/Reporting Enabler | Enabling Change | Business Change | Benefit | Investment Objective | Attribution confidence |
|---|---|---|---|---|---|
| A single classifier (Random Forest, `class_weight='balanced'`), demonstrated outside this engagement's scope | None — this module was never built, validated, or deployed as part of this engagement; no enabling change exists | None — no production process currently acts on this model's output | **Not scored — informational corroboration only.** Two independently-derived methods (a hand-specified physical threshold rule, Section 4.3, and a general classifier with no access to that rule) landing on the same specific weak spot (TWF) and the same specific strengths (OSF/PWF/HDF) is modest evidence that Section 4.3's findings reflect a genuine property of the underlying failure mechanisms, not an artifact of how Q5/Q6's threshold rule happened to be specified. It is **not** evidence that a predictive-maintenance capability is ready to deploy, and it does not change Section 4.3's "not yet claimable" status | Informs O5/O6 only as corroborating evidence, not a new objective | **Not scored, same as 4.3 — explicitly not a benefit, a piece of corroborating evidence for 4.3's existing (also unscored) finding** |

**Why this belongs in the network at all, given it changes nothing:** omitting it would hide a genuine, if modest, data point — that the Act & Prevent chain's findings in 4.3 are not a one-off artifact of a single analysis method. Including it as explicitly unscored, rather than quietly upgrading 4.3's confidence rating because of it, keeps the distinction this report has maintained throughout: a second data point that happens to agree is corroboration, not validation, and the real blockers to claiming 4.3 (FR-08 calibration logging unbuilt, no longitudinal data) are entirely unaffected by Module A's existence.

---

## 5. Non-Financial and Intangible Benefits

Not every benefit belongs in a dollar column, and forcing one to fit there would be the same false-precision problem this project has avoided everywhere else.

**Decision-quality benefits.** The Reliability Engineer's root-cause analyses currently compete against production's ready-made tonnes-times-price argument with "a spreadsheet and a hunch" (BRD §2). FR-01's asset-level rollup gives that argument a defensible number for the first time. This is a genuine behavioral-leverage benefit, not a cost saving — it changes who wins an argument in a room, which is a real and legitimate benefit category in a BDN, distinct from and additional to Section 4.4's dollar claim.

**Credibility and audit-defensibility benefits.** FR-04's three-tag disclosure system and NFR-03's drill-down-to-source-work-order requirement directly answer the Financial Controller's stated non-negotiable standard (BRD §3, §9) and close the exact gap that let her crusher-work-order error go undetected until it was large enough to be visually obvious. This is a risk-reduction benefit: fewer undetected misstatements reaching a report she has to personally stand behind.

**Cross-functional visibility benefit, with an attached adoption risk.** FR-01 was requested, in isolation, by three different stakeholders for three different reasons (BRD §8.1) — but one of those reasons was explicitly "negotiating leverage... against Operations" (Maintenance Manager, Q8), which sits in direct tension with the same requirement's NFR-02 cross-functional-access goal. The benefit here (a shared, trusted asset history both teams can act on) is real but conditional on rollout framing (BRD Risk 6) — this is carried into Section 6 as a genuine attribution risk, not glossed over as automatically realized.

---

## 6. Attribution Critique — stress-testing every claimed benefit

Applying the three tests from Section 1.2 to each benefit chain in Section 4, in descending order of how confidently this report can claim them.

**6.1 High confidence — the three-tag disclosure benefit (4.0).** Mechanism: direct and specific (a visible badge that did not exist before now exists). Counterfactual: very low risk — no other change in this engagement could plausibly produce the same distinction between dataset-derived and assumption-based figures. Evidence: the tagging system itself is the DATASET/CITED SOURCE/ASSUMPTION discipline already enforced throughout every prior deliverable in this project, so its consistency is independently checkable, not just asserted. **Verdict: genuinely attributable to this project's specific requirement (FR-04), not a generic "better reporting helps" claim.**

**6.2 Medium confidence — the Pareto-prioritization and preventable/random benefits (4.2).** Mechanism: plausible and named (redirect effort from the most memorable failure to the most costly/frequent one). Counterfactual risk is real: a maintenance team could independently notice HDF is dominant without a dashboard, given enough time and manual effort — this project's actual contribution is making that finding fast, defensible, and disclosed with its multi-flag-handling caveat, not making it possible for the first time. Evidence: the underlying 34%/28.9% figures are solid DATASET evidence (cross-verified via the true-occurrence fix, EDA Findings §Q2), but the downstream benefit — better-targeted maintenance spend — is not separately measured anywhere in this project; it is inferred from the finding's quality, not observed as an outcome. **Verdict: attributable in direction, not yet in magnitude.**

**6.3 Low confidence — the Step 4 escalation-checkpoint savings estimate (4.4), the report's single largest dollar claim.** This is the chain this critique is most obligated to challenge rather than restate favorably, because it is also the number most likely to end up on a LinkedIn post or a resume bullet if it isn't handled carefully.

- *Mechanism test — partially fails.* The business change (mandatory joint sign-off on a repeat fast-fix) is a real, specific process change, not vague. But its success depends entirely on human compliance under exactly the production-pressure conditions this project's own discovery found already override sound RCA arguments today (BRD §6, pain point 5; BRD Risk 1). A sign-off requirement that gets rubber-stamped under pressure produces the paperwork of Option B without its substance.
- *Counterfactual test — fails outright for the magnitude.* There is no pilot, no A/B comparison, and no external benchmark for this specific intervention (the workbook's own Limitations item 5 says this explicitly). Mobile-fleet downtime hours could also fall for reasons entirely unrelated to this project — normal year-to-year variance, an unrelated fleet-age or maintenance-contract change, or a commodity-price-driven change in operating tempo (Limitations item 6/BRD §13.5) — and this project has no way to separate that from a genuine Option B effect, because no pre/post comparison against a real baseline is possible in a simulated, static-extract engagement.
- *Evidence test — explicitly fails by the workbook's own disclosure.* 5%/10%/15% is stated, in the source file itself, as an **illustrative sensitivity range, not a cited benchmark.** Treating $172,064–$650,010 as a "AI-driven savings" figure anywhere in this portfolio's external materials (README, video, LinkedIn) would misrepresent an unvalidated planning assumption as a delivered result — precisely the "fabricated or over-claimed" pattern this project's own standing instruction asks to be flagged and avoided.

**Recommended framing going forward:** describe this as *"a modeled savings range, pending Reliability Engineer and Finance validation — not a realized or committed figure,"* every time it is quoted, and never state a single point figure (e.g., never "$650K in savings") without both the range and the pending-validation caveat attached in the same sentence or slide.

**6.4 Not scored — the Act & Prevent chain (4.3).** As stated in Section 4.3, this chain's benefit cannot currently be claimed at all, in any confidence tier, because its enabling change (calibration-date logging, FR-08) has not been built. Including an unscored row in this network, rather than omitting the chain entirely, is a deliberate choice: it shows the full dependency path a real predictive-maintenance benefit would need, without pretending any part of that benefit exists today.

**6.5 Cross-cutting attribution risk — adoption is not guaranteed by capability.** Every benefit in Sections 4.0–4.2 assumes the dashboard is actually used the way FR-01–FR-04 intend. NFR-02/KPI-01 (BRD §9.1) already tracks this as a post-launch KPI rather than a go-live gate, for exactly this reason — a system's existence does not cause its use. This report inherits that same caution rather than assuming it away: Section 7's KPI set is built specifically to catch the gap between "the capability was delivered" and "the benefit was realized," rather than declaring victory at delivery.

---

## 7. KPIs to Track Post-Implementation

Extends `03-BRD-Maintenance-Reporting.md` §9.1's KPI-01, rather than duplicating it.

| KPI | What it measures | Baseline | Target / review point | Owner |
|---|---|---|---|---|
| KPI-01 (existing, BRD §9.1) | Operations visibly uses the reporting output, not just tolerates it | 0 (no shared tool exists today) | Assessed at 6 months post-launch | Maintenance Manager |
| KPI-02 — Escalation-checkpoint invocation rate | Number of repeat-failure events that actually trigger Option B's joint sign-off, vs. number of qualifying repeat failures | Not yet measurable (no baseline process exists today) | Tracked from go-live; a low invocation rate on qualifying repeats is an early warning that Section 6.3's compliance risk is materializing | Reliability Engineer |
| KPI-03 — Mobile-fleet downtime hours, actual vs. 182.6-hr baseline | Whether Mobile-fleet hours lost actually falls, and by how much, against the Section 3.1 baseline | 182.6 hrs/yr (Current-State Cost, this workbook) | Reviewed at 6 and 12 months; **any observed change must be checked against Section 6.3's counterfactual risks (fleet-age, contract, price/tempo shifts) before being attributed to Option B** | Financial Controller + Reliability Engineer |
| KPI-04 — Monthly downtime-report preparation time | Direct measure of the Section 4.1 report-preparation-time benefit, currently only qualitatively described | Not yet timed — the Maintenance Manager's own "9pm the night before" account is anecdotal, not a stopwatch figure | A real baseline timing should be captured before go-live specifically so this benefit can be measured, not just asserted | Maintenance Manager |
| KPI-05 — % of reported figures carrying an FR-04 disclosure tag | Direct measure of the disclosure/credibility benefit (Section 6.1) | 0% (today's ad hoc reporting has no tagging convention) | 100% at go-live (this is a build requirement, not an aspiration — FR-04 is a Must) | CMMS/IT reporting owner |
| KPI-06 — Finance/system reconciliation variance | Whether this system's figures and the Financial Controller's ERP figures stay within the tolerance AC-6 requires be agreed (BRD §17, Action 3 — **still open**) | Tolerance not yet set | Set before UAT sign-off; reviewed each reporting cycle thereafter (NFR-04) | Financial Controller |

---

## 8. Limitations Carried Forward Into This Report

This report inherits, and does not relitigate, the structural limitations already disclosed in `03-BRD-Maintenance-Reporting.md` §13 and `06-Business-Case.xlsx`'s Limitations tab. Restated here specifically because they bound what this Benefit Realization Report can honestly claim:

1. **Sub-threshold stoppages are structurally invisible** to any work-order-based analysis (BRD §13.2). Any downtime-hours benefit claimed anywhere in this report is a benefit against the *recorded* failure population only — a genuinely high-frequency, low-severity pattern below the CMMS reporting threshold could represent a larger true cost than anything this project's benefits can speak to.
2. **This project speaks to the equipment-attributable share of loss only** (BRD §13.1). None of this report's benefits should be read as claiming any effect on weather, blast-delay, or roster-driven production loss.
3. **75.5% of the fleet's real failures carry no dollar figure** (Section 3.1; Business Case Limitations item 2). Every dollar benefit in this report is scoped to less than a quarter of the fleet's actual failure volume — the fleet's highest-criticality tier (Fixed plant) is entirely excluded from every dollar figure quoted above.
4. **Repair cost (labour + parts) is excluded from every tier** (Business Case Limitations item 1). Every dollar benefit in this report is therefore conservative by construction with respect to that category — a real additional upside this project cannot quantify, not a benefit this report is claiming and simply rounding down.
5. **Precursor/threshold findings cannot currently be distinguished from sensor drift or fouling** (BRD §13.3) — the reason Section 4.3's chain is explicitly unscored rather than optimistically estimated.
6. **The projected-savings percentage (Section 3.2) is illustrative, not benchmarked** (Business Case Limitations item 5) — the single most important caveat in this entire report, restated a third time here deliberately, because it is the number most likely to be quoted out of context downstream (video walkthrough, LinkedIn, resume).
7. **This is a simulated engagement** using role-played stakeholder personas and a real, cited, but re-skinned public dataset — not real company data (BRD §13.7; Business Case Limitations item 7).

**One item carried forward from the Reconciled Finish Schedule — CLOSED 1 October 2026, updated here during the project's final cross-document consistency pass:** the AI4I failure-mode full-name mapping (e.g., HDF = Heat Dissipation Failure, OSF = Overstrain Failure) used throughout this report's source documents has now been verified directly against the dataset's own documented generation mechanism (Matzka, S. (2020), "Explainable Artificial Intelligence for Predictive Maintenance Applications," *3rd International Conference on Artificial Intelligence for Industries (AI4I)*, IEEE, doi.org/10.1109/AI4I49448.2020.00023), as part of the same sourcing pass that produced the real Q5/Q6 analysis below. All five names match exactly what this report and the dashboard already display — no relabeling was needed. See `Scope-Decisions-and-Limitations-Log.md`, Gap G5 and Gap G8 entries, 1 Oct 2026, for the full record. (This item was still open when this report was first drafted on 30 Sept 2026; the paragraph above has been updated in place rather than left to silently contradict the Reconciled-Finish-Schedule's own 1 Oct 2026 closure note.)

---

## 9. Recommendation Summary

1. **Adopt as committed, go-live-ready:** the foundational disclosure benefit (4.0), the Pareto/preventable-vs-random prioritization benefits (4.2), and the credibility/audit-defensibility benefit (Section 5) — all rated Medium confidence or higher, all grounded in DATASET evidence, none dependent on an unvalidated external assumption.
2. **Adopt as a working-planning figure only, not a committed target:** the Step 4 escalation-checkpoint savings range (Section 3.2, Section 6.3) — proceed with the process change on its qualitative merits (it directly targets a named root cause, BRD Risk 1), but do not publish, pitch, or resume-bullet the $172,064–$650,010 figure without the Reliability Engineer/Finance calibration this report's own source workbook already requires.
3. **Do not yet claim:** any Act & Prevent (O5/O6) benefit. Build FR-08 (calibration-date logging) first; this chain is correctly represented in Section 4.3 as a dependency map, not a benefit. Module A's results (Section 4.5, added 6 Oct 2026) corroborate Section 4.3's findings but do not change this recommendation — a second method agreeing with the first is not the same as either becoming deployable.
4. **Before the video walkthrough or any external publication:** set KPI-04's real baseline timing (Section 7) — still open. The AI4I failure-mode-name verification (Section 8) closed 1 October 2026 and no longer needs action here.

---

## Appendix A — Portfolio Process Note

This deliverable applies two named prompting/analysis techniques per the Master Plan's Day 16 instruction: **framework-grounded structured output** (Ward & Daniel's Benefits Dependency Network, used to force every claimed benefit through an explicit business-change dependency chain rather than asserting it directly from a technical capability) and **attribution critique** (Section 6, applied uniformly to every benefit rather than selectively to the ones already suspected of being weak — the Step 4 savings estimate, Section 6.3, is the specific example worth logging in the prompt library as a case where the critique changed the recommended framing, not just added a caveat after the fact). Both techniques are logged for `Prompt-Library.md`.

A genuine data-integrity event is worth recording here rather than only in Section 1.3: this report's dollar figures were cross-checked twice — once by independent recomputation from the same locked benchmarks before `06-Business-Case.xlsx` was made available, and once by direct reading of the workbook itself once supplied — and the two converged exactly. This is offered as one small, concrete, checkable data point for this portfolio's own "AI improved defensibility, not just speed" claim, not as proof that every number in this project is correct.
