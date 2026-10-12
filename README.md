# Mining Maintenance Reliability Reporting — BA Portfolio Project

**Reducing Unplanned Equipment Downtime & Improving Maintenance Reliability** — a simulated Business Analyst engagement for a mining fleet and fixed-plant maintenance function, built to demonstrate professional-standard BA work and skilled, disclosed use of Claude as an AI collaborator throughout.

**Owner:** Gagana Suresh — Early-career Business Analyst, Perth WA

## Live dashboard

The Tableau Public dashboard built from this project's data is live here: **[Mining Fleet Reliability Dashboard](https://public.tableau.com/app/profile/gagana.suresh.vatal/viz/MiningFleetReliabilityDashboard_/MiningFleetReliabilityDashboard)**. It isn't hosted as a file in this repo — Tableau Public dashboards are published and viewed through Tableau's own hosting, not downloaded `.twb`/`.twbx` files — so this link is the dashboard's actual home, not a placeholder for a missing file.

## What this is

This repo simulates a real BA consulting engagement end-to-end: stakeholder interviews, requirements elicitation, process mapping, a data model and SQL layer, a user story backlog and test suite, a requirements traceability matrix, a benefit realization report, two optional stretch modules (an ML proof-of-concept and an LLM-based cause-code classifier), a published dashboard, and a business case — all built the way an actual engagement would be run, with the same rigor a hiring manager would expect from paid client work.

**Data disclosure, up front:** the core dataset (AI4I 2020, a real UCI Machine Learning Repository dataset) is generic industrial sensor data, not mining-labelled. It has been re-skinned onto a synthetic 48-asset mining fleet built for this project — see `data/reskin_deal.py` for the exact, reproducible, auditable method used. No real confidential company data appears anywhere in this repo. Every number in every deliverable is tagged as one of: real dataset value, a cited external source, or a disclosed labeled assumption — never presented ambiguously.

**Stakeholder interviews are simulated**, standing in for stakeholders this portfolio project has no access to — grounded in real mining organisational structures and interviewed through persona-prompted, multi-turn conversations, one fresh context per role. This is disclosed plainly in `discovery/` and in the BRD's own methodology section, including an honest limitation: the six personas are not truly *independent* evidence, since all six were generated from the same underlying process.

## A note on this repo's commit history

Most of this project's actual work happened inside a series of chat sessions, not commit-by-commit in a local git client — the files existed in a working document set before this repository did. Rather than start the visible history from a single "add everything" commit on the day the repo was created, each file below has been committed at the real calendar date it was substantively finished or last meaningfully revised (drawn from each document's own dated status line, or from the dated decision log entry that changed it). Where a file went through more than one real revision (for example, the BRD's v1 draft and its later red-team-critique v2), only the final state is committed, under the date of its last substantive revision — the intermediate draft was not preserved as a separate file, so this repo does not fabricate a synthetic diff between them. This is disclosed here rather than presented as a perfectly granular, moment-by-moment original history.

## Repo map

| Path | What's in it |
|---|---|
| `00-Master-Plan.md` | The project's own execution plan — scenario selection, data sourcing, week-by-week deliverable schedule, locked repo structure |
| `00-Assumptions-Log.md` | Running, numbered index of every labeled assumption used anywhere in the project, cross-referenced to `governance/Scope-Decisions-and-Limitations-Log.md` |
| `01-Project-Charter.md` | Scope, governance model (Sponsor/Business Owner split), constraints |
| `02-Stakeholder-Register.md` | 10–14 real roles, tiered by power/interest, with a disclosed open naming question |
| `03-BRD-Maintenance-Reporting.md` | Business Requirements Document (v2, post red-team critique) |
| `04-Process-Maps.md` | As-Is and To-Be swimlane process maps, gap analysis, the Step 4 governance-fix decision |
| `05-Data-Dictionary.md` | Field-by-field spec of the merged dataset, plus every external benchmark decision and its reasoning |
| `EDA-Findings.md` | Exploratory data analysis answering all six locked business questions (Q1–Q6), including the pre-registered Q5/Q6 statistical threshold analysis |
| `06-Business-Case.xlsx` | 5-tab linked Excel model (Summary, Assumptions & Sources, Current-State Cost, Projected Savings, Limitations) — cost-of-downtime business case with sourced Low/High sensitivity range |
| `07-User-Stories.md` | 17-story backlog across 8 epics, each traced to a BRD functional requirement |
| `08-Test-Cases.md` | 49 test cases with full traceability and documented edge cases |
| `09-Benefit-Realization-Report.md` | Benefits Dependency Network (Ward & Daniel), an attribution critique of every claimed benefit, 6 post-launch KPIs |
| `10-Traceability-Matrix.xlsx` | 5-tab linked workbook mapping every FR to its BR, user stories, test cases, and dashboard element, with live COUNTIF/COUNTIFS formulas |
| `11-Job-Fit-Matrix.md` | How this project's deliverables map to real Perth BA/analyst job postings |
| `12-ML-Proof-of-Concept.md` | Optional Module A: a scoped predictive-maintenance proof-of-concept |
| `13-LLM-Cause-Code-Classifier.md` | Optional Module B: an LLM-based cause-code classifier |
| `governance/Scope-Decisions-and-Limitations-Log.md` | The running record of every scope decision, data limitation, and disclosed methodology choice made across the project |
| `discovery/` | Six simulated stakeholder interview transcripts + the interview-prep Q&A bank |
| `process-maps/to-be-process-map.html` | Standalone visual rendering of the To-Be process map |
| `data/` | The re-skin script, the merged dataset, the SQLite database, and the load/verification script |
| `efficiency-tracker/Efficiency-Tracker.xlsx` | Task-by-task manual-time-vs-actual-time log — the evidence behind the "AI made me faster" claim |
| `portfolio-tracker/discovery-sprint.html` | A visual day-by-day progress tracker built alongside the project itself |
| `prompt-library/Prompt-Library.md` | 15 fully documented prompting-technique entries (context / prompt / why / output / what was changed after review), including two substantive-override entries |
| `video-and-linkedin/` | Video walkthrough script, LinkedIn article, and one-page case study summary |
| `working-notes/` | Plain-language flowchart explainers built during the project to check understanding before proceeding |

## Status

All core deliverables (00 through 13) are complete, along with the published Tableau dashboard, the full prompt library, and the efficiency tracker. See `00-Master-Plan.md` for the full schedule and `governance/Scope-Decisions-and-Limitations-Log.md` for the complete, continuously-updated decision record.
