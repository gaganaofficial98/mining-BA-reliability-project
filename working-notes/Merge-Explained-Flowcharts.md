# How the AI4I ↔ Asset Register Merge Actually Works

**Short answer up front:** you don't need to merge these two files — `ai4i2020kestrel.csv` already *is* the merged result. `reskin_deal.py` did it already, in a previous session. What's below explains exactly how, and then how to get Claude to do this kind of task well if you ever need to do something similar again.

---

## Flowchart 1 — What `reskin_deal.py` actually did

```mermaid
flowchart TD
    A["Raw ai4i2020.csv\n10,000 rows: sensor readings +\na Type column (L / M / H)"]
    B["assetregister.csv\n48 pretend machines, each with\na Criticality Tier (L / M / H)"]

    C{"Split BOTH files\nby tier: L, M, H"}

    D1["All 'L' rows from AI4I\n(a big pile of readings)"]
    D2["All 'M' rows from AI4I"]
    D3["All 'H' rows from AI4I"]

    E1["The L-tier machines only\n(29 of them)"]
    E2["The M-tier machines only\n(14 of them)"]
    E3["The H-tier machines only\n(5 of them)"]

    F["Deal like cards:\neach machine gets a roughly\nequal share of that tier's rows,\nshuffled randomly (fixed seed)"]

    G["New column added: 'Asset ID'\n— which machine each row landed on"]

    H["Join the register's other columns\n(Asset Name, Make/Model, Location...)\nonto each row using that Asset ID"]

    I["Check: does every row's original\nType still match its assigned\nmachine's Criticality Tier?"]

    J["✅ 0 violations —\nsafe to save as the final file"]

    OUT["ai4i2020-kestrel.csv\n— the file you already have"]

    A --> C
    B --> C
    C --> D1 & D2 & D3
    C --> E1 & E2 & E3
    D1 & E1 --> F
    D2 & E2 --> F
    D3 & E3 --> F
    F --> G --> H --> I --> J --> OUT

    style A fill:#e9ecea,stroke:#8a9598
    style B fill:#e9ecea,stroke:#8a9598
    style OUT fill:#d4edda,stroke:#2e7d32
    style J fill:#d4edda,stroke:#2e7d32
```

**Plain-language walkthrough:** imagine you have 10,000 playing cards (the AI4I rows) and 48 buckets (your machines). You're not allowed to drop a card in just any bucket — a card marked "H" can only go in one of the 5 "H" buckets, never an "L" or "M" one. So the script splits both the cards and the buckets into three separate piles by tier first. Within each pile, it shuffles the matching cards and deals them out as evenly as possible across that pile's buckets — same idea as dealing a deck of cards around a table. Once every card has a bucket (an Asset ID), it goes back and stamps that machine's other details (name, make/model, site) onto the card. Then, before saving anything, it counts how many cards ended up in the wrong-tier bucket — the answer has to be zero, or something's broken. That zero-violations check is what makes this "auditable" instead of "trust me."

---

## Flowchart 2 — Is this a good way to show your AI skills, and how do you direct Claude to do it?

**Short answer: yes, this is one of the best examples in your whole project** — but only because of *how* it was asked for, not just that AI wrote some code. The difference is in the flowchart below.

```mermaid
flowchart TD
    A["Weak prompt:\n'merge these two files for me'"]
    A2["⚠ Claude has to guess the rules\n→ inconsistent, unauditable,\nnothing to point to as 'my judgement'"]

    B["Strong prompt: give Claude\na full spec, not just a task"]
    B1["1. Name the exact two inputs\nand their exact columns"]
    B2["2. State the business RULE explicitly\n('H can only match H, never L or M')"]
    B3["3. Require reproducibility\n('use a fixed random seed')"]
    B4["4. Require a built-in check\n('print how many rows broke the rule —\nshould be zero')"]

    C["Claude writes the script\nto that spec"]
    D["You run it yourself\n(or ask Claude to run it)"]
    E{"Check the printed\nverification output"}
    E1["0 violations →\nkeep the output file"]
    E2["Not 0 →\nsomething's wrong, fix before trusting it"]

    F["Log it in the Prompt Library:\nprompt used, why designed that way,\nwhat you changed after reviewing it"]
    G["Log it in the Efficiency Tracker:\nmanual-time estimate vs. actual,\nwhat quality check it gave you"]

    A --> A2
    B --> B1 --> B2 --> B3 --> B4 --> C
    C --> D --> E
    E -->|pass| E1 --> F
    E -->|fail| E2 -.-> B
    F --> G

    style A2 fill:#f3e3d2,stroke:#a15c1c
    style E1 fill:#d4edda,stroke:#2e7d32
    style E2 fill:#f8d7da,stroke:#b02a37
    style F fill:#cfe2ff,stroke:#0d47a1
    style G fill:#cfe2ff,stroke:#0d47a1
```

**Why this is genuinely a strong example, in plain terms:** anyone can type "merge these two files." What makes `reskin_deal.py` a good portfolio artifact is that the actual request behind it had four specific ingredients — a stated business rule (tier-matching), a demand for reproducibility (the fixed seed), and a demand for proof it worked (the violation count printed at the end). That's the difference between "I asked AI to do my homework" and "I specified an engineering problem and verified the AI's solution" — which is exactly the story this whole portfolio project is trying to tell.

**How to actually get Claude to do this, step by step, next time you need something similar:**

1. Tell Claude exactly what the two inputs are and paste (or describe) their real column names — don't say "my data," say "AI4I has columns X, Y, Z."
2. State the rule as a sentence a non-technical person could check by eye — "a High row can only go to a High asset" is testable; "match them sensibly" is not.
3. Ask for reproducibility explicitly — "use a fixed random seed so this can be re-run and get the same result." This is what makes the whole thing auditable rather than a one-off fluke.
4. Ask Claude to build in its own proof — "print a count of any rows that broke the rule, so I can confirm it's zero before trusting the output." This is the same "verification step" technique the Master Plan calls for on Day 9's cleaning work.
5. Once it runs cleanly, that's your Prompt Library entry: the prompt, why you asked for it that way, and — critically — anything you personally changed or caught afterward (like the stale comment-count fix from earlier, which is a small but real example of you catching something Claude didn't).

So to directly answer your question: yes, keep this one — it's a strong prompt-library entry exactly as it already exists. The next thing worth doing isn't re-merging anything, it's writing up *this exact exchange* (the four-ingredient spec, the verification check, your own catch of the comment bug) as a proper Prompt Library entry, since it's a clean, concrete example of directing AI with real engineering discipline rather than just asking it to "do the task."
