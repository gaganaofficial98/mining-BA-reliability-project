# One-Page Case Study Summary

**Deliverable:** the one-pager referenced in `00-Master-Plan.md` §5.1/§5.4 (resume-linkable single page)
**Owner:** Gagana Suresh
**Status:** Draft v1 — 1 October 2026. Built last, as the Master Plan requires, once the headline numbers below were final. **Two things are still outstanding and must be filled in before this is published or linked from a resume:** the dashboard screenshot (placeholder noted below — this text-only session has no way to capture one) and the repo/video/article links (none exist yet — see `Reconciled-Finish-Schedule.md`). Module A (the classical ML proof-of-concept) is in progress, not finished, as of this draft — see the note under "Approach."

---

## Mining Maintenance Reliability Reporting — A Simulated BA Engagement with Claude

**The problem.** A mining maintenance function was losing production hours to unplanned equipment breakdowns and couldn't answer, in a single report, which asset class, failure mode, or shift was driving the loss. Maintenance data existed but reporting was manual, inconsistent across planners, and couldn't support root-cause analysis.

*Disclosure: this is a simulated engagement for a fictional company (Corvus Resources), built on a real, publicly available industrial dataset (AI4I 2020) re-skinned onto a synthetic mining asset register. Every synthetic element is flagged throughout the full project documentation.*

**Approach.**
- Simulated stakeholder interviews across six mining-operations personas, feeding a formally red-teamed Business Requirements Document
- As-is and to-be process maps, including a documented three-option trade-off decision on the project's single highest-friction process step
- A Tableau reliability dashboard built on a re-skinned, SQL-queried version of the dataset, with a documented mid-project correction to its failure-mode ranking
- A cost-of-downtime business case grounded in two independent, cited external benchmarks, reported as a range rather than a false-precision point estimate
- A benefit realization report built against a recognized benefits-dependency framework, including an attribution critique that downgrades the project's own largest financial claim pending further validation
- A full requirements traceability matrix, which itself surfaced and triggered the resolution of a real analysis gap
- Two optional stretch modules demonstrating range beyond core BA deliverables: an LLM-based cause-code classifier (complete, blind-evaluated) and a classical ML proof-of-concept (**in progress** as of this draft — update this line with its real result once built, per `Reconciled-Finish-Schedule.md`)
- A documented prompt library (14 entries) and a task-by-task efficiency tracker, logged live rather than reconstructed afterward

**[DASHBOARD SCREENSHOT PLACEHOLDER — insert a screenshot of the Failure Mode Pareto and Failure Rate by Tier worksheets here before publishing. Live dashboard: https://public.tableau.com/app/profile/gagana.suresh.vatal/viz/MiningFleetReliabilityDashboard_/MiningFleetReliabilityDashboard]**

**Headline numbers.**
- **$1.7M–$6.5M** estimated downtime loss on the Mobile fleet alone over the analysis period, from 83 real recorded failures and two independently cited cost-of-downtime benchmarks (reported as a range, not a single point estimate, because the two real sources disagree by roughly 4x)
- **~180x** — the size of a formula error caught before delivery during the business-case build (a referenced rate cell not multiplied by hours), via a multi-pass self-verification step; one of two documented moments in this project where a genuine mistake was found and fixed with full disclosure, not quietly corrected
- **6 of 11** process pain points fully closed by the recommended redesign, 2 partially closed, 2 genuinely still open, 1 permanently out of scope — an honest scorecard, not a claimed clean sweep

**Links.** Full repository: **[REPO LINK — not yet live]** · Video walkthrough: **[VIDEO LINK — not yet recorded]** · LinkedIn article: **[ARTICLE LINK — drafted, not yet posted]**

---

### Before this is linked from a resume or sent to anyone

1. Replace the dashboard screenshot placeholder with a real image.
2. Replace all three bracketed links once the repo exists, the video is recorded, and the article is posted — in that order, per `Reconciled-Finish-Schedule.md`'s remaining sequence.
3. If Module A is complete by the time this is finalized, update its bullet under "Approach" with its real, honestly-reported precision/recall result rather than leaving it as "in progress."
4. Re-check the three headline numbers above against whatever is live in the repo at that time — they're accurate as of 1 October 2026, and this project's own convention (see the Scope-Decisions-and-Limitations-Log's consistency-audit entry from today) is to re-verify numbers before republishing them, not assume they're still current.
