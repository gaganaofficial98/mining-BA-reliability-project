# Today's Task Flow — Week 2, Day 8: Data Dictionary

**In one sentence:** today we write down every field we're going to use — where it comes from, what it means — before touching any actual data. This is the "define your ingredients before you cook" step.

**Why this has to happen before Day 9:** Day 9 is where you actually clean and re-skin the AI4I dataset and load it into a database. You can't write a script to "clean the fields" until every field has a name, a meaning, and a source written down somewhere. This document is that somewhere.

---

## The flow for today

```mermaid
flowchart TD
    S["Start: two separate\nsources of fields"]

    A1["AI4I's real columns\n(Type, Torque, Tool wear,\nAir/Process temp, 5 failure flags)"]
    A2["Your synthetic asset register\n(Asset ID, Site, Criticality tier)"]

    M["Merge into ONE field list\nside by side"]

    T1{"For each field —\nwhere did it come from?"}
    D1["Tag: DATASET\n(comes straight from AI4I)"]
    D2["Tag: CITED SOURCE\n(e.g. the repair-time benchmark)"]
    D3["Tag: LABELED ASSUMPTION\n(you made a defensible call)"]

    F["Flag any field that still\nneeds to be invented —\nand say exactly why"]

    OUT["Output: 05-Data-Dictionary.md\none row per field, fully sourced"]

    NEXT["Feeds Day 9:\nclean + re-skin AI4I,\nload into SQLite,\nwrite the core SQL queries"]

    S --> A1
    S --> A2
    A1 --> M
    A2 --> M
    M --> T1
    T1 -->|dataset| D1
    T1 -->|real citation| D2
    T1 -->|your judgement call| D3
    D1 --> F
    D2 --> F
    D3 --> F
    F --> OUT
    OUT --> NEXT

    style S fill:#e9ecea,stroke:#8a9598
    style OUT fill:#d4edda,stroke:#2e7d32
    style NEXT fill:#fff3cd,stroke:#b8860b
    style F fill:#f3e3d2,stroke:#a15c1c
```

---

## What each box actually means, in plain terms

**Two separate sources of fields.** You're not building this from scratch — you're combining two things that already exist: AI4I's real sensor columns (the actual data file) and the asset register you invented in Week 1 (Asset ID, Site, Criticality tier). Neither one alone is enough; the dictionary is where they meet.

**Merge into one field list.** Literally one table, one row per field, whether it came from AI4I or from your own asset register. This is what makes the eventual cleaning script possible — the script just reads down this list and knows exactly what to do with each column.

**For each field — where did it come from?** This is the same three-way honesty rule you've used everywhere else in this project. A field is either straight from the dataset (e.g. Torque — it's just there in AI4I), backed by a real external citation (e.g. repair time, sourced from the mining-reliability papers), or a labeled assumption you made yourself (e.g. which specific machine an AI4I row got assigned to). Nothing gets to just sit there unlabeled.

**Flag anything that still needs inventing.** A few fields won't exist anywhere yet — for example, if the cause-code taxonomy redesign (FR-14) ever gets built, its new simplified code list would need to be invented here, with a note explaining why the old 40-option list wasn't kept. Better to name these gaps now than discover them mid-script on Day 9.

**Output: 05-Data-Dictionary.md.** The actual deliverable — one table, every field, every source tagged, nothing hidden.

**Feeds Day 9.** Once this exists, the Day 9 cleaning script has a spec to follow instead of guesswork — that's the entire point of doing this step first.

---

*Ready when you are — say the word and I'll start building the actual field list.*
