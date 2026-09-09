# Prompt Library — Index

**Status:** in progress. Candidate entries already identified during the build, to be written up in full per the Master Plan Section 4 format (context / prompt / why designed this way / output / what I changed):

1. **Prompt-to-code from an explicit spec + built-in verification** — `data/reskin_deal.py` and `data/load_to_sqlite.py`. Four-ingredient pattern: name the exact inputs, state the business rule as a testable sentence, require reproducibility, require the code to print its own proof (a violation count / sanity check) before trusting the output.
2. **Options analysis, decision deliberately left to the human** — the Step 4 fast-fix-vs-root-cause redesign (`04-Process-Maps.md` Section 8) and the Fixed-plant repair-cost gap (Option A/B, `governance/Scope-Decisions-and-Limitations-Log.md`, 1 Sept 2026) — Claude presented weighted options, Gagana made the call.
3. **Options analysis, recommendation given on request** — the Ancillary-tier repair-time aggregation decision (`05-Data-Dictionary.md` Section 3.2, 8 Sept 2026) — a case where Gagana explicitly asked Claude to recommend, a meaningfully different delegation pattern from #2, worth documenting as a contrast.
4. **Adversarial critique / red-team loop, memory-isolated** — the BRD v1 -> v2 revision (`03-BRD-Maintenance-Reporting.md`), 30 findings from a skeptical-reviewer persona run in a fresh context, every finding traced to a change.
5. **Substantive override candidate** — the ball/rod-mill repair-time citation, where a real, correctly-cited source's specific figures were checked against the source table directly and found to misrepresent it (`governance/Scope-Decisions-and-Limitations-Log.md`, 25 Aug 2026 verification pass). Strongest candidate for the Master Plan's required "at least one substantive override" entry.

Full write-ups to follow — this index exists so the repo shows the prompt library as a planned, tracked deliverable rather than a missing one.
