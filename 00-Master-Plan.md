# Master Plan — AI-Powered Business Analyst Portfolio Project (Mining Industry)

**Owner:** Gagana Suresh
**Status:** Scenario recommended and locked (pending your sign-off) — plan built around it. Dataset pairing, tech stack, and three recruiter-facing additions (SQL layer, Job-Fit Matrix, optional ML proof-of-concept module) locked 20 Aug 2026 after a Perth job-market review.
**Last updated:** 24 August 2026

This document is the single source of truth for the project. Every future work session in this Project should check this file first before producing new deliverables, so nothing contradicts or duplicates what's already decided here.

---

## 1. Project Concept & Framing

### 1.1 Recommended scenario

**Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability** for a mining fleet and fixed-plant maintenance function, delivered as a BA-led initiative to redesign the work-order/reporting process and specify a CMMS reporting enhancement.

Framed as a real BA engagement: *"The maintenance function is losing production hours to unplanned breakdowns and can't tell leadership which asset class, failure mode, or shift is driving the loss. I've been brought in to gather requirements, analyze 12 months of maintenance and sensor data, and recommend a reporting and process fix — with a quantified business case."*

**Why this beats the alternatives** (evaluated against: richness of real/plausible data, stakeholder complexity, strength of the financial business case, and how instantly a mining hiring manager recognizes the pain point):

- **Haul truck/fleet utilization** — a strong runner-up, but public telemetry-grade fleet data is thin; most available datasets are either too generic (generic "truck fleet" logistics data with no mining context) or would need heavy fabrication to look credible. Downtime/reliability data is richer and more defensible.
- **Safety incident trends** — genuinely excellent *real* Australian and US data exists (WA WorkSafe, MSHA — see 1.2). But a safety-only project reads to a hiring panel as a compliance/reporting exercise rather than an operational-improvement initiative, and gives you a thinner process-design story. I've kept it as a **bonus module** (see Week 4) rather than the spine.
- **Production/throughput reporting** — the best public dataset here (Geoscience Australia's national mine production series) is annual/national-level, not shift- or site-level, so you can't build a believable operational process map or requirements doc around it — the grain is wrong for BA artifacts.
- **Supply chain & procurement** — no credible public mining-specific dataset exists; you'd be fabricating almost everything, which is the exact "over-claiming/generic" trap the project brief warns against.
- **Workforce rostering & fatigue** — sensitive by nature, essentially no public data, high risk of looking invented.
- **ESG/emissions reporting** — real Australian data exists (NPI — see 1.2), but on its own it's a reporting/compliance build, not a process-and-requirements story with a dollar-value business case.

Downtime/reliability wins because it gives you all five things a recruiter is scanning for in 60 seconds: a **dollar-quantified business case** (cost of downtime × hours lost), a **real cross-functional stakeholder set** (reliability engineers, maintenance planners, operations superintendent, procurement, finance, HSE), a **process to map and redesign** (breakdown → work order → repair → RCA → close-out), a **data model and dashboard** to build, and a problem every mining ops/maintenance leader recognizes on sight.

### 1.2 Data sources (real, public — use these; flag any gap-filling clearly)

Core equipment failure/sensor dataset: AI4I 2020 Predictive Maintenance Dataset (UCI ML Repository, mirrored on Kaggle) — real, citable, 10,000 industrial machine records with sensor readings and failure modes, re-skinned onto a synthetic mining asset register (disclosed explicitly). Repair time (MTTR) and repair cost benchmarks: sourced externally, Week 2, since AI4I has no repair-duration or repair-cost fields (confirmed 24 Aug 2026). Real Australian mining safety statistics (WorkSafe WA), US comparator safety data (MSHA), national production context (Geoscience Australia / Nature Scientific Data), a real mining process/quality dataset (Kaggle — evaluated and rejected as primary), and emissions/ESG data (NPI) round out the grounding-source set.

**Dataset pairing — locked (20 Aug 2026):** AI4I 2020 is the primary dataset because it is the only option with real row-level failure and sensor data. The Quality Prediction in a Mining Process dataset was deliberately evaluated and rejected as the primary source: real mining data, but no work-order structure to support a maintenance BRD.

**Correction (24 Aug 2026):** AI4I supports a genuine failure-mode Pareto and failure-frequency segmentation directly. It does **not** support a directly-computed MTTR — there is no repair-duration or repair-cost field in the source data at all. MTTR and repair cost must be sourced as external, cited benchmarks and applied as labeled assumptions on top of AI4I's real failure counts.

**Data integrity rule for the whole project:** every chart, table, or claim must be traceable to either (a) the AI4I dataset re-skinned with a documented mapping table, (b) a cited real source, or (c) an explicitly labelled assumption. Never let a number appear in the deliverables without one of those three tags.

### 1.3 Elevator pitch (interview-ready)

*"I built a portfolio project simulating a BA engagement inside a mining maintenance function that was losing production hours to unplanned equipment breakdowns with no clear view of which assets or failure modes were driving the loss. I ran it like a real consulting engagement — stakeholder interviews (simulated but grounded in real mining org structures), a requirements and process-mapping phase, a redesigned maintenance reporting workflow, a Power BI reliability dashboard, and a benefit-realization report projecting the downtime-cost reduction. What makes it different from a typical portfolio piece is that I used Claude as a genuine analytical partner throughout — not just for polish — and I tracked exactly where it saved time and where it caught requirement gaps I'd have missed working alone, with real before/after numbers documented in a prompt library anyone can review."*

### 1.4 Target roles this project is optimized for

Business Analyst (mining/resources or heavy industry), Business Systems Analyst, Process/Operational Excellence Analyst, Data & Insights Analyst with BA leanings, and "AI-augmented" or "Analyst, AI Enablement" roles.

### 1.5 Tools & tech stack

Data cleaning/transformation: Python (pandas) and Excel. Data storage/querying: a small SQLite layer — the cleaned, re-skinned dataset is loaded into an actual queryable database, and the core analytical queries are written as SQL. Added deliberately on 20 Aug 2026 after reviewing live Perth BA/analyst job postings. Reporting/dashboard: Power BI (or Tableau Public). Process mapping: Draw.io/Lucidchart/Visio. Requirements/backlog tracking: Jira or Trello. Predictive analytics (optional stretch module only): Python (scikit-learn). Version control/portfolio hosting: **GitHub.**

---

## 2. Week-by-Week Execution Plan (summary)

**Week 1 — Discovery, Framing & Requirements:** charter, synthetic asset register, stakeholder register, simulated interview transcripts, BRD v1, red-team critique → BRD v2.

**Week 2 — Process Mapping & Data Design:** as-is process map, to-be process map + gap analysis, data dictionary, clean/re-skin the dataset + load into SQLite + core SQL queries, first-pass EDA.

**Week 3 — Build:** Power BI dashboard, cost-of-downtime business case, user stories, test cases.

**Week 4 — Benefit Realization, Bonus Module, Testing & Sign-off:** benefit realization report, optional safety-trend bonus module, traceability matrix, full documentation consistency pass, Job-Fit Matrix.

**Flex/Polish Week (Week 5) — Packaging:** GitHub repo assembly, video recording, LinkedIn article, one-pager.

**Optional Stretch Module (build only after everything else):** a single, tightly-scoped predictive-maintenance classifier proof-of-concept — never the headline of the portfolio.

---

## 3. The Efficiency Story — Your Core Differentiator

Log **every** task in a running efficiency tracker the moment you finish it — not retrospectively, because the numbers will look invented otherwise. Track: task name, deliverable, estimated manual time (recorded *before* starting), actual time with Claude, AI's role, a concrete quality signal, technique used, and an honest caveat. The credible version of "AI made me faster" needs specific named tasks, a defensible pre-recorded baseline, and quality evidence beyond speed — never a single headline multiplier like "10x faster."

---

## 4. The Prompt Engineering Artifact (Prompt Library)

Build `prompt-library/` as its own folder, one markdown file per technique-tagged prompt (aim for 15–25 entries): context, the actual prompt verbatim, why designed that way, output produced, and — the most important field — what was changed after reviewing it. **At least one entry must document a substantive override** — a real moment of disagreeing with and changing a meaningful Claude judgment call, not a typo fix.

---

## 5. Portfolio Packaging

### 5.1 GitHub repository structure

```
mining-ba-reliability-project/
├── README.md
├── 00-Assumptions-Log.md
├── 01-Project-Charter.md
├── 02-Stakeholder-Register.md
├── 03-BRD-Maintenance-Reporting.md
├── 04-Process-Maps/
├── 05-Data-Dictionary.md
├── 06-Business-Case.xlsx
├── 07-User-Stories.md
├── 08-Test-Cases.md
├── 09-Benefit-Realization-Report.md
├── 10-Traceability-Matrix.xlsx
├── 11-Job-Fit-Matrix.md
├── 12-ML-Proof-of-Concept.md          # OPTIONAL, build last
├── data/
│   ├── raw/
│   ├── processed/
│   ├── mining_reliability.db
│   └── data-lineage-note.md
├── dashboard/
├── prompt-library/
├── efficiency-tracker/
└── video-and-linkedin/
```

### 5.2–5.4 Video, LinkedIn article, one-page case study

Video (6–8 min): hook → BRD/stakeholder walkthrough with a real critique catch shown on screen → process map trade-off → live dashboard tied to the business case → the efficiency story with honest caveats → close. LinkedIn article (800–1200 words) + a short announcement post. One-page case study, built last, once every number is final.

---

## 6. Recruiter-Facing Polish

Confirm before publishing: every number traces to the dataset, a cited source, or a labelled assumption; every prompt-library entry shows a real edit, not just a paste; the README states plainly this is a simulated engagement with synthetic/adapted data; the efficiency numbers include at least one honest caveat; the writing sounds human, not unedited AI output.

---

## 7. Risks & Pitfalls

Over-claiming AI's contribution, generic ungrounded industry claims, no evidence of judgment, treating synthetic data as if real, confusing the operational dataset with citation-only grounding sources, and scope creep from the optional ML module are the five failure modes this plan is deliberately built to avoid — see the full document (Claude Project) for the specific guardrail against each.
