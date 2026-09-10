-- ============================================================
-- core_queries.sql
-- Day 9, Mining Reliability Reporting project.
-- REVISED 10 Sept 2026 — see revision note below and
-- Scope-Decisions-and-Limitations-Log.md, 10 Sept 2026 entry.
--
-- Three core queries, saved as VIEWs inside mining_reliability.db
-- so they're ready to click on in DB Browser for SQLite without
-- retyping anything. Each one follows the rules already locked in
-- 05-Data-Dictionary.md and enforced by load_to_sqlite.py:
--   - counts come from failure_events (source-of-truth rule +
--     3 data-quality exclusions already applied when this table
--     was built)
--   - repair-time hours are only ever applied to the Mobile fleet
--     (Medium tier) via the separate tier_repair_benchmark lookup
--   - Fixed plant and Ancillary always show a disclosed reason,
--     never a blank cell, per the Financial Controller's Q6
--     presentation requirement (Scope-Decisions-and-Limitations-Log,
--     3 Sept 2026)
--
-- REVISION NOTE (10 Sept 2026) — v_failure_mode_pareto reworked:
-- An independent fresh-context review (same red-team technique used
-- on the BRD) found that the original version of this view silently
-- under-counted OSF (and, to a lesser extent, PWF) because of the
-- tie-break rule in load_to_sqlite.py's classify_cause(): when a row
-- has more than one mode flag set, only the first flag in the fixed
-- order [TWF, HDF, PWF, OSF, RNF] gets credited as the row's ONE
-- "primary cause" (required so the Pareto still sums to 339 and
-- never double-counts the 24 overlap rows — see the Data Dictionary
-- rule this must still respect). OSF is last in that list, so every
-- time it co-occurs with an earlier-listed flag, it loses the tie
-- and disappears from the original single-count Pareto — even though
-- it genuinely happened. That mattered specifically because Q5 (the
-- overstrain/torque-threshold question) depends on OSF's true rate.
--
-- Fix: this view now reports BOTH numbers, side by side, instead of
-- picking one silently:
--   - primary_cause_count / primary_cause_pct = the original,
--     mutually-exclusive, one-row-one-cause count. Still sums to
--     339. Still the right number for "how many discrete failure
--     EVENTS were mainly caused by X" and for the overall Pareto bar
--     chart's headline ranking.
--   - true_occurrence_count / true_occurrence_pct = how many real
--     failures had this flag set AT ALL, regardless of tie-break.
--     Deliberately does NOT sum to 339 (a row with 2 flags set is
--     counted once under each flag) — this is a different question
--     ("how often is this mode involved") answered on purpose, not
--     a violation of the "count by event, not by flag" rule, which
--     still governs primary_cause_count and the 339 failure total.
--   - additional_occurrences = the gap between the two, i.e. exactly
--     how much a given mode was undercounted by the tie-break rule.
-- ============================================================

DROP VIEW IF EXISTS v_failure_mode_pareto;
CREATE VIEW v_failure_mode_pareto AS
WITH primary_cause AS (
    SELECT
        CASE
            WHEN failure_cause LIKE '% (+overlap)'
                THEN SUBSTR(failure_cause, 1, INSTR(failure_cause, ' (+overlap)') - 1)
            ELSE failure_cause
        END AS failure_mode,
        COUNT(*) AS primary_cause_count
    FROM failure_events
    GROUP BY failure_mode
),
true_occurrence AS (
    SELECT 'TWF' AS failure_mode, SUM(TWF) AS true_occurrence_count FROM readings WHERE "Machine failure" = 1
    UNION ALL
    SELECT 'HDF', SUM(HDF) FROM readings WHERE "Machine failure" = 1
    UNION ALL
    SELECT 'PWF', SUM(PWF) FROM readings WHERE "Machine failure" = 1
    UNION ALL
    SELECT 'OSF', SUM(OSF) FROM readings WHERE "Machine failure" = 1
    UNION ALL
    SELECT 'RNF', SUM(RNF) FROM readings WHERE "Machine failure" = 1
)
SELECT
    t.failure_mode,
    COALESCE(p.primary_cause_count, 0) AS primary_cause_count,
    ROUND(100.0 * COALESCE(p.primary_cause_count, 0) / (SELECT COUNT(*) FROM failure_events), 1) AS primary_cause_pct,
    t.true_occurrence_count,
    ROUND(100.0 * t.true_occurrence_count / (SELECT COUNT(*) FROM failure_events), 1) AS true_occurrence_pct,
    t.true_occurrence_count - COALESCE(p.primary_cause_count, 0) AS additional_occurrences_hidden_by_tiebreak,
    'primary_cause_count sums to 339 (one row = one event, per the Data Dictionary rule); true_occurrence_count intentionally does not (a row with 2+ flags is counted under each) — use true_occurrence for "how often is this mode really present," primary_cause for the headline event-count ranking.' AS disclosure_note
FROM true_occurrence t
LEFT JOIN primary_cause p ON p.failure_mode = t.failure_mode
UNION ALL
SELECT
    p.failure_mode,
    p.primary_cause_count,
    ROUND(100.0 * p.primary_cause_count / (SELECT COUNT(*) FROM failure_events), 1),
    0 AS true_occurrence_count,
    0.0 AS true_occurrence_pct,
    0 AS additional_occurrences_hidden_by_tiebreak,
    'Rows with Machine failure=1 but no mode flag set at all (9 rows) — has no "true occurrence" counterpart by definition.' AS disclosure_note
FROM primary_cause p
WHERE p.failure_mode = 'Unclassified'
ORDER BY true_occurrence_count DESC;

DROP VIEW IF EXISTS v_failure_rate_by_tier;
CREATE VIEW v_failure_rate_by_tier AS
SELECT
    "Criticality Tier" AS tier,
    CASE "Criticality Tier"
        WHEN 'H' THEN 'Fixed plant'
        WHEN 'M' THEN 'Mobile fleet'
        WHEN 'L' THEN 'Ancillary'
    END AS tier_name,
    COUNT(*) AS total_readings,
    SUM("Machine failure") AS failure_count,
    ROUND(100.0 * SUM("Machine failure") / COUNT(*), 2) AS failure_rate_pct
FROM readings
GROUP BY "Criticality Tier"
ORDER BY failure_rate_pct DESC;

DROP VIEW IF EXISTS v_downtime_hours_by_tier;
CREATE VIEW v_downtime_hours_by_tier AS
SELECT
    r."Criticality Tier" AS tier,
    b.tier_name,
    COUNT(*) AS failure_count,
    b.assumed_repair_hours,
    CASE
        WHEN b.assumed_repair_hours IS NOT NULL
            THEN ROUND(COUNT(*) * b.assumed_repair_hours, 1)
        ELSE NULL
    END AS estimated_downtime_hours,
    CASE
        WHEN b.assumed_repair_hours IS NULL
            THEN 'Frequency only — no defensible repair-time source for this tier (Data Dictionary Section 3.1). Not a blank: a disclosed scope boundary.'
        ELSE 'Hours = failure count x 2.2 hrs, a typical-case average from cited mine-site sources (Data Dictionary Section 3.1). Individual repairs documented in those same sources run as long as 45 hrs — this figure is a central estimate, not an upper bound. Revised 10 Sept 2026 to add this range caveat.'
    END AS disclosure_note
FROM readings r
JOIN tier_repair_benchmark b ON r."Criticality Tier" = b.tier_code
WHERE r."Machine failure" = 1
GROUP BY r."Criticality Tier", b.tier_name, b.assumed_repair_hours
ORDER BY r."Criticality Tier";

-- ============================================================
-- KNOWN LIMITATION (documented, not fixed — n=1, low materiality)
-- One row has both TWF and RNF set simultaneously (Machine failure=1).
-- Under the tie-break rule, this row's primary_cause_count credits
-- TWF (TWF is earlier in the fixed order than RNF). For Q4
-- (preventable vs. random failure classification), this single row
-- is genuinely ambiguous: it could be read as a preventable tool-wear
-- failure that happened to also trip the random-failure flag, or as
-- a coincidental double-flag. Left as a disclosed one-row edge case
-- rather than special-cased in SQL, since a bespoke rule for n=1
-- would add more complexity than the row's materiality justifies.
-- Found in the 10 Sept 2026 independent review — see
-- Scope-Decisions-and-Limitations-Log.md, 10 Sept 2026 entry.
-- ============================================================
