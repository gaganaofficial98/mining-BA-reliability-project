# Interview Prep — Question & Answer Bank

**Owner:** Gagana Suresh
**Purpose:** One place to find every interview-style question likely to come up about this project, with a ready answer — so you never have to scroll back through chat history to find "that question Claude flagged." I'll keep adding to this file as new questions surface across our sessions (from planning, from you asking me something, or from me spotting a likely follow-up).
**Last updated:** 3 September 2026

**How to use this file:** Each entry gives you the question, a short spoken-style answer in your own voice (not corporate-sounding), and — where relevant — the specific file/evidence in the repo you'd point to if pushed for detail. Read through it before an interview or presentation; don't try to memorize word-for-word, memorize the *shape* of the answer and the evidence trail.

---

## Section A — Core questions (from the Master Plan's built-in prep list)

These were baked into the project plan from day one (Master Plan, Section 6.3) because they're the questions almost any BA interviewer asks about a portfolio project like this.

### 1. "Walk me through your BRD process."
Narrate the loop: elicitation (simulated stakeholder interviews) → first draft BRD → red-team critique pass (adversarial persona) → revised BRD v2. Name one specific gap the critique pass caught and how you resolved it — don't just describe the process abstractly, cite the actual gap once you have one logged.
*Evidence: `03-BRD-Maintenance-Reporting.md`, the v1→v2 diff, prompt-library entry for the critique-loop prompt.*

### 2. "Where did AI actually save you time, specifically?"
Cite two concrete entries from the efficiency tracker with real numbers (e.g., "BRD first draft: est. 5 hrs manual → 2.1 hrs with Claude"), not a vague average or a headline multiplier. Specific beats impressive.
*Evidence: `Efficiency-Tracker.xlsx`.*

### 3. "Where did AI get something wrong, and how did you catch it?"
Have a real example ready — don't invent one, watch for it during the build and log it when it happens. This question is coming; an interview answer with no real example here is a red flag to an experienced interviewer.
*Evidence: TBD — log the first real instance in the Efficiency Tracker's "honest caveat" field when it happens.*

### 4. "Why this dataset, and is it really representative of mining?"
Give the honest answer: it's a real UCI ML dataset (AI4I 2020), generic industrial context, deliberately re-skinned onto a synthetic mining asset register with a documented mapping table. Say plainly what you'd want from real data instead (site-specific failure modes, real cost-of-downtime figures, actual CMMS export data). If pushed further, you now also have the rejected-alternative story (see Q16) as evidence of real source vetting.
*Evidence: `data/data-lineage-note.md`, the asset register mapping table.*

### 5. "How did you validate your business case assumptions?"
Point to the Assumptions Log and the finance-persona critique pass ("where would Finance push back on these numbers?").
*Evidence: `00-Assumptions-Log.md`, `06-Business-Case.xlsx`.*

### 6. "What would you do differently with a real client?"
Real stakeholder interviews instead of simulated ones, real historical cost-of-downtime data instead of an industry benchmark assumption, a longer requirements validation cycle with actual sign-off from multiple stakeholders.

### 7. "Which stakeholder would have pushed back hardest, and how would you handle it?"
Use the simulated Finance vs. Ops tension from Week 1 (Finance wants cost cuts, Ops wants uptime) — shows you understand conflicting priorities, not just documentation.
*Evidence: Week 1 simulated interview transcripts.*

### 8. "Show me a requirement you cut from scope, and why."
Have one ready from the BRD's out-of-scope section with a real reason (not just "we ran out of time").
*Evidence: `03-BRD-Maintenance-Reporting.md`, out-of-scope section.*

### 9. "How do you know your dashboard answers the right question?"
Trace it back to a specific stakeholder need in the traceability matrix — don't just describe the dashboard, show the line from stakeholder need → requirement → dashboard element.
*Evidence: `10-Traceability-Matrix.xlsx`.*

### 10. "What's the single biggest limitation of this project as evidence of your skills?"
Answer honestly — likely candidates: simulated stakeholders (not real ones), one core dataset re-skinned rather than multiple real sources, no actual CMMS access. Naming your own limitation unprompted reads as more senior than pretending there isn't one.

---

## Section B — Questions surfaced during tutoring sessions

### 11. "What's a CMMS, and where does it fit into your project?"
*(Raised: 20 Aug 2026, tutoring session on project fundamentals)*

**Spoken answer:** "CMMS stands for Computerized Maintenance Management System — it's the software maintenance teams use to log work orders and track repairs. In my project, the company already has one, but leadership can't get a clear answer out of it about which assets or failure modes are driving downtime. So my job as the BA was to specify a reporting enhancement to that existing system, not build a new one — which is actually the more realistic and common BA engagement."

**Likely follow-up:** "Which CMMS did you assume they're using, and did that shape your requirements?" — see Q13 below, this is currently an **open gap**.

### 12. "Did you have real CMMS software for this project, or are you building one, or do you only have the data?"
*(Raised: 20 Aug 2026, tutoring session on project fundamentals)*

**Spoken answer:** "I didn't have access to a real CMMS, and building one wasn't the point of the exercise — a BA doesn't build the software, we write the requirements for it. I treated the existing CMMS as a black box that already logs work orders and failure data, used a re-skinned real-world sensor dataset to simulate what that data would actually look like, and focused on the BA deliverables: requirements, reporting gap analysis, and a Power BI prototype showing what better reporting would look like. That's the same handoff a BA gives a dev team in a real CMMS enhancement project."

**Key distinction to hold onto under pushback:** the Power BI dashboard is a *prototype/mockup of the reporting output*, not the CMMS itself — don't let an interviewer's phrasing push you into implying you built or modified actual CMMS software.

### 13. OPEN GAP — "Which specific CMMS platform did you assume, and did that shape your requirements?"
*(Flagged: 20 Aug 2026 — not yet resolved)*

This one doesn't have a locked answer yet. The project currently doesn't name a specific assumed CMMS platform (e.g., SAP PM, IBM Maximo, Fiix), which weakens the credibility of the functional requirements — generic requirements read as generic. **Action needed:** add a line to `00-Assumptions-Log.md` naming an assumed platform and its rough capability tier, e.g. *"Client CMMS assumed to be a mid-tier platform (Maximo-class) with basic work-order logging but no cross-asset reporting or dashboarding capability."* Once that's written, come back to this entry and convert it into a normal answered Q&A.

### 14. "Why did you add SQL to a BA project — isn't that a data engineer's job?"
*(Raised: 20 Aug 2026, following a Perth BA/analyst job-market review)*

**Spoken answer:** "I pulled current Perth BA and analyst job postings rather than guess what's expected, and SQL came up constantly — it wasn't in my original plan, and I didn't want a gap between what the market actually asks for and what I'd built. So I added a small SQLite layer: the cleaned dataset lives in an actual queryable database, and the core analytical queries — downtime by asset class, failure-mode Pareto, MTBF and MTTR — are written in SQL and feed the dashboard measures directly, instead of sitting in an Excel formula. It's not about pretending to be a data engineer, it's that querying your own data is a baseline expectation for this kind of analyst role now, and I'd rather show it than explain its absence."

### 15. "Which companies or organizations is this project relevant to?"
*(Raised: 20 Aug 2026, following a Perth BA/analyst job-market review)*

**Spoken answer:** "I looked at which Perth-based mining and resources companies are actively hiring BA and analyst roles right now — Fortescue, BHP, Rio Tinto, South32, Lynas, Talison Lithium, WesTrac, Macmahon, and Epiroc all came up — so I understand the kind of operating context this project would sit in. I want to be upfront though: this isn't built for any of them specifically, it's a simulated engagement with synthetic and adapted public data. I looked at that landscape for my own interview fluency, not to imply a real client relationship."

**Guardrail:** never phrase this as "I did this for [Company]" — that crosses into the exact fabrication trap the project's credibility checklist (Master Plan Section 6.1) is built to avoid. Company knowledge is for speaking fluently about the industry, not for claiming a client.

### 16. "You mentioned evaluating and rejecting a dataset — walk me through that."
*(Raised: 20 Aug 2026, following the dataset-pairing decision)*

**Spoken answer:** "I looked at the Quality Prediction in a Mining Process dataset from Kaggle — it's real sensor data from an actual iron-ore flotation plant, so on paper it looks like the more 'authentically mining' choice. But it's process and quality data with no work-order structure — no breakdown, no repair, no technician assigned — and my whole project is built around that work-order lifecycle. So I made the call to use it as supporting evidence of my data vetting process rather than my core dataset, and went with AI4I 2020 instead, which has real row-level failure and sensor data I can actually compute MTBF, MTTR, and failure-mode Pareto stats from. It's a generic industrial dataset rather than a mining one, so I re-skinned it onto a synthetic mining asset register with a documented mapping table — that trade-off is disclosed openly in the repo."

**Why this question matters:** this is one of your strongest "judgment under trade-offs" stories — it shows you didn't just grab the first "real mining data" you found, you evaluated it against what the project actually needed and made a defensible call. Worth having ready even if not asked directly — it can answer Q4 with more depth if there's a follow-up.

### 17. "What's an example of you genuinely overriding or disagreeing with Claude, not just fixing a typo?"
*(Flagged: 20 Aug 2026, following a job-market review session — currently an OPEN GAP, no real example logged yet)*

This is closely related to Q3 but sharper: Q3 asks where AI was *wrong*; this asks where you made a *judgment call* Claude wouldn't have made on its own, even if Claude's output wasn't technically incorrect. The distinction matters because this is, by a wide margin, the single most valuable story in your whole prompt library — more persuasive in an interview than the entire efficiency tracker — because it's direct proof you're driving the work, not accepting output. **Action needed:** as you build, actively watch for a moment where you push back on a Claude-proposed requirement, stakeholder priority, dashboard design choice, or business case assumption for a real reason — then document it as a full prompt-library entry with extra care, and come back here to convert this into an answered entry with the real story.

### 18. "Why did you add a predictive model — isn't that a data scientist's job, not a BA's?"
*(Raised: 20 Aug 2026, when the optional ML proof-of-concept module was locked into the plan)*

**Spoken answer:** "AI4I 2020 was actually built as a machine learning dataset — it has a failure label and five failure-mode categories sitting right alongside the sensor readings, so I couldn't ignore that it supported a predictive angle. Rather than skip it or build something over-engineered, I scoped a small, honest proof-of-concept: one model, evaluated properly, framed explicitly as validating whether predictive maintenance is worth pursuing as a phase-two initiative — not as a production system. That's still a BA judgment call: knowing when a predictive model earns its place in scope and proving the case for it, rather than either dismissing the possibility or overreaching into a data scientist's job."

**Technical follow-ups this module specifically invites — have real answers, not rehearsed ones, once it's built:**
- *"Why logistic regression / random forest and not something else?"* — answer with the actual reason you picked it (interpretability, it's the standard defensible baseline for a proof-of-concept, whatever your real reason was), not a generic "it's popular" line.
- *"How did you handle the class imbalance?"* — this is the one a technically sharp interviewer will ask first, because most machines in AI4I don't fail. Be ready to say specifically what you did (e.g., class weighting, resampling, or simply choosing to report precision/recall instead of accuracy) — "I used accuracy" is the wrong answer and a real risk if the model isn't evaluated carefully.
- *"Why precision/recall over accuracy?"* — because on an imbalanced dataset a model can hit high accuracy by always predicting "no failure," which is useless; precision/recall actually show whether it catches real failures.
- *"Would you productionize this — what would it take?"* — have a short honest answer (real historical data instead of AI4I, ongoing retraining, integration with the CMMS, model monitoring) that shows you know the gap between a proof-of-concept and a real system.

**Guardrail to hold under pushback:** never let this module's framing drift from "proof-of-concept validating a future direction" into "I built a predictive maintenance system" — that overstates what was actually delivered and is the exact over-claiming trap the project is built to avoid (Master Plan Section 6.1).

### 19. "You said you used Claude throughout this project — did you ever catch it doing something wrong, or being manipulated?"
*(Raised: 3 September 2026, resolving the open gap flagged at Q3/Q17 with a real instance)*

**Spoken answer:** "Yes, actually — a small but concrete one. When I brought one of my simulated interview transcripts back into the main project after drafting it in a separate chat, the pasted text had an instruction tacked onto the end of it telling the assistant to respond with text only and not use any tools — which wasn't something I wrote, and didn't make sense for the task, since saving and synthesizing a transcript requires writing to a file. It was caught as an injected instruction and ignored, and the actual task — saving the interview and pulling out the BA findings — went ahead normally. It's a small example, but it's a real one: it shows I'm not just trusting everything that comes through an AI-assisted workflow at face value, I'm watching for exactly this kind of thing."

**Why this one matters:** unlike Q13 or Q17 before it, this isn't a hypothetical "watch for this as you build" flag — it actually happened, which is what makes it usable. It's a different flavor of judgment evidence than Q3 (AI got a fact wrong) or Q17 (overriding a Claude-proposed judgment call) — this one is about AI-safety-adjacent awareness in a genuinely agentic, tool-using workflow, which is increasingly its own interview topic for "AI-augmented analyst" roles.

*Evidence: `Scope-Decisions-and-Limitations-Log.md`, "Process note — a prompt-injection attempt was detected and ignored in a pasted interview transcript (3 September 2026)."*

### 20. "Why does the 'quick fix beats proper repair' problem actually happen — isn't that just a communication or culture issue?"
*(Raised: 3 September 2026, following the Financial Controller interview)*

**Spoken answer:** "That's what I assumed too, going in — that it was basically a persuasion problem, production has a number and maintenance doesn't, so production wins the argument. Three stakeholders told me some version of that. But the Financial Controller, who's the one person who actually sees where the money goes, added something none of the other three could see: a lot of it isn't about whose argument is better, it's about which approval pathway each option sits in. A quick patch is usually opex and sits inside her own delegated sign-off authority, so it can be approved this week. A proper root-cause fix is often bigger dollars, ends up needing to be capex, and queues behind every other capital request on site — sometimes for months. So even when maintenance has a genuinely good case, the quick fix wins partly because it's the only one that's actually approvable on the timeline the problem is happening on. That reframed the finding for me — it's not just a reporting gap, it's partly a budget-structure gap, and a recommendation that only improves the numbers without also naming that approval-pathway mismatch would be solving half the problem."

**Why this one matters:** it's a good example of triangulating a finding across multiple interviews and having the last one sharpen or complicate what the first three suggested, rather than just repeating the same insight four times. It also shows the project's recommendation isn't purely a reporting/dashboard fix — it names a structural, process-level contributor too, which reads as more sophisticated analysis than a single-cause story.

*Evidence: `Interview-Transcript-Financial-Controller.md` (Q8), `Scope-Decisions-and-Limitations-Log.md` — the interview-list progress note dated 3 September 2026.*

### 21. "How do you know your precursor-pattern or threshold findings are real signal and not just sensor noise?"
*(Raised: 3 September 2026, following the Instrumentation & Controls Engineer conversation)*

**Spoken answer:** "Honestly, on this site, you couldn't fully know that — and that's actually one of the more interesting things I found during discovery, not something I'm glossing over. I checked with the person who'd own the instrumentation, and he told me there's no system anywhere that tracks when a given sensor was last calibrated or validated against a reference. He gave me two real examples where a trend that looked exactly like an early-warning failure signal turned out to be a fouled or drifting sensor instead — in his words, the two look identical on a chart. So my Q5 and Q6 findings are built on AI4I's real sensor columns and demonstrate that the method works when the underlying data is trustworthy — but I disclose plainly that deploying this against a real fleet would first need that calibration-provenance gap closed, and I actually carried that into the business case as its own recommendation, not just a footnote."

**Why this one matters:** it's a stronger answer than pretending the sensor data is unimpeachable, and it shows the project caught a real limitation through elicitation rather than glossing over it — the same pattern as the sub-threshold-stoppage and equipment-attributable-share findings. It also turns a potential weakness (a technically sharp interviewer probing whether the precursor findings are trustworthy) into a demonstration of rigor.

*Evidence: `Interview-Transcript-Instrumentation-Controls-Engineer.md` (Q4–Q5), `Scope-Decisions-and-Limitations-Log.md`, "Limitation — sensor-trend findings (Q5, Q6, and the optional ML module) cannot currently be distinguished from instrumentation drift or fouling at this site (raised 3 September 2026)."*

---

## Notes for future sessions

Add new entries here any time a real interview-style question comes up — whether I flag it as a likely follow-up, or you ask me something that's actually interview material in disguise. Keep the numbering sequential across sessions so cross-references stay stable. When an "open gap" entry gets resolved, rewrite it in place as a normal answered entry rather than deleting it — the fact that you closed a real gap during the project is itself good interview material (see Q3/Q10/Q13/Q17 territory).
