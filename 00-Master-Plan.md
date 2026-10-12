# Master Plan — AI-Powered Business Analyst Portfolio Project (Mining Industry)

**Owner:** Gagana Suresh
**Status:** Scenario recommended and locked (pending your sign-off) — plan built around it. Dataset pairing, tech stack, and three recruiter-facing additions (SQL layer, Job-Fit Matrix, optional ML proof-of-concept module) locked 20 Aug 2026 after a Perth job-market review. **A second optional stretch module (LLM cause-code classifier) added 24 Sept 2026 — see Section 2.**
**Last updated:** 24 September 2026

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

| Purpose | Source | Notes |
|---|---|---|
| Core equipment failure/sensor dataset | [AI4I 2020 Predictive Maintenance Dataset — UCI ML Repository](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) (mirrored on [Kaggle](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020)) | Real, citable, machine-learning-grade dataset of 10,000 industrial machine records with sensor readings (torque, rotational speed, tool wear, temperature) and failure modes, including a binary `Machine failure` label and five failure-mode labels (TWF, HDF, PWF, OSF, RNF). **It is generic industrial equipment, not mining-labelled.** You will re-skin it: map its machine IDs onto a synthetic mining asset register (haul trucks, crushers, conveyors, pumps) you build yourself. Disclose this adaptation explicitly in the README and case study — this is the "honest synthetic data" move the project brief requires. **Confirmed limitation (24 Aug 2026): AI4I has no repair-time or repair-cost fields — see the Scope-Decisions-and-Limitations-Log entry of that date.** |
| Repair time (MTTR) and repair cost benchmark | *To be sourced — Week 2, before Day 9/10 build* | AI4I has no repair-duration or repair-cost data at all (confirmed 24 Aug 2026). Needed as two labeled external assumptions: average repair time per failure event, and average repair cost per failure event — see Scope-Decisions-and-Limitations-Log for the full reasoning and sourcing approach. |
| Real Australian mining safety statistics (context/business case grounding) | [WorkSafe WA — Mining and Exploration Safety Statistics](https://www.worksafe.wa.gov.au/mining-and-exploration-safety-statistics) | Real, current, Perth-relevant. Use for your business case narrative ("the WA mining sector recorded X lost-time injuries in FY24/25...") — gives the project a credible local anchor since you're WA-based. |
| US comparator safety data (optional, for the safety bonus module) | [MSHA Mine Data Retrieval System](https://www.msha.gov/data-and-reports/mine-data-retrieval-system) and [MSHA Accident/Injuries dataset on data.gov](https://catalog.data.gov/dataset/msha-accident-injuries-data-set) | Real, large, downloadable accident/injury records. Good if you build the safety-trends bonus deliverable in Week 4. |
| National production context (intro/background only, not operational analysis) | [A Comprehensive Dataset for Australian Mine Production, 1799–2021 (Nature Scientific Data)](https://www.nature.com/articles/s41597-023-02275-z); [Geoscience Australia OZMIN operating mines dataset](https://data.gov.au/data/dataset/65c0c042-1ba8-47a8-9793-4363672500b9) | Use in your BRD's "industry context" section for credibility, not as the operational dataset — grain is too coarse. |
| Real mining process/quality dataset (evaluated and rejected as primary — see decision note below) | [Quality Prediction in a Mining Process — Kaggle](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process) | Real sensor data from an actual iron-ore flotation plant. Not used as the core dataset — citing it in your prompt library ("evaluated as an alternative dataset, rejected because...") shows real judgement/vetting rather than grabbing the first dataset you found. |
| Emissions/ESG (optional bonus angle) | [National Pollutant Inventory data — DCCEEW](https://www.dcceew.gov.au/environment/protection/npi/data) | Real Australian facility-level emissions data if you want to extend the case study into an ESG angle later. |
| Synthetic free-text work-order cause codes (for the LLM classifier stretch module — see Section 2) | *Built by hand, Gagana + Claude, before that module is built* | AI4I has no free-text field at all — this is a purpose-built, clearly-labeled synthetic dataset representing the kind of messy, inconsistent cause-code entries the Maintenance Superintendent – Fixed Plant interview described (the real ~40-option CMMS dropdown, roughly half of which don't fit real failure descriptions). Same disclosure discipline as the AI4I re-skin: label it synthetic, everywhere it appears. |

**Dataset pairing — locked (20 Aug 2026):** AI4I 2020 is the primary dataset because it is the only option with real row-level failure and sensor data — that's what makes genuine MTBF/MTTR calculations and a failure-mode Pareto possible, instead of narrative-only BA documents with no numbers behind them. The Quality Prediction in a Mining Process dataset (real mining sensor data) was deliberately evaluated and rejected as the primary source: it's real mining data, but it's process/quality data with no work-order structure, so it cannot support a BRD or maintenance business case built around the breakdown → work order → repair lifecycle. Document this rejection explicitly in the prompt library as evidence of source vetting. AI4I is paired with WA WorkSafe safety statistics and Geoscience Australia production data as a grounding layer — cited specifically in the business case and industry-context sections — so the project reads as being about WA mining specifically, not generic industry with a mining label stuck on it.

**Correction (24 Aug 2026):** the phrase "genuine MTBF/MTTR calculations" above is only half accurate and is kept here for decision history, not as current guidance — see the next paragraph and the Scope-Decisions-and-Limitations-Log entry of 24 Aug 2026. AI4I supports a genuine failure-mode Pareto and failure-frequency segmentation directly. It does **not** support a directly-computed MTTR (mean time to repair) — there is no repair-duration or repair-cost field in the source data at all. MTTR and repair cost must be sourced as external, cited benchmarks and applied as labeled assumptions on top of AI4I's real failure counts, not computed from AI4I itself.

**Two different kinds of "using a data source" — don't conflate them (clarified 20 Aug 2026):** AI4I 2020 is your only **operational dataset** — the one you actually download as a file, clean, re-skin onto your synthetic asset register, load into the SQLite database, and run row-level analysis against (failure-mode Pareto, failure-rate segmentation, and — pending the asset-mapping decision in the Scope-Decisions-and-Limitations-Log — a frequency-based MTBF proxy). WA WorkSafe and Geoscience Australia are **grounding/citation sources**, not operational datasets — you do not download and merge them the way you do AI4I. Instead you visit their published reports/statistics pages, pull out specific real figures, and cite them directly (with a link) in the BRD's industry-context section (Week 1, Day 4) and the business case (Week 3, Day 13). If a task in this plan says "download and clean," it means AI4I. If it says "cite" or "use for grounding/context," it means go find the real number on the source's site and reference it — no bulk download or row-level data processing needed for those two.

**Data integrity rule for the whole project:** every chart, table, or claim must be traceable to either (a) the AI4I dataset re-skinned with a documented mapping table, (b) a cited real source above, or (c) an explicitly labelled assumption (e.g., "Assumed loaded cost of downtime: $4,200/hour — sourced from [industry benchmark], see Assumptions Log"). Never let a number appear in the deliverables without one of those three tags. In particular, the core downtime-cost-per-hour figure driving the business case, and (as of 24 Aug 2026) the MTTR-per-event and repair-cost-per-event figures, must all be real, cited industry benchmarks — not plausible-sounding round numbers — since these are the first things a skeptical interviewer or finance stakeholder will probe. The same discipline extends to the LLM classifier module (Section 2): its input free-text data is synthetic and must be labeled as such everywhere it appears, exactly like the site-location scaffolding data.

### 1.3 Elevator pitch (interview-ready)

*"I built a portfolio project simulating a BA engagement inside a mining maintenance function that was losing production hours to unplanned equipment breakdowns with no clear view of which assets or failure modes were driving the loss. I ran it like a real consulting engagement — stakeholder interviews (simulated but grounded in real mining org structures), a requirements and process-mapping phase, a redesigned maintenance reporting workflow, a Power BI reliability dashboard, and a benefit-realization report projecting the downtime-cost reduction. What makes it different from a typical portfolio piece is that I used Claude as a genuine analytical partner throughout — not just for polish — and I tracked exactly where it saved time and where it caught requirement gaps I'd have missed working alone, with real before/after numbers documented in a prompt library anyone can review."*

### 1.4 Target roles this project is optimized for

Business Analyst (mining/resources or heavy industry), Business Systems Analyst, Process/Operational Excellence Analyst, Data & Insights Analyst with BA leanings, and "AI-augmented" or "Analyst, AI Enablement" roles now appearing at resources companies and BA consultancies. The deliverable set (BRD, process maps, dashboard, benefit realization report) targets the first three directly; the prompt library and efficiency metrics target the AI-augmented framing specifically. The two optional stretch modules (Section 2 — a classical ML proof-of-concept and an LLM-based text classifier) nudge fit further toward the "Data & Insights Analyst with BA leanings" and "AI Enablement" ends without repositioning the project away from its BA core — together they demonstrate range across both classical ML and applied LLM/NLP work, which is an increasingly common pairing in these job ads.

### 1.5 Tools & tech stack

Data cleaning/transformation: Python (pandas) and Excel. Data storage/querying: a small SQLite (or Postgres) layer — the cleaned, re-skinned dataset is loaded into an actual queryable database, and the core analytical queries (downtime by asset class, failure-mode Pareto, MTBF/MTTR) are written as SQL rather than living only as Excel formulas. This was added deliberately on 20 Aug 2026 after reviewing live Perth BA/analyst job postings: SQL is one of the most repeated required skills in the market and was the one clear gap in the original plan. Reporting/dashboard: Power BI (or Tableau Public), with measures built on top of the SQL layer. Process mapping: Draw.io, Lucidchart, or Visio for swimlane diagrams (BPMN-style notation). Requirements/backlog tracking: Jira or Trello for user stories. Predictive analytics (optional stretch module only): Python (scikit-learn) for a single classification model — logistic regression or random forest — see Section 2. Applied LLM/NLP (second optional stretch module): Claude, prompted directly (no separate ML training step) to classify free-text work-order entries — see Section 2. Version control/portfolio hosting: GitHub.

---

## 2. Week-by-Week Execution Plan

Planned as **4 core weeks + 1 flex/polish week** (use the flex week if you want the safety bonus module, extra dashboard polish, or more video takes — the brief calls for "3–4+ weeks," this plan is built to flex from 4 to 5 without restructuring). Two optional stretch modules (predictive maintenance proof-of-concept, and an LLM cause-code classifier) sit outside this structure entirely — see the end of this section.

Each task lists: **deliverable → how to use Claude → prompting technique to practice → time estimate**. Prompt examples are adapt-and-paste starting points, not scripts to copy verbatim — tell Claude what's different about your context and it'll adjust.

### Week 1 — Discovery, Framing & Requirements

| Day | Task & Deliverable | How to use Claude | Technique practiced | Est. time |
|---|---|---|---|---|
| 1 | Finalize scope statement + project charter (`01-Project-Charter.md`) | Role-prompt Claude as a "principal BA reviewing a junior's charter for a mining client" and have it red-team your draft scope for ambiguity, missing success criteria, and scope creep risks | Role/persona prompting; critique loop | 2 hrs |
| 1–2 | Build the synthetic mining asset register (equipment list, sites, criticality ratings) that the AI4I data will be re-skinned onto | Give Claude the AI4I column structure and ask it to propose a realistic mining asset taxonomy (haul trucks, excavators, crushers, conveyors, pumps) with criticality/cost-of-downtime tiers, citing why each tier makes sense operationally | Structured output (ask for a table with defined columns); few-shot (give it 2 example rows in your target format) | 3 hrs |
| 2 | Stakeholder register (`02-Stakeholder-Register.md`) — 10–14 stakeholders across ops, maintenance, finance, HSE, IT/CMMS, procurement | Chain-of-thought prompt: ask Claude to first reason through the maintenance work-order lifecycle end-to-end, *then* derive every role that touches that lifecycle, before producing the register — this stops it from generating a generic/shallow stakeholder list | Chain-of-thought reasoning before structured output | 2.5 hrs |
| 3 | Draft interview questions + **simulated stakeholder interview transcripts** (3–4 personas: Maintenance Planner, Reliability Engineer, Ops Superintendent, Finance/Cost Controller) | Multi-turn role-play: ask Claude to play each persona (grounded, mildly conflicting priorities — e.g., Finance wants cost cuts, Ops wants uptime) while you interview it in character; capture the transcript as raw input for requirements. **Flag clearly in the repo that these are simulated interviews standing in for unavailable real stakeholders.** | Persona/role prompting; iterative multi-turn dialogue | 4 hrs |
| 4 | Requirements elicitation → **Business Requirements Document draft v1** (`03-BRD-Maintenance-Reporting.md`); also cite real WA WorkSafe/Geoscience Australia figures in the BRD's "industry context" section (see Section 1.2 note on grounding sources) | Feed the transcripts + charter to Claude and ask for a first-draft BRD in a defined template (functional/non-functional reqs, in/out of scope, assumptions, constraints); this is your first "time to first draft" measurement point (see Section 3) | Structured output format; template-constrained generation | 3 hrs |
| 5 | **Red-team the BRD**: ask Claude, in a fresh context as an adversarial reviewer, to find gaps, ambiguous requirements, untestable acceptance criteria, and conflicting stakeholder needs | Explicit critique/red-team prompt ("You are a skeptical PM at sign-off review — find every requirement that would get bounced back") — then revise the BRD to v2 and log every gap it caught | Critique/red-team loop; self-consistency check across two Claude passes | 3 hrs |

**Week 1 milestone:** Charter, stakeholder register, BRD v2, and a running Assumptions Log (`00-Assumptions-Log.md`) that already needs to exist by end of Week 1 — start it Day 1, add to it every day.

### Week 2 — Process Mapping & Data Design

| Day | Task & Deliverable | How to use Claude | Technique practiced | Est. time |
|---|---|---|---|---|
| 6 | As-is process map: current (broken) breakdown-to-repair workflow, in draw.io/Lucidchart | Ask Claude to convert your BRD's narrative into a step-by-step swimlane process description (who does what, handoffs, delays) that you then diagram manually — Claude doesn't draw the diagram, it structures the logic | Chain-of-thought decomposition of a process into discrete steps/swimlanes | 3 hrs |
| 7 | To-be process map + gap analysis (`04-Process-Maps.md` + diagram files) | Give Claude the as-is map and ask it to propose 2–3 to-be redesign options with trade-offs (cost, effort, risk) rather than one "best" answer — forces you to make and justify the actual decision | Structured comparison / options-analysis output | 3 hrs |
| 8 | Data model: entity relationships between asset register, work orders, failure records, cost data (`05-Data-Dictionary.md`) | Ask Claude to reverse-engineer a data dictionary and ER structure from the AI4I columns + your asset register, flagging any fields you'll need to fabricate and why | Structured output; explicit "flag assumptions inline" instruction | 3 hrs |
| 9 | Clean and re-skin the AI4I dataset into the mining context in Excel/Python (mapping machine IDs → asset IDs, relabeling failure types to mining failure modes); load the cleaned dataset into a SQLite database and write the core SQL queries (failure counts/rate by asset class, failure-mode Pareto — plus downtime-hours/cost queries that join real failure counts against the external MTTR and repair-cost benchmarks decided in the Scope-Decisions-and-Limitations-Log, 24 Aug 2026) that will feed the Week 3 dashboard. **Before this day starts:** confirm how multiple AI4I rows map to one synthetic asset ID (open item in that same log entry) and source the two external repair-time/repair-cost benchmarks — MTTR is not computable from AI4I itself. | Use Claude to write/check the Python (pandas) transformation script and the SQL queries; ask it to also generate a short data-lineage note documenting exactly what was changed from the source dataset, including which figures are dataset-derived vs. assumption-derived | Prompt-to-code with explicit spec; verification step (ask Claude to write a sanity-check script that flags row-count/nulls issues) | 4.5 hrs |
| 10 | Exploratory data analysis: failure counts/rate by asset class, failure-mode Pareto, and downtime-hours/cost estimation (real failure counts from AI4I × the external MTTR and repair-cost benchmarks — see Scope-Decisions-and-Limitations-Log, 24 Aug 2026 entry; a frequency-based MTBF proxy only if the Day 9 asset-mapping decision supports it) | Ask Claude to co-review your analysis approach *before* you build it — "what would a skeptical reliability engineer say is missing from this analysis plan?" — then use it to interpret your output stats afterward | Plan-then-critique loop (ask for critique of the plan, not just the output) | 4 hrs |

**Week 2 milestone:** As-is/to-be process maps, data dictionary, cleaned dataset with documented lineage and loaded into a SQLite database with the core analytical queries, first-pass EDA findings.

### Week 3 — Build: Dashboard, Business Case, Requirements Sign-off Artifacts

| Day | Task & Deliverable | How to use Claude | Technique practiced | Est. time |
|---|---|---|---|---|
| 11–12 | Build the Power BI (or Tableau Public) reliability dashboard: downtime trend, top failure modes, cost-of-downtime by asset class, MTTR/MTBF trend | Use Claude for DAX/measure logic built on top of the Week 2 SQL queries, chart-selection reasoning ("which chart type best shows failure-mode concentration — justify"), and a dashboard-design critique pass once built | Structured reasoning for design decisions; critique loop on a visual artifact via screenshot | 8 hrs |
| 13 | Cost-of-downtime business case model in Excel (`06-Business-Case.xlsx`) — current-state loss vs. projected savings from the to-be process; ground the AUD/hour downtime-cost figure, the MTTR-per-event figure, the repair-cost-per-event figure, and any comparator stats with real cited benchmarks (see Section 1.2 note and the Scope-Decisions-and-Limitations-Log, 24 Aug 2026 entry) | Ask Claude to sanity-check your formulas and assumptions logic, and to red-team the business case the way a finance stakeholder would ("where would Finance push back on these numbers?"); confirm the core AUD/hour, MTTR, and repair-cost figures are all real, cited industry benchmarks, not plausible-sounding round numbers | Critique/red-team loop applied to quantitative work, not just text | 3 hrs |
| 14 | User stories / functional requirements + acceptance criteria for the CMMS reporting enhancement, in Jira or Trello (`07-User-Stories.md`) | Few-shot: give Claude 2 well-formed example stories in your house format, ask it to generate the rest in matching style and quality, then you edit for accuracy | Few-shot prompting for consistent output format | 3 hrs |
| 15 | Test cases / UAT scenarios for the dashboard and reporting requirements (`08-Test-Cases.md`) | Ask Claude to derive test cases directly from the acceptance criteria (traceability), and separately to generate 2–3 edge cases a less careful analyst would miss | Chain-of-thought traceability mapping; edge-case generation prompt | 2.5 hrs |

**Week 3 milestone:** Working dashboard, business case model, user stories with acceptance criteria, test cases — this is the "so what" week where the numbers get real.

### Week 4 — Benefit Realization, Bonus Module, Testing & Sign-off

| Day | Task & Deliverable | How to use Claude | Technique practiced | Est. time |
|---|---|---|---|---|
| 16 | Benefit realization report (`09-Benefit-Realization-Report.md`) — projected $ and hours saved, KPIs to track post-implementation | Ask Claude to structure this against a recognized benefits-realization framework and to stress-test whether your claimed benefits are actually attributable to the recommended changes (vs. wishful attribution) | Framework-grounded structured output; attribution critique | 3 hrs |
| 17 | **Bonus module (optional, lowest priority of the three optional add-ons):** safety-incident trend mini-analysis using real WorkSafe WA / MSHA data, framed as "what this means for the maintenance reliability program" | Ask Claude to help you identify a genuinely interesting, defensible correlation/pattern to investigate (not a spurious one) — practice asking it to argue *against* a pattern before you commit to reporting it | Devil's-advocate / self-critique prompting to avoid spurious-correlation traps | 4 hrs |
| 18 | Full requirements traceability matrix (BRD → user stories → test cases → dashboard elements) (`10-Traceability-Matrix.xlsx`) | Ask Claude to build this by cross-referencing your existing documents and flag any requirement with no corresponding test case or dashboard element | Structured cross-document consistency check | 2.5 hrs |
| 19 | Full documentation pass: consistency check across every deliverable (naming, numbers matching across docs, no contradictions) | Feed Claude the full document set and ask it to audit for inconsistencies (a number in the BRD that doesn't match the business case, etc.) | Cross-document QA / consistency audit prompt | 3 hrs |
| 20 | Buffer/catch-up day; build the Job-Fit Matrix (`11-Job-Fit-Matrix.md`) — pull 8–12 real requirement lines from current Perth BA/analyst job postings (Power BI, SQL, BPMN, JIRA, ERP/CMMS, stakeholder management, "AI-assisted development," etc.) and map each one directly to a specific deliverable you've already built | Ask Claude to help source and organize real quoted requirement lines from live postings, then structure the matrix; this is a recruiter-facing artifact, not a technical one — it does the recruiter's pattern-matching work for them | Structured cross-referencing; sourcing/citation discipline | 3 hrs |

**Note on the bonus safety module (Day 17):** with two optional stretch modules now also in scope (below), the safety bonus module is the first thing to cut if time runs short — it was always the lowest-priority optional add-on of the three, since it reads as a compliance/reporting side-note rather than reinforcing the core reliability story the way the ML and LLM modules do (both of which connect directly to the locked business questions and a real, disclosed process pain point). Default assumption, flagged for Gagana to override: **defer it**, revisit only if the core plan finishes with real time to spare.

### Flex/Polish Week (Week 5) — Packaging

Reserved for GitHub repo assembly, video recording (multiple takes are normal), LinkedIn article writing, and the one-pager — detailed in Section 5. Budget 15–20 hours. **Sequencing note, updated 24 Sept 2026:** run this *after* both optional stretch modules below, not before — the video script and LinkedIn article are each meant to include a one-sentence mention of the stretch modules (per their own guardrails), which only works if they already exist when you write the packaging copy.

### Optional Stretch Modules

**Locked 20 Aug 2026 (Module A); added 24 Sept 2026 (Module B).** Build both **only after** Weeks 1–4 are fully complete — they do not occupy a day slot in the core plan and must never delay or displace a core deliverable. If time runs out before you reach either, skip it entirely; the project is complete and credible without them. **Shared guardrail for both:** neither module may ever be the headline of the README, video, or LinkedIn article — each is a footnote demonstrating range, not a second core deliverable. If either starts requiring meaningfully more than its budgeted time, or you find yourself wanting to feature it prominently, that's the signal to cut scope back, not expand it.

#### Module A — Predictive Maintenance Proof-of-Concept (classical ML)

**Why it earns a place (kept honest):** AI4I 2020 was originally built as an ML classification dataset — it ships with a binary `Machine failure` label and five failure-mode labels (TWF, HDF, PWF, OSF, RNF) sitting alongside the sensor features you're already using. Recognizing that the data supports a predictive angle, scoping a small validated proof-of-concept rather than either ignoring it or overbuilding it, is itself a BA judgment call — knowing when a predictive model is worth building and validating that case — not a pivot into claiming data-scientist depth. This is on-story, not off-story, *as long as its size stays protected.*

**Locked scope (do not exceed):**

| Task & Deliverable | How to use Claude | Technique practiced | Est. time |
|---|---|---|---|
| Build a single predictive-maintenance classifier (logistic regression or random forest — no ensembling, no hyperparameter-tuning rabbit holes) on the cleaned dataset from the Week 2 SQL layer; use a proper train/test split; explicitly handle the dataset's known class imbalance (most machines don't fail, so accuracy alone is a meaningless metric); report precision, recall, and a confusion matrix honestly, including where the model underperforms; write a short plain-English proof-of-concept note (`12-ML-Proof-of-Concept.md`) linking the result back to the Benefit Realization Report as a forward-looking recommendation ("this validates that a predictive extension is feasible; productionizing it would be a phase-2 initiative outside this engagement's scope") | Ask Claude to review your evaluation approach *before* you build — specifically to check you're not just optimizing accuracy on an imbalanced dataset — then use it to sanity-check the model code and to red-team whether the result is genuinely useful or just a naive majority-class predictor in disguise | Plan-then-critique loop applied to a technical/quantitative deliverable; explicit "flag the naive-baseline trap" framing | 4–6 hrs |

See `Interview-Prep-QA.md` Q18 for the technical follow-up questions this module invites and how to hold the line under them.

#### Module B — LLM Cause-Code Classifier (applied NLP/LLM)

**Added 24 Sept 2026, at Gagana's request to demonstrate LLM/prompt-engineering range alongside the classical ML module.** **Why it earns a place, on the same "kept honest" standard as Module A:** this isn't a bolt-on gimmick — it directly implements a real, already-identified gap. The Maintenance Superintendent – Fixed Plant interview (3 Sept 2026) named a specific, credible process pain point: the CMMS's cause-code field is a roughly 40-option dropdown, and about half those options don't actually fit real failure descriptions, so technicians pick "close enough" rather than accurate. That finding produced a proposed requirement, **FR-14** (`04-Process-Maps.md` Section 10; Scope-Decisions-and-Limitations-Log, 4 Sept 2026), which was logged as "proposed, not yet built" pending a decision from Gagana. This module *is* that decision, exercised as a stretch build rather than a formal BRD requirement (see the status note below) — it demonstrates the exact kind of judgment call BA-with-AI roles are increasingly asked to make: recognizing where an LLM is the right tool for a messy-text classification problem a rules-based dropdown redesign can't cleanly solve.

**Status — demo/stretch, not a formal engagement requirement (default assumption, flagged for Gagana to confirm or override):** treated the same way as Module A — a labeled proof-of-concept sitting outside the locked engagement scope, not folded into BRD v3 as an approved FR-14. This keeps it out of the traceability matrix, test cases, and acceptance-criteria machinery a formal requirement would need, which is what keeps its time budget honest. If Gagana later decides FR-14 should become a real, numbered requirement, that's a bigger follow-on piece of work than this module — see `03-BRD-Maintenance-Reporting.md` Section 17 open items.

**Data note:** AI4I has no free-text field of any kind, so this module needs its own small, purpose-built, clearly-labeled synthetic dataset — a set of illustrative free-text work-order cause-code entries reflecting the kind of messiness the interview described (inconsistent phrasing, overlapping categories, a few genuinely ambiguous entries). This is scaffolding data in the same category as the synthetic asset register (Section 1.2), not a data-derived finding — it must never be presented as if it came from a real CMMS export.

**Locked scope (do not exceed):**

| Task & Deliverable | How to use Claude | Technique practiced | Est. time |
|---|---|---|---|
| Build a small synthetic set (~40–60 rows) of illustrative free-text work-order cause-code entries, grounded in the interview's description of the messy real taxonomy, explicitly labeled synthetic. Design a small, clean target taxonomy that maps onto AI4I's five real failure modes (TWF/HDF/PWF/OSF/RNF) plus 1–2 additional categories the interview named that AI4I's taxonomy doesn't cover (e.g., electrical, instrumentation/sensor). Prompt Claude to classify each entry into the clean taxonomy — this is a prompting/evaluation exercise, not a fine-tuning project, so no model training step is needed. Hold out a subset you label by hand first, then score the classifier's agreement against your own labels — report accuracy honestly per category, including where it does worst (e.g., genuinely ambiguous entries), the same "no naive metric, show where it underperforms" discipline as Module A. Write a short plain-English write-up (`13-LLM-Cause-Code-Classifier.md`) that states the synthetic-data caveat up front, links back to FR-14 and the Fixed-Plant Superintendent interview, and frames the result the same way Module A frames its result: this validates feasibility; deploying it against a real CMMS export would be a phase-2 initiative outside this engagement's locked scope. | Use Claude for the classification itself (this is the deliverable, not just the drafting aid — be explicit in the write-up that Claude is the classifier under test, not merely helping you build one); ask it to also help you design the hand-labeled evaluation set adversarially (deliberately include a few ambiguous/edge-case entries, don't only test on easy ones) | Structured output + prompt-based classification; critique/red-team framing applied to your own evaluation design, not just the output (the same "check you're not just testing the easy cases" discipline as Module A's "check you're not just optimizing accuracy" instruction) | 4–5 hrs |

**Guardrail specific to this module:** because Claude is both the classifier under test and the tool you're using to build the evaluation, be explicit in the write-up about that dual role, and disclose it plainly — this is exactly the kind of "did AI just do this for you?" question the project's credibility checklist (Section 6.2) already anticipates, just applied to a new deliverable. The honest framing: you designed the taxonomy, built the adversarial evaluation set, and judged the results — Claude did the classification itself, which is the point of the demo, not something to obscure.

---

## 3. The Efficiency Story — Your Core Differentiator

### 3.1 What to track, and how

Log **every** task above in a running efficiency tracker the moment you finish it — not retrospectively at the end, because you will not remember accurately and the numbers will look invented. Use this template as an Excel/Sheets tab (`Efficiency-Tracker.xlsx`, one row per task):

| Field | What to record |
|---|---|
| Task ID / name | e.g. "BRD v1 first draft" |
| Deliverable produced | Link to file |
| Estimated manual time (no AI) | Your honest best estimate *made before* you start, based on how long you know this kind of task normally takes — write this down first, so it can't be reverse-fitted afterward |
| Actual time with Claude | Stopwatch/timestamp it — start and end |
| AI role in the task | Drafting / critique-only / code-generation / research / sanity-check |
| Quality signal | Concrete and countable, e.g. "red-team pass caught 4 requirement gaps I'd missed," "critique flagged 2 conflicting stakeholder needs," "sanity-check caught a formula error in the business case" |
| Technique used | Cross-reference to the prompt library entry |
| Honest caveat | Anything that makes the number less clean — e.g. "included 20 min of me correcting AI's assumption about X" |

### 3.2 Turning this into a believable narrative (not a vague claim)

The credible version of "AI made me faster" has three ingredients a skeptical reader checks for: **specific tasks named**, **a defensible baseline** (your pre-recorded manual-time estimate, not a guess made after the fact to fit a good ratio), and **quality evidence that isn't just speed** (gaps caught, errors prevented). Structure your final efficiency summary as a short table plus 3–4 sentences, e.g.:

> *"Across the project I logged 20 discrete BA tasks. Median time reduction was ~45% (e.g., BRD first draft: est. 5 hrs manual → 2.1 hrs with Claude). More importantly, the critique-loop technique caught 11 requirement gaps and 3 numerical inconsistencies across the document set before they reached a 'final' state — issues that, in my prior BA work, typically surfaced during stakeholder review rather than before it. Full task-by-task data is in the Efficiency Tracker."*

Avoid a single headline multiplier ("10x faster!") — it's the first thing an experienced interviewer will probe and it invites skepticism. A distribution of numbers across real, named tasks is far more defensible than one big claim.

---

## 4. The Prompt Engineering Artifact (Prompt Library)

Build `prompt-library/` as its own folder in the repo, not an afterthought. For **every** technique-tagged prompt in the tables above (aim for 15–25 entries, quality over quantity — a smaller set of 10–12 genuinely detailed entries is a defensible fallback if time is short, but is not the default), document one entry as a short markdown file using this structure:

```
### [Technique] — [Task it was used for]
**Context:** what you were trying to achieve and why a simpler prompt wouldn't have worked
**Prompt:** the actual prompt, verbatim
**Why designed this way:** the specific engineering choice (e.g., "role-prompting as an adversarial reviewer rather than asking 'check my BRD' — a neutral ask gets a neutral pass, an adversarial persona surfaces real gaps")
**Output produced:** link or excerpt
**What I changed after reviewing it:** your judgement call — this is the line that proves you didn't just copy-paste AI output
```

That last field is the most important one in the entire portfolio: it's the direct answer to "did AI just do this for you?" Every entry needs at least one concrete edit you made.

**At least one entry must document a substantive override** — a real moment where you disagreed with and changed a meaningful judgment call Claude made (not a typo fix or a wording tweak). Flagged 20 Aug 2026 during a job-market review session: this single example is disproportionately valuable in an interview — more valuable than the entire efficiency tracker — because it's the clearest possible evidence that you're exercising real judgement rather than accepting AI output wholesale. Watch for a real instance during the build; when it happens, document it more carefully than a typical entry. **Two strong candidates already exist as of 24 Sept 2026** — the ball/rod-mill citation-verification catch (25 Aug 2026) and the failure-mode Pareto OSF-undercount fix (10 Sept 2026); see the Scope-Decisions-and-Limitations-Log for both.

---

## 5. Portfolio Packaging

### 5.1 GitHub repository structure

```
mining-ba-reliability-project/
├── README.md                          # Elevator pitch, repo map, data disclosure, how to navigate
├── 00-Assumptions-Log.md
├── 01-Project-Charter.md
├── 02-Stakeholder-Register.md
├── 03-BRD-Maintenance-Reporting.md
├── 04-Process-Maps/                   # diagrams + a short md explainer
├── 05-Data-Dictionary.md
├── EDA-Findings.md                    # unnumbered — no slot reserved for it in this structure; renamed 24 Sept 2026 to clear a collision with 06-Business-Case.xlsx
├── 06-Business-Case.xlsx
├── 07-User-Stories.md
├── 08-Test-Cases.md
├── 09-Benefit-Realization-Report.md
├── 10-Traceability-Matrix.xlsx
├── 11-Job-Fit-Matrix.md               # Real Perth job-ad requirements mapped directly to deliverables
├── 12-ML-Proof-of-Concept.md          # OPTIONAL, build last — Module A, predictive maintenance proof-of-concept (+ notebook/script)
├── 13-LLM-Cause-Code-Classifier.md    # OPTIONAL, build last — Module B, LLM-based cause-code classifier (+ synthetic dataset + script/prompts)
├── data/
│   ├── raw/                           # original AI4I file, untouched, with source citation
│   ├── processed/                     # re-skinned mining dataset
│   ├── mining_reliability.db          # SQLite database (Week 2 SQL layer) + core query scripts
│   ├── data-lineage-note.md
│   └── llm-classifier-synthetic-cause-codes.csv   # Module B's synthetic input data, clearly labeled
├── dashboard/                         # .pbix or Tableau public link + screenshots
├── prompt-library/
│   └── (one .md per entry, indexed by an index.md)
├── efficiency-tracker/
│   └── Efficiency-Tracker.xlsx (+ a summary.md)
└── video-and-linkedin/
    ├── video-script.md
    └── linkedin-article.md
```

README should open with the elevator pitch (1.3), a one-line data disclosure ("Core dataset is a real UCI ML dataset re-skinned to a mining context — see data-lineage-note.md"), and a table of contents linking every numbered file. `12-ML-Proof-of-Concept.md` and `13-LLM-Cause-Code-Classifier.md` should both be listed last and described as "optional" in the table of contents — do not let either read as equal-weight to the core numbered deliverables.

### 5.2 Video walkthrough outline (target 6–8 minutes)

1. (0:00–0:45) Hook: the problem statement and why it matters, stated in plain business language, not BA jargon.
2. (0:45–2:00) Walk through the BRD and stakeholder register — show the red-team/critique pass catching a real gap, on screen.
3. (2:00–3:30) Process map: as-is vs to-be, the trade-off decision you made and why.
4. (3:30–5:30) Live dashboard walkthrough — the "so what," tied straight to the business case number.
5. (5:30–6:30) The efficiency story — show the tracker, state the honest numbers, name one specific quality catch.
6. (6:30–7:30) Close: what you'd do with more time/real data, and the prompt library as evidence of process. If you built either or both optional stretch modules, one sentence per module here is enough — do not give either more runtime than the core dashboard/business case walkthrough.

### 5.3 LinkedIn article outline + announcement post

**Article** (800–1200 words): open with the business problem (not "I used AI to..."), walk through the engagement like a case study, dedicate one clear section to the efficiency data with the honest caveats included, close with a link to the repo and video.

**Announcement post** (short): 3–4 sentences — the hook, one concrete number, one link. No hashtag stuffing.

### 5.4 One-page case study summary

Single page, resume-linkable: problem → approach (bullet the deliverable list) → one dashboard screenshot → the 2–3 headline efficiency numbers → links to repo/video/article. Build this **last**, once every number is final.

---

## 6. Recruiter-Facing Polish

### 6.1 Credibility checklist

Confirm before publishing: every number traces to the dataset, a cited source, or a labelled assumption; every prompt-library entry shows an edit you made, not just a paste; the README states plainly and early that this is a simulated engagement with synthetic/adapted data (never implies it's a real client); the efficiency numbers include at least one honest caveat or a task where AI *didn't* help much; and the writing sounds like you, not like unedited AI output (read it aloud — clunky repeated sentence structures are the tell).

### 6.2 Handling "did AI just do this for you?" directly

Answer it before it's asked: dedicate a short README/article section to *how* you used Claude — drafting vs. critique vs. code vs. research — and point straight at the prompt library's "what I changed" fields as evidence. The honest framing to practice out loud: *"Claude drafted faster than I could type, but the requirements gaps it caught only mattered because I knew what a real gap looks like — the judgement calls were mine, and I can show you exactly where."* For the LLM classifier module specifically, the honest framing is slightly different and worth practicing separately: *"Claude is the classifier being demonstrated, not just my drafting assistant on this one — my judgement went into the taxonomy design and the adversarial evaluation set, and I'm showing you exactly where it got things wrong, not just where it worked."*

### 6.3 Likely interview questions + how to answer

See `Interview-Prep-QA.md` in this project for the full, continuously-updated question bank (this section's original 10 questions are Section A there, plus additional questions surfaced during tutoring sessions).

---

## 7. Risks & Pitfalls (and how this plan avoids them)

Over-claiming AI's contribution is the single most common failure mode — avoided here by requiring an honest-caveat field in every tracker row and a "what I changed" field in every prompt-library entry. Generic industry knowledge with no real grounding is avoided by anchoring the business case and safety module in real WA/MSHA data rather than invented statistics. No evidence of judgement/critical thinking is avoided by making the critique/red-team loop a graded, documented step in nearly every week rather than a one-off gesture. Treating the dataset as if it were real mining data (implicit fabrication) is avoided by the mandatory data-lineage disclosure in the README and data folder. Confusing the operational dataset with the grounding/citation sources — e.g., trying to "clean and merge" WorkSafe or Geoscience Australia data the way AI4I is cleaned — is avoided by the explicit distinction in Section 1.2. Scope creep from the optional stretch modules diluting the core BA story is avoided by their locked scopes, "build last," and "never the headline" guardrails in Section 2 — now applying to two modules instead of one, which raises rather than lowers the discipline needed to hold that line. Finally, a portfolio that's technically complete but reads as a checklist rather than a story is avoided by building the elevator pitch and the "so what" business case *first* (Week 1 and Week 3) and writing every later deliverable to serve that narrative, rather than assembling documents for their own sake.

---

## Next steps

1. Confirm you're happy with the scenario lock in Section 1.1 — if you'd rather run the safety-trends scenario as the spine instead of the bonus module, say so now, before Week 1 work starts.
2. Set up the repo skeleton from Section 5.1.
3. Start `00-Assumptions-Log.md` and `Efficiency-Tracker.xlsx` today — both need to be live from Day 1, not backfilled.
4. When you finish each task, come back here and log it — I'll prompt you for the efficiency-tracker entry and flag which prompting technique to log in the library.
5. Both optional stretch modules (Section 2) only get built after everything else, including the Flex/Polish Week's sequencing note — don't let either creep earlier.
6. Right now: download AI4I 2020 (the only dataset that needs downloading at this stage) and get it into the project workspace — WA WorkSafe and Geoscience Australia figures get pulled later, as citations, not downloads (see Section 1.2).
7. Before Week 2 Day 9: source the two external repair-time (MTTR) and repair-cost benchmarks, and decide the AI4I-rows-to-one-asset mapping approach — both flagged 24 Aug 2026 in the Scope-Decisions-and-Limitations-Log after confirming AI4I has no repair-time or repair-cost fields of its own.
8. **Status as of 24 September 2026:** Weeks 1–2 and Week 3 Day 10 (EDA) are complete. Live position is Week 3, Days 11–12 (dashboard build, in progress). See `Reconciled-Finish-Schedule.md` for the concrete day-by-day plan covering everything remaining, including both optional stretch modules.
</content>
