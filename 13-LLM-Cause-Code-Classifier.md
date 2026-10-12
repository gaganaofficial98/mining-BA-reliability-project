# 13 — LLM Cause-Code Classifier (Module B, Optional Stretch Module)

**Status: optional demo/stretch module, NOT a formal engagement requirement.** Per `00-Master-Plan.md` Section 2, this sits outside the locked BRD/traceability-matrix scope — it is not folded into `03-BRD-Maintenance-Reporting.md` as approved FR-14, is not in `10-Traceability-Matrix.xlsx`, and is not covered by `08-Test-Cases.md`'s acceptance-criteria machinery. It exists to demonstrate applied LLM/NLP range alongside Module A's classical ML proof-of-concept, never as the headline of this project.

**Data note — read before anything below:** every free-text work-order entry used in this module is **synthetic** — written by hand (with Claude's drafting help) to resemble the kind of messy, inconsistent cause-code entries a real CMMS export would contain, not pulled from any real system. AI4I 2020 has no free-text field at all, so this data could not have been sourced any other way. It must never be presented as a real CMMS export, in this document or anywhere this project is shown.

**Why this module exists:** the Maintenance Superintendent – Fixed Plant interview (3 Sept 2026) named a specific, credible pain point: the CMMS's cause-code field is a roughly 40-option dropdown, and about half those options don't fit real failure descriptions, so technicians pick "close enough" rather than accurate. That finding produced proposed requirement **FR-14** (`04-Process-Maps.md` Section 10; `Scope-Decisions-and-Limitations-Log.md`, 4 Sept 2026) — logged as "proposed, not yet built," pending exactly this kind of decision. This module is that decision, exercised as a bounded demo rather than a formal requirement: it tests whether an LLM can do the messy-text classification a rules-based dropdown redesign can't cleanly solve.

---

## 1. Target taxonomy

Seven mutually-exclusive categories: AI4I 2020's own five real failure-mode labels, plus two additional categories named directly by this project's own interviews, which AI4I's taxonomy doesn't cover at all.

| Code | Category | Source | Definition used for classification |
|---|---|---|---|
| TWF | Tool Wear Failure | AI4I 2020 | A cutting tool, liner, blade, insert, or wear part has physically worn down. |
| HDF | Heat Dissipation Failure | AI4I 2020 | Heat/thermal buildup (overheating, cooling failure) is the proximate driver. |
| PWF | Power Failure | AI4I 2020 | Torque/power-supply mismatch to the driven load — undertorque, overtorque on startup, stalling under load. |
| OSF | Overstrain Failure | AI4I 2020 | A mechanical component failed because physical load/strain exceeded its rated limit — acute overload, not gradual wear. |
| RNF | Random Failure | AI4I 2020 | No identifiable cause after inspection; genuinely unexplained. |
| ELEC | Electrical fault | **New — Instrumentation & Controls Engineer interview** | Wiring faults, short circuits, contactor/breaker failures, earth faults — faults in the electrical circuit itself, distinct from power-to-load mismatches (PWF) and heat (HDF). |
| INST | Instrumentation/sensor fault | **New — Instrumentation & Controls Engineer interview; also raised by Maintenance Superintendent – Fixed Plant** | A sensor, transmitter, or measurement device is miscalibrated, drifted, or physically faulty — the fault is in the measurement system, not the asset being measured. |

The two new categories were chosen deliberately, not arbitrarily: ELEC and INST are exactly the categories the real ~40-option dropdown PP2 describes conflating with AI4I's five modes (per the interview), so a taxonomy that only used AI4I's five labels would force every electrical or sensor-related entry into an ill-fitting category — reproducing the exact PP2 problem this module exists to fix, rather than solving it.

---

## 2. Synthetic dataset

51 rows, built by hand against the taxonomy above: `data/llm-classifier-synthetic-cause-codes.csv`. Roughly 6–9 rows per category, plus 6 **deliberately adversarial** rows designed to test judgment under ambiguity, not just easy pattern-matching — per the locked scope's explicit instruction to "design the hand-labeled evaluation set adversarially (deliberately include a few ambiguous/edge-case entries, don't only test on easy ones)."

The adversarial rows (WO-046 through WO-051) each embed two plausible causes in one entry — a root cause and a downstream consequence, or two genuinely co-occurring issues — deliberately mirroring the same kind of multi-cause ambiguity that the Day 9 SQL tie-break bug exposed in the AI4I data itself (`Scope-Decisions-and-Limitations-Log.md`, 10 Sept 2026; `Prompt-Library.md` Entry 9). Each adversarial row's ground-truth label was adjudicated by Gagana with a written justification for why one cause was treated as proximate/primary over the other, **before** the classifier saw any of the data — see the `adjudication_note` column in the CSV.

---

## 3. Methodology — how the classification was actually run

**The dual-role disclosure the Master Plan requires (Section 2, Module B guardrail):** Claude is the classifier under test in this module, not merely a drafting assistant helping build one. To make that test genuinely blind rather than Claude grading its own answer key, the classification was run as a **separate, memory-isolated subagent** with no access to this conversation, the ground-truth labels, or the adjudication notes — the same fresh-context isolation technique already used for the BRD red-team (`Prompt-Library.md` Entry 5) and the SQL OSF-undercount review (Entry 9), applied here for the first time as the actual deliverable being tested, not just a quality-control step on something else.

The subagent was given only: the taxonomy definitions (Section 1 above, worded as classification instructions) and the 51 raw free-text entries with their work-order IDs — no labels, no hints about which rows were adversarial, no context about this project. It was instructed to pick the single best-fitting category per entry, based on the stated root cause or proximate trigger where an entry described two things happening together, and to make its best judgment call on every row rather than asking for clarification.

**What this blind-subagent approach does and doesn't solve:** it genuinely prevents the trivial failure mode of the same context that wrote the "answer" also writing the "prediction" with memory of what it intended. It does **not** solve a deeper limitation, disclosed plainly in Section 6: the entries themselves were written by an LLM-assisted process in the first place, which means their vocabulary may be unconsciously aligned with how an LLM classifier reasons about these categories, in a way a genuine real-world CMMS export's messier, more inconsistent phrasing would not be.

---

## 4. Results

**Overall: 50 of 51 correctly classified (98.0%).**

| Category | TP | FP | FN | Precision | Recall |
|---|---|---|---|---|---|
| TWF | 8 | 0 | 0 | 100.0% | 100.0% |
| HDF | 9 | 0 | 0 | 100.0% | 100.0% |
| PWF | 6 | 1 | 0 | 85.7% | 100.0% |
| OSF | 9 | 0 | 0 | 100.0% | 100.0% |
| RNF | 6 | 0 | 1 | 100.0% | 85.7% |
| ELEC | 6 | 0 | 0 | 100.0% | 100.0% |
| INST | 6 | 0 | 0 | 100.0% | 100.0% |

**The one miss, examined rather than glossed over — WO-048:**
> "Conveyor stopped, nothing obviously wrong, but we did have a power dip on site 10 min prior"

Ground truth (Gagana's pre-registered adjudication): **RNF**, reasoned as follows — the entry does not assert the power dip *caused* the stoppage, only that it occurred nearby in time; treating a merely correlated event as a confirmed cause is exactly the kind of unearned causal leap this project's own attribution-critique discipline (`Prompt-Library.md` Entry 10) exists to catch.

Classifier's call: **PWF**, with its own stated reasoning — "entry supplies a plausible cause (power dip 10 min prior) rather than stating no cause found, so classified as power-related rather than RNF."

**This is reported as a genuine, defensible disagreement, not simply an error.** A reasonable reviewer could side with either call — the classifier's logic (a stated candidate cause, however loosely connected, outweighs declaring "no cause found") is coherent and arguably the more common real-world convention; Gagana's adjudication applied a stricter causal-evidence standard consistent with this project's own attribution-critique framework. Presenting this as "the classifier made an error" would overstate how clear-cut the correct answer actually is — the more honest statement is that the two adjudicators (Gagana and the classifier) used different, both-defensible thresholds for how much causal evidence an entry needs before it stops counting as "random."

All five other adversarial rows (WO-046, WO-047, WO-049, WO-050, WO-051) were classified in agreement with Gagana's pre-registered adjudication, including the hardest one (WO-049, a genuinely two-stage failure where the classifier correctly identified the instrumentation fault as the stated root cause rather than keyword-matching on the downstream "overheated" symptom to HDF).

---

## 5. Honest limitations (per the locked scope's "no naive metric" discipline)

**The 98% figure should not be read as a validated real-world accuracy rate, and this document does not claim it is one.** Three specific reasons, stated plainly rather than left implicit:

1. **Same-origin bias.** The 45 non-adversarial entries were written with enough lexical signal for their intended category that a reasonably careful reader — human or model — would be expected to classify most of them correctly. A near-perfect score on data built this way is evidence the classifier isn't making careless category confusions on clear-cut cases; it is not evidence the classifier would perform this well against a real CMMS export's genuine messiness (typos, trade jargon, incomplete sentences, multiple truly tangled causes with no clean "proximate trigger" to identify).
2. **The adversarial subset (6 of 51 rows) is the more honest signal**, and even there, performance (5/6 matching the pre-registered adjudication) should be read alongside the fact that the one disagreement was a coherent, defensible alternative reading — not a case of the classifier missing an obvious answer.
3. **Evaluator and classifier share a common ancestor.** Blind subagent dispatch prevents the classifier from literally seeing the ground truth, but it does not create true independence between the entries' author and the classifier the way a held-out real-world dataset and a human-labeled benchmark would. This is disclosed here rather than left for a skeptical reader to discover on their own.

**What this module validates, stated at the same confidence level as Module A's own framing:** that an LLM can apply a structured, multi-category taxonomy to messy free text and make reasoned, explainable judgment calls on genuinely ambiguous multi-cause entries — including correctly identifying a root cause over a more lexically obvious downstream symptom (WO-049). It does **not** validate production-ready accuracy against a real CMMS export, which would need a real, messier dataset and genuinely independent human labeling to assess credibly. Deploying this against a real CMMS export would be a phase-2 initiative outside this engagement's locked scope, exactly as Module A's write-up frames its own result.

---

## 6. Relationship back to FR-14 and the interview finding

This module does not resolve FR-14's open validation items (CMMS/IT system-owner feasibility, cross-check against AI4I's taxonomy for the four AI4I-only questions) — those remain genuinely open per `03-BRD-Maintenance-Reporting.md` Section 13.9 and `04-Process-Maps.md` Section 10. What this module does show is that the *category of fix* FR-14 proposes — a smaller, cleaner taxonomy that actually maps to real failure descriptions — is one an LLM can apply consistently and explain its reasoning for, which is directly relevant evidence for a future BRD v3 conversation about whether FR-14 should become a formal requirement, and whether an LLM-assisted classification step (rather than a purely manual dropdown redesign) is worth considering as part of that requirement's actual implementation.
