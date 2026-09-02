# Interview Transcript — Maintenance Manager

**Date conducted:** 2 September 2026
**Interviewer:** Gagana Suresh
**Technique:** Persona/role-prompting with fresh-context isolation, run in a separate chat outside this Project so the character had no visibility into internal scope-decisions or data-cleaning logic. Questions designed using a funnel structure (context → current-state pain → owned business questions, reframed away from the raw number → prioritization → tension point → closing) and a critical-incident style ("walk me through the last time...") rather than opinion-fishing.
**Status:** Simulated interview standing in for an unavailable real stakeholder — flagged per the project's data-integrity rule.

---

## Transcript

**1. Walk me through what a typical week looks like for you when it comes to dealing with equipment breakdowns — what actually crosses your desk, and how?**

So a breakdown happens — could be a haul truck engine derate, could be the crusher jamming, whatever — and the first I hear about it is usually a radio call or a text from the shift supervisor, or sometimes I just walk out and see a truck parked up at the workshop that shouldn't be there. That's it. There's no system pinging me. My planner might raise a work order in the CMMS after the fact, if he's not flat out, but half the time by the time it's logged properly I'm already three problems further down the road and I've forgotten the detail of the first one.

Rest of the week is me bouncing between the workshop and the pit trying to triage — what's down, what's my crew doing about it, do I need to pull a part from another unit to keep something running. I spend a stupid amount of time just chasing information, honestly. Ringing the parts store to see if we've even got the filter or the hose we need. Chasing operations to find out if they knew something was wrong before it failed, because half the time I reckon they did and just kept driving it. And then Friday arrives and someone wants a number for the ops meeting — how many hours did we lose this week — and I'm literally sitting there adding up work orders in a spreadsheet the night before, trying to make it add up to something believable.

**2. How do you currently find out a breakdown has happened, and how do you currently find out what it's costing you?**

How I find out, like I said, it's word of mouth first, CMMS second. As for what it's costing me... *(laughs, not really a happy laugh)* that's the one that gets me. I can tell you what parts and labour cost, roughly, because that's in the work order if my guys actually fill in the fields properly, which is a coin flip. But production hours lost? Nobody's given me a clean way to tie "truck 14 was down for six hours" to "that's this many tonnes we didn't move." I know it in my gut — I can feel when it's been a bad week — but I can't put a number in front of the GM that I'd bet my job on. And that's a problem, because when Finance or Ops question the maintenance budget, I've got nothing solid to push back with. I'm arguing with a feeling against their spreadsheet.

**3. Think of the last time you had to report a downtime or maintenance-cost figure up to the GM or head office — where did that number actually come from, and how confident were you in it?**

*(exhales)* Okay — last one was maybe six weeks back. Monthly ops review, GM wants "maintenance downtime hours" and "unplanned maintenance spend" on the one slide next to production tonnes.

Here's how that number actually got built, if I'm honest. I pulled the work order list out of the CMMS for the month, filtered to whatever I could find that looked unplanned — which is its own problem because half our guys don't tick the "breakdown" flag properly, some of them log a bearing failure as "preventive" because that's just the box that was open when they started typing. So I'm eyeballing descriptions, going "yeah that's a breakdown, that's a breakdown, that one's actually a PM that ran over," and building my own list by hand in Excel.

For the downtime hours, I'm cross-referencing that against whatever the shift supervisors wrote in the handover log, because the CMMS "downtime" field is filled in by whoever closed the work order, and that could be three days after the fact, and it's honestly sometimes just a guess. For the cost side I'm adding up parts issued against the work order plus labour hours times whatever rate, and that misses stuff like if we had to charter a part in, or if a contractor did the repair, because that invoice lands in Finance's system, not mine, and I don't always see it before the report's due.

So the number I put on that slide — was I confident in it? *(shakes head)* Not really, no. I'd say it was in the right ballpark, plus or minus twenty, twenty-five percent maybe, and I said as much verbally in the room, but it goes on a slide next to a hard production number and it looks just as solid as everything else up there. Nobody questioned it in the meeting, but I know what went into it, and if you asked me to defend that number line by line I'd start sweating. And that's the bit that actually worries me — not that I look bad in a meeting, but that someone makes a real call, like whether we replace a fleet unit or not, off a number I built at nine o'clock the night before out of a spreadsheet and a hunch.

**4. What's the most frustrating part of not having a clear, asset-by-asset view of where your downtime is actually coming from?**

Honestly? It's that I can't win an argument with data, so I end up winning it — or not winning it — on gut feel and volume. If I go to the GM and say "I reckon it's the 793s giving us the most grief," and Ops comes back with "no, it's your maintenance blokes taking too long on the mill," neither of us can actually settle that in the room. We just get louder. And usually whoever's louder, or whoever's got the GM's ear that week, wins.

What kills me is I actually think I know some of it in my gut — I'd bet the old excavator, the 320, and a couple of the older haul trucks are eating way more than their share of my hours. But "I reckon" isn't a business case. I can't ask for the budget to overhaul the 320 or bring one of the trucks in for a proper rebuild instead of another quick patch, because I've got no clean asset-by-asset number to point at. So what happens instead is everything gets treated the same — reactive, patch it up, get it back out there — because nobody can prove any one unit deserves special attention over another.

And then there's the failure type side of it, which is almost worse. Is it mechanical? Electrical? Is it actually an operator issue — someone lugging the engine or running something into the ground — dressed up as a component failure? I've got my suspicions there too, strong ones, but again, no clean way to slice it. So it just sits as noise, and every month it's the same fight, and every month I walk out of that meeting with a number I don't fully trust and an argument I can't quite finish.

**5. Right now, do you treat a haul truck and the crusher with roughly the same maintenance approach, or does something get more attention than something else — and on what basis do you make that call?**

Nah, they're not the same, but the reasoning's a bit — it's not as scientific as it probably should be, put it that way.

The fixed plant — crusher, mill, conveyors, thickener — that stuff gets more attention almost by default, because if the crusher goes down, the whole site stops. There's no truck behind it picking up the slack. So my planner's pretty religious about PMs on that gear, we've got a decent spares holding for the known wear parts, and if something starts sounding off on the mill I'll pull a guy off other work to go look at it same day.

Haul trucks and the excavators, it's more like a numbers game — we've got a fleet, so if one unit's down we've in theory still got production happening on the others, so it doesn't feel as urgent in the moment, even if three trucks being down at once is actually a bigger tonnage hit than the crusher for an afternoon. Nobody's ever actually done that comparison properly though. And within the mobile fleet, honestly, attention goes to whichever unit is shouting loudest that week — which operator complained, which one broke down most recently, which one my leading hand has a bee in his bonnet about.

What it's not based on is any actual ranking of "this asset costs us the most downtime hours or dollars over time, therefore it gets priority." I'd like it to be that. I just don't have the visibility to build that ranking with any confidence, so instead I'm making the call on instinct, whoever's yelling, and what nearly killed us last time.

**6. When something breaks down, how do you currently tell the difference between "we should have caught that coming" and "that one was always going to happen eventually"?**

Honestly? Mostly I don't. Not in any rigorous way. What happens in practice is after the fact, informally, in the shed, someone'll say "yeah, we knew that bearing was on its way out" or "the oil sample flagged that three weeks ago" — and then I get annoyed, because if we knew, why didn't it get actioned? We do have oil sampling and some vibration stuff on the bigger rotating gear — the mill mainly, a bit on the crusher — and that data does exist. But it lives with whoever runs that program, it's not sitting next to the breakdown history where I'd actually connect the two.

For the haul truck fleet it's worse, because there's less condition monitoring on them full stop — you're relying on operator pre-starts and whatever the onboard fault codes throw up, and operator pre-starts are patchy. So when a truck's engine lets go, is that "the derate warning's been flashing for two days and got ignored," or is that "catastrophic failure, nobody could've seen it"? I genuinely can't always tell you.

If you want my gut feel — because that's all I've got right now — I'd say a good chunk of what we call "random failures" probably weren't, if we'd been better at either catching the early signs or actually acting on them once flagged. But I can't prove that number, and until someone can show me it in black and white, it stays an argument rather than a fact.

**7. If you had earlier warning that a piece of equipment was heading toward failure, what would you actually be able to do differently today, with your current crew and budget?**

*(nods slowly)* Yeah, alright — that's a fair question, because I don't want to sit here and tell you a dashboard fixes everything, because it doesn't, not with what I've got.

Some stuff, genuinely, I could act on tomorrow with the crew I've already got. If I knew three days out that a truck's about to have a transmission issue instead of finding out when it dies in the pit, I can plan that — pull it in on a shift where I'm not already flat out, have the part pre-ordered instead of chasing it same-day, do it as a controlled job instead of a guys-standing-around-waiting-for-freight job. That alone would save me real hours, because so much of what blows out a repair right now isn't the actual spanner time, it's the waiting.

Which is the bit that gets messy, honestly. Even if I know something's coming, I still need Operations to give me the truck. And they're chasing tonnes, so their instinct is always "can it do one more shift," and mine is "no, pull it now before it strands itself in the pit and costs us worse." So part of what I'd want out of any of this reporting is something that helps make that case to them too, not just something for my own team.

Where it gets harder is if the answer is "you need to condition-monitor more gear" or "you need dedicated planning resource to action all these warnings properly." Because right now my planner's one bloke, flat chat just keeping the CMMS ticking over, and I don't have spare tradies sitting around waiting for a heads-up job. So more warning without more planning capacity just means I've got more things I know about and still can't get to in time. So — yes to earlier warning, genuinely. Just don't want you walking away thinking a bit of data alone solves the crew and access problems underneath it, because it won't.

**8. If this project could only hand you one thing — a solid cost number, a ranked list of your worst offenders, or an early-warning flag — which would actually change what you do day to day, and why?**

*(thinks about it properly, doesn't rush the answer)* Okay — if I can only pick one, I'd take the ranked list of worst offenders. Not the early warning, not even the cost number on its own.

The cost number's nice to have, but it's a scorecard — it tells me how bad things are, it doesn't tell me where to spend my next hour. A ranked list — this asset, this failure type, costing us this much downtime, month after month — that's something I can act on Monday morning. I can say "right, the 320 and truck 14 account for a third of our unplanned hours, everyone's attention goes there until that changes," instead of spreading my crew thin reacting to whatever broke most recently.

Early warning I'd love, genuinely, but without knowing where my worst assets already are, an early warning flag just tells me about more problems, sooner, and I still don't necessarily know which of those warnings matter most if I've got three going off in one week and only enough hands for one. The ranked list tells me priority. Warning without priority is just more noise, earlier.

And look — part of why I want that list is it's also my ammunition. Right now when Operations pushes back and says "just get it running, we need the tonnes," I've got nothing to counter that with except "trust me." A list that says this specific unit has cost us this many hours over the last six months lets me actually argue "no, we pull this one now and fix it properly." That's the fight I have with Ops every second week — them wanting it back out there today, me wanting to actually fix the root cause instead of another quick bodge that fails again in a fortnight. Right now that argument is just two people with opinions. A ranked list, with real numbers behind it, at least means I'm not walking into that conversation empty-handed.

**9. When Operations is pushing hard to get an asset back online, how do you decide between a fast fix and the fuller root-cause job your reliability engineer would rather do? Who usually wins that call, and what does it end up costing you later?**

*(lets out a breath, this is clearly a sore spot)* Yeah. This one I could talk about for the full forty minutes if you let me.

Honestly, most of the time, Operations wins. Not officially — but in the moment, when the pit's screaming for tonnes and the shift supervisor's on the radio asking when truck 14's coming back, the pressure's real and it's immediate, and it lands on me, not on my reliability engineer. He'll come to me and say "look, this is the third time this alternator mount's cracked, we should pull it apart properly, check the alignment" — and he's probably right, he usually is. But that's a two-day job done properly versus a four-hour job to get it rolling again. And when I've got the mine manager or the ops superintendent standing at my shoulder, "two days" is a very hard number to say out loud, even when I know it's the right call.

So what happens, more often than I'd like to admit, is I make the call to patch it, get it back out there, and quietly tell myself we'll schedule the proper job "next time it's in for a service" — which mostly doesn't happen, because next time it's in for a service we're flat out doing the actual service. And then, sure enough, six weeks later, same mount, same failure, except now it's failed at a worse moment, and I've spent more total hours and dollars across two rushed jobs than I would have on one proper one.

What it costs me — beyond the obvious repeat downtime — is credibility, both ways. Ops starts thinking maintenance is slow and precious when we do push back, because they've seen us cave before. And my own reliability bloke starts feeling like there's no point raising the root-cause option because it never gets approved anyway, which is worse, because then I'm not even getting the recommendation to override.

If I'm honest with myself, who "should" win that call depends on the asset and the pattern, not on who's yelling louder that day — and right now I've got no clean way to show, in the moment, "this is repeat number three, the fast fix has already cost us more than the full job would have." If I had that in front of me when Ops is pushing, that changes the conversation completely, because then it's not maintenance being difficult, it's a number.

**10. What would make this whole reporting initiative a waste of your time — what does it absolutely have to get right before you'd actually use it?**

*(leans forward a bit)* Alright, I'll give you the honest list, because I've seen this kind of thing fail before at a previous site and I don't want to sit through that again.

Number one — it has to be built off data that's actually trustworthy, or it's worse than useless, because then I've got a shiny report telling me confidently wrong things, and I'll make a bad call and point at the dashboard when it goes sideways. If it's just pulling straight out of the CMMS the way it's filled in today — half-ticked flags, downtime hours that are someone's guess — then you've just automated my spreadsheet problem, you haven't fixed it.

Second — it can't create more work for my crew than it saves me. If the answer to fixing the data is "get your tradies to fill in eight more fields on every work order," that's dead on arrival.

Third — I need it to actually tie downtime to something I can defend. Not just "unit X was down for Y hours," but something that survives Finance or the GM poking at it — hours, dollars, tonnes lost, ideally all lining up.

And fourth, and maybe the one that worries me most — it needs Ops to actually look at it too, not just live on my laptop. If this becomes "maintenance's report" that everyone nods at in the meeting and then changes nothing about how fast they release a truck to me, I've spent all this effort building ammunition nobody else picks up. So if you want my honest bar for success — it's not "does it look good." It's: six months from now, am I actually making different calls because of it, and is Ops actually having a different conversation with me because of it.

**11. Is there anything about how downtime or maintenance decisions get made here that I haven't asked about but should have?**

*(sits back, actually pauses to think)* Yeah, actually — there's one thing that hasn't come up, and it's probably the one I'd bring up myself if you hadn't asked.

Nobody's asked me about who actually decides how a breakdown gets classified — whose fault it was, essentially, even if nobody says it that bluntly. Right now, if a truck comes in with a busted final drive, my guys write up what they find mechanically, but there's no real process for saying "this failed because of normal wear" versus "this failed because someone was riding the brakes down every ramp for a month" or "this got overloaded past spec." That's a conversation that basically doesn't happen formally — it happens as grumbling in the workshop — because nobody wants to be the one who officially blames an operator on a piece of paper. So it just gets logged as a component failure, full stop, and rolled into my numbers as if it's a reliability issue, when some chunk of it — I genuinely don't know how much, could be five percent, could be twenty — is actually a training or supervision issue that sits over in Operations' court, not mine.

That matters for what you're building, because if your reporting lumps all of that in as "unplanned maintenance," I look worse than I am, and the actual fix for a chunk of my downtime isn't more spanners or better parts stocking, it's someone in Ops having a word about how their guys are driving. That's a conversation I've tried to raise before and it hasn't gone anywhere, because there's no data to back it up. So if there's any way this initiative can separate out "this looks like it might be operator-influenced" from "this is a genuine wear-and-tear or design issue," even roughly, that'd be worth having — not to go pointing fingers publicly, but because right now that whole category of downtime is invisible, and I carry the blame for all of it by default.

---

## Key findings extracted (BA synthesis)

**1. New, unscripted finding — operator-attributed vs. genuine equipment failure is currently invisible, and it wasn't planted in the persona brief.** He raised this unprompted at the closing catch-all question. This is a real requirement candidate: a lightweight "suspected contributing factor" field distinct from failure mode, so operator-influenced damage isn't silently absorbed into maintenance's reliability numbers. Handle carefully in the BRD — frame as a contributing-factor category, not a blame/disciplinary field, since he was explicit he doesn't want it used to point fingers publicly.

**2. Four concrete success criteria for the entire initiative**, stated in his own words at Q10: (a) underlying data must be trustworthy, not just automated from today's inconsistent CMMS entries; (b) must not add data-entry burden on tradies; (c) must tie downtime to defensible hours/dollars/tonnes that survive scrutiny; (d) must be visibly used by Operations too, not just live in Maintenance's own report. These map almost directly onto UAT/acceptance-criteria language for `08-Test-Cases.md` later.

**3. Prioritization signal for the dashboard:** given a forced choice between a cost number, a ranked asset/failure-mode list, and an early-warning flag, he picked the ranked list — explicitly because it's actionable ("tells me where to point my next hour") and because it doubles as leverage in the Operations negotiation. Strong argument for making the Pareto/ranked view the dashboard's primary element rather than a KPI tile.

**4. A quantifiable "cost of the quick fix" pattern** — the alternator-mount example (patch now, same failure recurs ~6 weeks later at a worse moment, total cost across two rushed jobs exceeds one proper job). This is a concrete, named recurring-failure narrative worth carrying into the business case as an illustrative example of why root-cause investment pays off, alongside the aggregate Pareto numbers.

**5. Confirms and sharpens the register's existing Q4/Q6 framing** ("preventable vs. random," "precursor patterns") — he independently estimates 5–20% of "random" failures likely had a missed warning sign, and separately confirms condition monitoring exists on fixed plant (oil sampling, vibration) but isn't integrated with breakdown history, and is largely absent on the mobile fleet. Corroborates why the Instrumentation & Controls Engineer's short interview matters.

**6. Confirms the sponsor/tension model already logged:** Operations wins the fast-fix-vs-root-cause call "most of the time," described entirely from his side — a clean, usable data point for the BRD's stakeholder-conflict section, and a natural setup for whatever the Reliability Engineer's interview says on the same question.

**7. Data-visibility gap worth logging as a limitation, not a requirement:** he doesn't see contractor/parts-charter costs before his reporting deadline because those invoices land in Finance's system. Cross-functional data-visibility gap between Maintenance and Finance, separate from the CMMS itself — worth a line in the BRD's constraints section.
