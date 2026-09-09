# Day 9 — Loading the Data & Writing the Core Queries, in Flowcharts

Two flowcharts here: first, exactly what rules the SQL query code has to follow (the "spec" from the last message, drawn out instead of written as one dense paragraph). Second, the actual step-by-step plan for today — who does what, in what order.

---

## Flowchart 1 — The rules the query code must follow (the "spec")

```mermaid
flowchart TD
    A["Look at one row of ai4i2020-kestrel.csv"]
    B{"Machine failure = 1?\n(the ONLY column we trust\nto answer 'did it break')"}

    C{"Any of the 5 cause flags\n(TWF/HDF/PWF/OSF/RNF) set?"}
    D["Count as a REAL failure.\nBucket cause = 'Unclassified'\n(9 rows like this)"]
    E{"More than one cause\nflag set at once?"}
    F["Count as a REAL failure.\nBucket by whichever ONE\ncause is most relevant\n(24 rows like this — count\nas ONE event, not two)"]
    G["Count as a REAL failure.\nBucket by that cause flag."]

    H{"RNF = 1 even though\nMachine failure = 0?"}
    I["NOT a failure.\nExclude from every count.\n(18 rows like this — expected\nbehaviour, not an error)"]
    J["NOT a failure.\nExclude — nothing to count."]

    K["Group every counted failure\nby Criticality Tier"]
    L{"Which tier?"}
    M["Mobile fleet (Medium)\n→ multiply failure count ×\n~2.2 hrs to get hours lost"]
    N["Fixed plant (High)\n→ report COUNT only.\nNo hours, no dollars — by design."]
    O["Ancillary (Low)\n→ report COUNT only.\nNo hours, no dollars — by design."]

    P{"SANITY CHECK before\ntrusting any of this:"}
    Q["Does the database have\nall 10,000 rows?"]
    R["Any blank cells where\na real reading should be?"]
    S["Does the total failure\ncount equal 339\n(the known real number)?"]
    T["❌ Any check fails →\nstop, fix the code, re-run"]
    U["✅ All checks pass →\ntrust the output, hand it over"]

    A --> B
    B -->|Yes| C
    C -->|No| D --> K
    C -->|Yes| E
    E -->|Yes| F --> K
    E -->|No| G --> K
    B -->|No| H
    H -->|Yes| I
    H -->|No| J

    K --> L
    L --> M
    L --> N
    L --> O

    M --> P
    N --> P
    O --> P
    P --> Q --> R --> S
    S -->|no match| T
    S -->|matches| U

    style D fill:#fff3cd,stroke:#a67c00
    style F fill:#fff3cd,stroke:#a67c00
    style I fill:#f8d7da,stroke:#b02a37
    style J fill:#f8d7da,stroke:#b02a37
    style N fill:#e9ecea,stroke:#8a9598
    style O fill:#e9ecea,stroke:#8a9598
    style T fill:#f8d7da,stroke:#b02a37
    style U fill:#d4edda,stroke:#2e7d32
```

**Plain-language walkthrough:** every one of the 10,000 rows goes through this same decision tree. First question, always: does `Machine failure` say 1? That column is the referee — nothing else gets a vote on whether a breakdown "really" happened. If yes, we still count it even when none of the five cause flags are set (9 rows), we still count it as just one event even when two flags fired together (24 rows), and we bucket it by cause. If `Machine failure` says 0, the row is not a breakdown, full stop — even the 18 rows where `RNF` is oddly set to 1 anyway. Once every row has been sorted into "real failure" or "not," the failures get grouped by which tier the asset belongs to, and only the Mobile fleet gets turned into an hours-lost number, because that's the only tier with a real, trustworthy repair-time figure behind it. Last step, before any of these numbers get used anywhere: three checks against facts we already know are true (10,000 rows, no missing data, exactly 339 real failures). If even one of those doesn't match, something in the code above broke a rule and needs fixing before the numbers can be trusted.

---

## Flowchart 2 — Today's actual plan (who does what, in order)

```mermaid
flowchart TD
    A["Data Dictionary is done\n(yesterday, 8 Sept)\nEvery field's meaning + source\nis now written down"]

    B["Claude writes the load script:\nCSV → mining_reliability.db,\nfollowing the spec in\nFlowchart 1 exactly"]
    C["Claude writes the core queries:\nfailure-mode Pareto,\nfailure rate by tier,\nMobile-fleet downtime hours"]
    D["Claude runs everything here first\n— nothing gets handed to you\nuntouched or unverified"]
    E{"Sanity check output:\n10,000 rows? no nulls?\n339 failures counted?"}
    F["Claude fixes the code\nand re-runs"]
    G["Claude shows you the real\noutput numbers in chat"]

    H["You get the actual files:\nmining_reliability.db\n+ the .sql query files"]
    I["You open them yourself in\nDB Browser for SQLite\n(free, install if you don't have it)"]
    J["You run the same queries\nand confirm your numbers\nmatch what Claude showed you"]
    K{"Anything look off,\nor would you write\na query differently?"}
    L["That's a real override —\nlog it as a prompt-library\nentry with your reasoning"]
    M["Log this whole task in\n06-Efficiency-Tracker.md:\nmanual-time estimate,\nactual time, quality signal"]

    N["Day 9 complete →\nfeeds Day 10: first-pass EDA\nusing these exact queries"]

    A --> B --> C --> D --> E
    E -->|fails| F --> D
    E -->|passes| G --> H --> I --> J --> K
    K -->|yes| L --> M
    K -->|no, matches| M
    M --> N

    style A fill:#d4edda,stroke:#2e7d32
    style F fill:#f8d7da,stroke:#b02a37
    style G fill:#cfe2ff,stroke:#0d47a1
    style L fill:#e5d9f5,stroke:#6a3fa0
    style N fill:#d4edda,stroke:#2e7d32
```

**Plain-language walkthrough:** you're not starting from a blank page today — yesterday's Data Dictionary is the actual spec this code gets built against, so nothing here is guesswork. Claude writes the load script and the three core queries, runs them in this sandbox first, and checks the sanity numbers before showing you anything — if the check fails, Claude fixes it silently and re-runs rather than handing you broken output to debug. Once it passes, you get the real files (not screenshots or pasted text) — the actual database and the actual `.sql` files — and you open and run them yourself in a free tool called DB Browser for SQLite. That's the step that makes this yours: if your numbers match, great, that's confirmation; if something looks off or you'd have written a query differently, that's exactly the kind of "I caught something and changed it" moment worth logging in the prompt library. Either way, this task gets one line in the Efficiency Tracker before we move to Day 10, which is the first day real business-question answers come out of this pipeline instead of a plan for getting there.

---

**Next message will be the actual load script and queries**, built to the Flowchart 1 spec, run here, with the sanity-check output shown to you directly.
