-- ============================================================
-- core_queries.sql
-- Day 9, Mining Reliability Reporting project.
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
-- ============================================================

DROP VIEW IF EXISTS v_failure_mode_pareto;
CREATE VIEW v_failure_mode_pareto AS
SELECT
    CASE
        WHEN failure_cause LIKE '% (+overlap)'
            THEN SUBSTR(failure_cause, 1, INSTR(failure_cause, ' (+overlap)') - 1)
        ELSE failure_cause
    END AS failure_mode,
    COUNT(*) AS failure_count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM failure_events), 1) AS pct_of_total,
    SUM(CASE WHEN failure_cause LIKE '% (+overlap)' THEN 1 ELSE 0 END) AS of_which_had_a_second_flag_too
FROM failure_events
GROUP BY failure_mode
ORDER BY failure_count DESC;

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
        ELSE 'Hours = failure count x assumed repair time per event (Data Dictionary Section 3.1, cited mine-site sources).'
    END AS disclosure_note
FROM readings r
JOIN tier_repair_benchmark b ON r."Criticality Tier" = b.tier_code
WHERE r."Machine failure" = 1
GROUP BY r."Criticality Tier", b.tier_name, b.assumed_repair_hours
ORDER BY r."Criticality Tier";
