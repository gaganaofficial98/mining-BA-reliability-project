"""
load_to_sqlite.py
==================
Day 9, Mining Reliability Reporting project.

WHAT THIS DOES
--------------
Loads the already-merged ai4i2020-kestrel.csv (10,000 rows, 20 columns) into a
real SQLite database, then builds the core analytical views the Week 2/3
dashboard and business case will query against.

THE SPEC THIS SCRIPT FOLLOWS (see Todays-Task-Flow-Day9.md, Flowchart 1,
and 05-Data-Dictionary.md Sections 2-3 for the full reasoning):

1. SOURCE-OF-TRUTH RULE (Scope-Decisions-and-Limitations-Log, 24 Aug 2026):
   `Machine failure` is the ONLY column that decides whether a row is a real
   breakdown. The five mode flags (TWF/HDF/PWF/OSF/RNF) only categorize a
   failure Machine failure has already confirmed - they never detect one.

2. THREE DATA-QUALITY EXCLUSIONS (same log entry, 24 Aug 2026):
   a) 9 rows: Machine failure=1, no mode flag set -> still counted, bucketed
      as 'Unclassified'.
   b) 18 rows: RNF=1 but Machine failure=0 -> NOT counted as a failure at all
      (expected behaviour per RNF's documented independent ~0.1% design).
   c) 24 rows: more than one mode flag set on the same row -> counted as ONE
      failure event (by row), never by summing flag columns (which would
      double-count these 24 rows).

3. TIER-BASED REPAIR-TIME LOGIC (05-Data-Dictionary.md Section 3.1-3.2):
   Repair-time hours only get applied to the Mobile fleet (Medium tier,
   ~2.2 hrs/event). Fixed plant (High) and Ancillary (Low) report failure
   COUNT only, by design (Option B, 1 Sept 2026; Ancillary decision,
   8 Sept 2026) - no fabricated hours figure for either.
   This benchmark lives in its OWN small lookup table (tier_repair_benchmark),
   never stamped onto the raw dataset rows - keeps "real data" and
   "external assumption" visibly separate, per the project's standing rule.

4. BUILT-IN SANITY CHECK (verification step, same pattern as reskin_deal.py):
   Before anything is treated as trustworthy, this script checks and prints:
   - row count == 10,000
   - zero nulls in every column
   - zero Criticality Tier / Type mismatches (tier-matching rule still holds)
   - total counted failures == 339 (the known real Machine failure=1 count)
   If any check fails, the script prints which one and stops - it does not
   silently produce a database with unverified numbers.
"""

import sqlite3
import pandas as pd
import sys

CSV_PATH = "/root/.claude/uploads/302e4f88-9ea3-5715-aef6-8cf2002005e4/21c1f933-ai4i2020kestrel.csv"
DB_PATH = "/home/claude/work/mining_reliability.db"

MODE_FLAGS = ["TWF", "HDF", "PWF", "OSF", "RNF"]

# --- external benchmark, cited: see 05-Data-Dictionary.md Section 3.1 ---
# Mobile fleet only. Fixed plant and Ancillary deliberately have no figure.
TIER_REPAIR_BENCHMARK = [
    ("M", "Mobile fleet", 2.2, "Rezaei Dashtaki et al. 2025 (Scientific Reports) + "
                                "Jakkula et al. 2025 (J. Eng. Mgmt & Sys. Eng.) - "
                                "real mine-site repair data, tiers converge near this midpoint"),
    ("H", "Fixed plant", None, "No defensible source found - Option B, resolved 1 Sept 2026. "
                                "Report by failure frequency only."),
    ("L", "Ancillary", None, "INL proxy source covers only 4 of 29 assets - resolved 8 Sept 2026. "
                              "Report by failure frequency only, same rule as Fixed plant."),
]


def main():
    print("=" * 70)
    print("STEP 1 — Reading source CSV")
    print("=" * 70)
    df = pd.read_csv(CSV_PATH)
    print(f"Read {len(df):,} rows, {len(df.columns)} columns from:\n  {CSV_PATH}\n")

    # ------------------------------------------------------------------
    # STEP 2 — write the raw data into SQLite, untouched (this is the
    # single source table every query below reads from)
    # ------------------------------------------------------------------
    print("=" * 70)
    print("STEP 2 — Writing raw data into SQLite (table: readings)")
    print("=" * 70)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("readings", conn, if_exists="replace", index=False)
    print(f"Wrote {len(df):,} rows into 'readings' table at:\n  {DB_PATH}\n")

    # ------------------------------------------------------------------
    # STEP 3 — apply the source-of-truth + exclusion rules to derive
    # a clean 'failure_events' table (only rows that count as real
    # breakdowns under the rule above, plus their cause bucket)
    # ------------------------------------------------------------------
    print("=" * 70)
    print("STEP 3 — Applying source-of-truth rule + 3 data-quality exclusions")
    print("=" * 70)

    def classify_cause(row):
        flags_set = [f for f in MODE_FLAGS if row[f] == 1]
        if len(flags_set) == 0:
            return "Unclassified"          # exclusion (a): 9 rows
        if len(flags_set) == 1:
            return flags_set[0]
        return flags_set[0] + " (+overlap)"  # exclusion (c): 24 rows, still ONE event

    real_failures = df[df["Machine failure"] == 1].copy()
    real_failures["failure_cause"] = real_failures.apply(classify_cause, axis=1)

    real_failures[[
        "UDI", "Asset ID", "Asset Name", "Equipment Class", "Criticality Tier",
        "failure_cause"
    ]].to_sql("failure_events", conn, if_exists="replace", index=False)

    excluded_rnf = df[(df["Machine failure"] == 0) & (df["RNF"] == 1)]
    print(f"Real failures counted (Machine failure=1): {len(real_failures):,}")
    print(f"  - of which Unclassified (no flag set):     {(real_failures['failure_cause']=='Unclassified').sum()}")
    print(f"  - of which overlapping flags (>1 set):     {real_failures['failure_cause'].str.contains('overlap').sum()}")
    print(f"Excluded rows (RNF=1 but Machine failure=0): {len(excluded_rnf)} — not counted, per exclusion (b)\n")

    # ------------------------------------------------------------------
    # STEP 4 — write the tier repair-time benchmark as its OWN lookup
    # table (kept separate from raw data, per the labeled-assumption rule)
    # ------------------------------------------------------------------
    print("=" * 70)
    print("STEP 4 — Writing tier_repair_benchmark lookup table")
    print("=" * 70)
    bench_df = pd.DataFrame(
        TIER_REPAIR_BENCHMARK,
        columns=["tier_code", "tier_name", "assumed_repair_hours", "source_note"]
    )
    bench_df.to_sql("tier_repair_benchmark", conn, if_exists="replace", index=False)
    print(bench_df.to_string(index=False))
    print()

    conn.commit()

    # ------------------------------------------------------------------
    # STEP 5 — SANITY CHECK (verification step) — must pass before
    # anything downstream gets treated as trustworthy
    # ------------------------------------------------------------------
    print("=" * 70)
    print("STEP 5 — SANITY CHECK (must all pass)")
    print("=" * 70)

    checks = []

    row_count = conn.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
    checks.append(("Row count == 10,000", row_count == 10000, f"got {row_count:,}"))

    null_total = 0
    for col in df.columns:
        n = conn.execute(f'SELECT COUNT(*) FROM readings WHERE "{col}" IS NULL').fetchone()[0]
        null_total += n
    checks.append(("Zero nulls across all 20 columns", null_total == 0, f"got {null_total} nulls"))

    tier_mismatches = conn.execute(
        "SELECT COUNT(*) FROM readings WHERE \"Criticality Tier\" != Type"
    ).fetchone()[0]
    checks.append(("Zero Criticality Tier / Type mismatches", tier_mismatches == 0, f"got {tier_mismatches}"))

    counted_failures = conn.execute("SELECT COUNT(*) FROM failure_events").fetchone()[0]
    checks.append(("Total counted failures == 339 (known real count)", counted_failures == 339, f"got {counted_failures}"))

    all_passed = True
    for name, passed, detail in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}  ({detail})")
        if not passed:
            all_passed = False

    print()
    if not all_passed:
        print("SANITY CHECK FAILED — stopping here. Do not trust mining_reliability.db until fixed.")
        conn.close()
        sys.exit(1)

    print("ALL SANITY CHECKS PASSED — mining_reliability.db is ready to query.")
    conn.close()


if __name__ == "__main__":
    main()
