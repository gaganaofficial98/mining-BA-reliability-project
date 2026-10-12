# Video Walkthrough Script

**Deliverable:** `video-and-linkedin/video-script.md` per Master Plan §5.1/5.2
**Owner:** Gagana Suresh
**Status:** Draft v1 — 1 October 2026. Script only — **not recorded**. Recording needs Gagana's own voice and screen presence and cannot be produced inside a text-only session; see `Reconciled-Finish-Schedule.md`.
**Target runtime:** 6–8 minutes, per Master Plan §5.2's outline (reproduced segment-by-segment below so the structure stays checkable against the source instruction).
**Built from:** real content already in this project — the BRD, Stakeholder Register, Process Maps, Dashboard, Benefit Realization Report, EDA Findings, and Efficiency Tracker. Every number and quote below traces to one of those documents; none are invented for the video. Timing is a floor plan, not a stopwatch contract — natural delivery will run long or short in places, and that's fine.

**How to use this script:** it's written as speaking points and on-screen direction, not a word-for-word read — say it in your own voice. Bracketed `[SCREEN: ...]` notes mark what should be on screen at that moment; bracketed `[SAY IN YOUR OWN WORDS: ...]` notes mark places where the script gives you the substance but you should not read it verbatim, because it needs to sound like you talking, not narration.

**Module A status note (read before recording):** per Gagana's own instruction, Module A (the classical ML proof-of-concept) is being built the day after this script was written, not before. Section 6 below is written to describe it honestly as **in progress / coming**, not as a finished deliverable — if Module A is complete by the time this is actually recorded, update that one paragraph to past tense and add its real precision/recall result; don't record this script unchanged if that's happened.

**GitHub repo status note (read before recording):** the repo this video will point viewers to does not exist yet as of this script's writing (see `Reconciled-Finish-Schedule.md`'s "Deferred" section). Do not record this video, and do not publish it, until the repo is live and populated — a video that says "link in the description" to a repo that doesn't exist is the one claim in this whole project that would actually be false, not just incomplete.

---

## Opening disclosure (say this, or something very close to it, before the hook — not optional)

*"Quick disclosure before I start: this is a simulated engagement. The company — Corvus Resources — is fictional, I built it for this project. The core dataset is real — it's the AI4I 2020 predictive maintenance dataset, a genuine industrial dataset — but I've re-skinned it onto a synthetic mining asset register, and I'll flag every synthetic piece as I go. Nothing here claims to be real client work."*

This isn't a throat-clearing formality — it's the direct answer to the first question a skeptical recruiter has, asked before they have to ask it. Keep it under 15 seconds and move straight into the hook.

---

## Segment 1 — Hook (0:00–0:45)

**Master Plan instruction:** *"Hook: the problem statement and why it matters, stated in plain business language, not BA jargon."*

[SCREEN: a simple title card or the dashboard's top-line number, not yet the full dashboard]

[SAY IN YOUR OWN WORDS, hitting these beats:]
- A mining maintenance function is losing production hours to equipment breakdowns it can't explain.
- Nobody can answer, in one report: which asset, which failure mode, which shift is driving the loss.
- That's not a data problem on the surface — it's a reporting and process problem, and that's exactly the kind of problem a Business Analyst gets brought in to fix.
- You ran this as if it were a real BA engagement: stakeholder interviews, requirements, a redesigned process, a dashboard, and a business case — with Claude as a genuine working partner throughout, not just a polish tool.

**Concrete anchor to land the hook (real number, use it):** the dashboard's own Mobile-fleet estimate — **roughly 183 hours lost to unplanned breakdowns** over the analysis period, just on one of three asset tiers — is a good first number to say out loud here, before you've even opened the dashboard. It gives the hook a real stake instead of a vague problem statement.

---

## Segment 2 — BRD & Stakeholder Register: a critique pass catching a real gap (0:45–2:00)

**Master Plan instruction:** *"Walk through the BRD and stakeholder register — show the red-team/critique pass catching a real gap, on screen."*

[SCREEN: `01-Project-Charter.md`, Appendix D — scroll to Finding 5]

[SAY IN YOUR OWN WORDS:]
- Before the BRD, the project charter itself went through a red-team pass: you role-prompted Claude as a skeptical principal BA reviewing a junior's charter before client sign-off, and told it explicitly not to soften the feedback.
- One finding is worth showing on screen directly, because of what it led to later. An early draft of Objective 5 asked whether a torque/tool-wear threshold predicted overstrain risk **"clearly enough to justify a policy."** The critique caught that this was unfalsifiable as written — quote it: *"any correlation could be argued as 'clear enough' after the fact."*
- The fix: rewrite the success criterion so the statistical bar — the actual pass/fail threshold — has to be fixed **before** the analysis runs, not chosen afterward to fit whatever the data says.
- [PAYOFF — flag that this comes back later]: *"Hold that thought, because that one fix is the reason I was able to honestly report, a month later, that one of my five failure modes actually failed its own bar rather than being stretched to pass it. I'll show you that in a minute."*
- Same discipline on the Stakeholder Register: rather than one generic "who are the stakeholders" prompt, you ran two independent passes — one reasoning through the physical work-order lifecycle step by step, one asking "whose decision changes once each business question is answered" — and compared them, rather than trusting either alone.

Keep this to about 75 seconds — one finding shown in detail, the stakeholder-register technique mentioned in one sentence, don't try to show more than that on screen.

---

## Segment 3 — Process Map: a real trade-off decision, not a single assumed answer (2:00–3:30)

**Master Plan instruction:** *"Process map: as-is vs to-be, the trade-off decision you made and why."*

[SCREEN: `04-Process-Maps.md` Section 8 — the three-option trade-off table, then the To-Be Mermaid diagram with Step 4 highlighted]

[SAY IN YOUR OWN WORDS:]
- Walk the as-is map briefly: eleven steps from breakdown to closeout, and one structural problem sits right in the middle of it — Step 4, where a failure either gets a quick patch or a proper root-cause fix. Today that call is made informally, under production pressure, and the quick patch almost always wins.
- You didn't just pick a fix. You asked Claude to lay out three real options with honest trade-offs: **Option A**, reporting only — give the decision-maker better information and hope the decision changes; **Option B**, a formal escalation rule — once the same failure recurs on the same asset, a further patch needs documented joint sign-off from Maintenance and Reliability; **Option C**, the most ambitious — a pre-approved budget pool that lets a proper fix bypass the capital-approval queue entirely.
- The decision: **Option B, adopted.** Option C wasn't rejected — it's explicitly carried forward as a future-phase recommendation, because it needs a Finance/capital-planning stakeholder this discovery phase never reached.
- [SAY IN YOUR OWN WORDS, the honest-scorecard beat — this is the credibility moment of this segment]: *"And when I did the full gap analysis afterward, the honest count was 6 of 11 pain points fully closed, 2 partially closed, 2 genuinely still open, and one permanently out of scope. Not eleven out of eleven — a redesign that claimed to fix everything would be exactly the kind of overclaiming this project is trying not to do."*

---

## Segment 4 — Live dashboard walkthrough: the "so what" (3:30–5:30)

**Master Plan instruction:** *"Live dashboard walkthrough — the 'so what,' tied straight to the business case number."*

[SCREEN: the live Tableau Public dashboard — https://public.tableau.com/app/profile/gagana.suresh.vatal/viz/MiningFleetReliabilityDashboard_/MiningFleetReliabilityDashboard]

[SAY IN YOUR OWN WORDS, in this order:]
1. **Failure Mode Pareto first.** Heat Dissipation Failure is the clear #1 cause of breakdowns, at roughly 34%. For #2, point at OSF (Overstrain) — and tell the real story behind it: *"This ranking actually flipped. An early version of this chart had Power Failure in second place. A fresh, independent review of my own SQL — someone else checking my work, basically, except it was a memory-isolated Claude instance with no context from how I'd built the query — caught a tie-break bug that was silently under-counting Overstrain. Once fixed, Overstrain overtakes Power Failure for second place. That's not a cosmetic difference — it changes which failure mode you'd tell a maintenance team to prioritize."*
2. **Failure Rate by Tier.** Point out the counter-intuitive finding: the tier that fails *most often* — low-criticality ancillary equipment, at roughly 3.9% — is the opposite of the tier that matters *most* per failure — high-criticality fixed plant, at roughly 2.1%. The naive recommendation (chase the highest failure rate) would misallocate investment. The real recommendation is differentiated investment by *consequence*, not frequency.
3. **Tie it to the business case number — the actual "so what."** *"For the Mobile fleet alone, 83 real recorded failures at a cited industry-average repair time works out to about 183 hours of lost production. Multiply that by a real, cited cost-of-downtime range — I used two independent published benchmarks that disagree by about 4x, so I reported both rather than picking one to look precise — and that's somewhere between roughly $1.7 million and $6.5 million, on one asset tier, for one historical period. That range, not a single too-clean number, is what a business case built on real external benchmarks actually looks like."*
4. **Close the loop from Segment 2.** *"And remember that pre-registered statistical bar from the charter red-team? I ran it for real. The torque/tool-wear overstrain threshold hit it exactly — 100% precision, 100% recall, a clean go-ahead for a proactive replacement policy. But tool-wear failure didn't clear the same bar — it caught 93.5% of real tool-wear failures but only 5.4% of its own alarms were right. I reported that as a partial result, not a win, because the bar was fixed before I ran the test — that's the whole point of fixing it in advance."*

This is the longest segment (2 minutes) — it's carrying the entire "so what" of the project, so don't rush it, but don't try to show every dashboard worksheet either. Three charts, one business-case number, one callback. That's enough.

---

## Segment 5 — The efficiency story (5:30–6:30)

**Master Plan instruction:** *"The efficiency story — show the tracker, state the honest numbers, name one specific quality catch."*

[SCREEN: `Efficiency-Tracker.md`]

[SAY IN YOUR OWN WORDS:]
- *"I logged this as I went, task by task, rather than estimating backward at the end — because backward estimates get shaped to look good, and I wanted numbers that would survive someone asking me to defend them."*
- **Name one specific quality catch, concretely — don't generalize.** The strongest one in the tracker: *"Building the cost-of-downtime business case, Claude's own formula caught its own bug before I ever saw it — a cell was referencing the hourly rate without multiplying by the hours, which would have shipped roughly $9,400 instead of the correct $1.72 million. That's not a rounding error, that's off by about 180 times. A multi-pass verification step caught it before delivery, not after."*
- **State one honest number, not a single flattering multiplier.** Avoid saying "10x faster" — say something like: *"Across the tasks I've logged so far, the time savings vary a lot by task type — drafting work compressed dramatically, verification and judgment calls didn't compress nearly as much, and that's the honest shape of it, not a single number."*
- **Name the one place AI genuinely didn't help — this is required, not optional, for credibility.** *"Not every task sped up. Rebuilding the Tableau dashboard from scratch, after the original file's data extracts were lost to a platform issue, took real manual rework in the desktop app — that bottleneck was Tableau Public's own extract-handling limitation, not something AI could route around. I'm including that here on purpose, because a project that only reports wins invites more skepticism than one that's honest about where the tool didn't help."*

---

## Segment 6 — Close (6:30–7:30)

**Master Plan instruction:** *"Close: what you'd do with more time/real data, and the prompt library as evidence of process. If you built either or both optional stretch modules, one sentence per module here is enough — do not give either more runtime than the core dashboard/business case walkthrough."*

[SCREEN: `Prompt-Library.md` index / entry list, then briefly `12-ML-Proof-of-Concept.md` and `13-LLM-Cause-Code-Classifier.md` file names in the repo tree]

[SAY IN YOUR OWN WORDS:]
- **What you'd do with more time or real data (pick 2, don't list all of these — say them naturally):** get real stakeholder sign-off on the two findings that are currently just the Business Analyst's own assessment, not a validated one; source a defensible repair-time benchmark for fixed-plant equipment, which — after two full search passes — simply doesn't exist publicly, a genuine data gap worth naming rather than papering over; and get real longitudinal, per-asset sensor data, because the current dataset can prove a sensor threshold is real at a single moment but can't prove how much advance warning time it would actually buy on a real asset over time.
- **Prompt library, one sentence:** *"Every notable prompt I used — role-prompting, chain-of-thought, critique loops, structured output — is documented in a prompt library with what I actually changed after reviewing the output, including two moments where I overrode a judgment call Claude made, because 'did AI just do this for you' is the question I wanted to answer before anyone asked it."*
- **Module A, one sentence (update if built by recording time — see the status note at the top of this document):** *"I'm also building a small, honestly-scoped classical ML proof-of-concept on top of this same dataset — a single model, a proper train/test split, reported with its real precision and recall including where it underperforms — as a footnote demonstrating range, not a second core deliverable."*
- **Module B, one sentence:** *"And separately, I built a small LLM-based classifier for messy, free-text maintenance cause codes — evaluated blind, by a Claude instance with zero access to my ground-truth answers — which scored 98% overall but genuinely disagreed with me on one entry, and I show that disagreement in the write-up rather than hiding it."*
- **Final line:** *"Everything here — the documents, the dashboard, the prompt library, the efficiency data — is in the repo linked below, with every synthetic piece flagged, and every number traced to either the dataset, a cited source, or a disclosed assumption. Thanks for watching."*

---

## Production notes (not part of the spoken script)

- **Total spoken time check:** six segments at roughly 45s / 75s / 90s / 120s / 60s / 60s plus the opening disclosure (~15s) comes to about 7.5 minutes before any natural pauses or re-takes — comfortably inside the 6–8 minute target. If a take runs long, Segment 3 (process map) and Segment 6 (close) are the two safest places to trim, since Segment 4 is carrying the project's core "so what" and shouldn't be cut.
- **Screen recording order:** record the dashboard walkthrough (Segment 4) as a separate clean screen-capture pass before recording yourself talking over it — Tableau Public's own UI chrome (loading states, tooltips) is easier to edit around after the fact than live.
- **Do not record until:** (a) the GitHub repo is live and populated — see the status note at the top of this document — and (b) Module A's status in Segment 6 reflects reality at the time of recording, not the state as of 1 October 2026.
- **Consistent with this project's own disclosure discipline:** if anything in this script turns out to be stated imprecisely once the actual dashboard/repo are in front of a camera, correct it in the next draft of this file rather than ad-libbing a correction live and hoping it lands — the same error-disclosure convention used everywhere else in this project applies here too.
