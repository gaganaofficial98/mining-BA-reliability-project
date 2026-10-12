# LinkedIn Article + Announcement Post

**Deliverable:** `video-and-linkedin/linkedin-article.md` per Master Plan §5.1/5.3
**Owner:** Gagana Suresh
**Status:** Draft v1 — 1 October 2026. **Draft only — not posted.** Posting needs Gagana's explicit go-ahead, and per `Reconciled-Finish-Schedule.md`, the GitHub repo and the recorded video this article links to don't exist yet — **do not publish until both of those links are real.**
**Word count (article body):** ~1,050 words, inside the Master Plan's 800–1,200 target.
**Built from:** the same real project documents as the video script — nothing in this draft is invented for the article. Two bracketed placeholders remain: `[REPO LINK]` and `[VIDEO LINK]`. Replace both before posting; don't post with a placeholder still in the text.

---

## Article

### When the maintenance team can't tell you which machine is actually costing you money

A mining maintenance function loses production hours to unplanned equipment breakdowns every month, and when leadership asks which asset class, which failure mode, or which shift is driving that loss, nobody has a clean answer. The data exists somewhere in the CMMS. It just isn't organized to answer that question, and the reporting that does exist is manual, inconsistent between planners, and can't support a real root-cause conversation.

That's the problem I built a full Business Analyst engagement around — simulated, not a real client, but run with the same rigor I'd bring to a real one: stakeholder interviews, a requirements document, process redesign, a reliability dashboard, and a business case with real dollar figures behind it. I used Claude throughout, not as a drafting shortcut but as a genuine working partner — and I tracked, task by task, exactly where it helped and where it didn't, because "AI made me faster" is a claim worth being able to defend, not just assert.

**A quick disclosure, up front:** the company in this project — Corvus Resources — is fictional. The underlying dataset is real: it's the AI4I 2020 predictive maintenance dataset, a genuine industrial sensor dataset, which I re-skinned onto a synthetic mining asset register. Every synthetic piece is flagged as such throughout the project. Nothing here claims to be a real client engagement.

**Discovery and requirements.** I ran simulated stakeholder interviews across six personas — a Reliability Engineer, a Maintenance Manager, a Financial Controller, an Operations Manager, and others — each grounded in a real mining org structure with genuinely conflicting priorities (Finance wants cost cuts, Operations wants uptime, and those two things pull against each other constantly). From those interviews came a Business Requirements Document, which I then put through an adversarial review: a fresh instance of Claude, with no memory of how I'd drafted it, playing a skeptical principal BA whose job was to find what would bounce back at sign-off, not to be encouraging. One finding from that pass is worth naming specifically, because it shaped the rest of the project: an early success criterion asked whether a sensor threshold predicted failure risk "clearly enough to justify a policy." The critique caught that this was unfalsifiable — any correlation could be argued as clear enough after the fact. The fix was to require a statistical bar, fixed before any analysis ran. That discipline mattered a month later, when I actually ran that analysis for real.

**Process redesign — a real trade-off, not a single assumed answer.** Mapping the current breakdown-to-repair workflow surfaced a structural problem: at the point where a failed asset gets either a quick patch or a proper root-cause fix, the quick patch wins almost every time, under production pressure, with no documented decision behind it. Rather than assume one fix, I had Claude lay out three options with honest trade-offs — reporting only, a formal escalation rule requiring joint sign-off on repeat failures, and a more ambitious pre-approved budget pool that would need a finance-policy change this discovery phase couldn't validate. I adopted the escalation rule and explicitly deferred the budget-pool option to a future phase rather than either over-promising or quietly dropping it. When I ran the full gap analysis afterward, the honest count was 6 of 11 identified pain points fully closed, 2 partially closed, 2 still genuinely open, and one permanently out of scope. Not eleven of eleven — a redesign claiming to fix everything would be exactly the kind of overclaiming this project is trying to avoid.

**The dashboard and the business case — the "so what."** The reliability dashboard's failure-mode ranking actually changed mid-project: an independent, memory-isolated review of my own SQL caught a tie-break bug that was silently under-counting one failure mode, and fixing it flipped which failure mode ranked second — a real, material correction, not a cosmetic one. The dashboard also surfaces a genuinely counter-intuitive finding: the equipment tier that fails most *often* is the opposite of the tier that matters most *per failure*, which argues for investing by consequence, not frequency. Tied to a real, cited cost-of-downtime benchmark — I used two independent published figures that disagree by roughly 4x, so I reported both as a range rather than collapsing them into one falsely precise number — the Mobile fleet alone accounts for somewhere between roughly $1.7 million and $6.5 million in estimated lost value over the analysis period. That range, not a tidy single number, is what a business case built on real external sources actually looks like.

**The efficiency data — with the caveats included, not the flattering parts only.** I logged every task as I finished it, not reconstructed from memory afterward, specifically so the numbers couldn't be shaped to look good in hindsight. The single strongest quality catch in the tracker: while building the cost-of-downtime business case, a formula error that would have understated the actual dollar loss by roughly 180 times was caught and fixed before I ever saw the output, through a multi-pass verification step. I'm not reporting one headline speed multiplier, because the honest shape of the data doesn't support one — drafting work compressed dramatically, verification and judgment calls much less so. And one task genuinely didn't get faster at all: rebuilding a Tableau dashboard from scratch after a platform issue destroyed the original file's data extracts took real manual rework no AI tool could route around. I included that on purpose. A project that only reports wins invites more skepticism than one that's honest about where the tool didn't help.

**What I'd do with more time or real data:** get formal sign-off from a real Reliability Engineer on two findings that currently rest on my own assessment as the analyst; find a defensible repair-time benchmark for fixed-plant equipment, which — after two genuine search passes — simply doesn't exist publicly, a real data gap I'm naming rather than papering over; and get real per-asset sensor data over time, since the current dataset can prove a warning threshold is real at a single moment but can't prove how much actual advance notice it would buy on a real machine.

Every prompting technique I used — role-prompting, chain-of-thought reasoning, critique loops, structured output — is documented in a prompt library alongside what I actually changed after reviewing Claude's output, including two moments where I overrode a judgment call it made. That field is the real answer to "did AI just do this for you?": the judgment calls were mine, and I can show you exactly where.

Full write-up, dashboard, prompt library, and efficiency data: **[REPO LINK]**. Full video walkthrough: **[VIDEO LINK]**.

---

## Announcement post (short — 3–4 sentences, no hashtag stuffing)

A mining maintenance function can't tell you which asset or failure mode is actually driving its downtime losses — so I built a full BA engagement to fix that: stakeholder interviews, a redesigned process, a reliability dashboard, and a business case, with Claude as a genuine analytical partner throughout. One finding worth sharing on its own: a formula error that would have understated a real dollar loss by roughly 180x got caught before it ever shipped. Full write-up, dashboard, and prompt library here: **[REPO LINK]** · video walkthrough: **[VIDEO LINK]**.

---

## Pre-posting checklist (do not skip)

- [ ] `[REPO LINK]` replaced with the real, live GitHub repo URL — not a placeholder, not a "coming soon" repo with an empty README.
- [ ] `[VIDEO LINK]` replaced with the real, published video URL.
- [ ] Gagana has given explicit go-ahead to post — this draft does not authorize posting on its own.
- [ ] Read the article aloud once before posting — the project's own credibility checklist (`00-Master-Plan.md` §6.1) flags clunky, repeated sentence structure as the tell that writing is unedited AI output; this draft should be edited into Gagana's own voice, not posted verbatim.
- [ ] Confirm the dollar range and dashboard-ranking claims above still match whatever is live in the repo at the time of posting — if either document changes again before publish, update this article to match, don't let it drift stale the way `09-Benefit-Realization-Report.md` briefly did earlier in this project.
