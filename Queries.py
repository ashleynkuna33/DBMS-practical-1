# team name: code warriors
# student numbers: 4363144, 4429119, 4346572, 4426381, 4323138, 4323584
# filename: Queries.py

QUERY_1_ACTIVE_ITEMS = """
SELECT
    i.item_id,
    i.title,
    i.category,
    i.status,
    CONCAT(u.first_name, ' ', u.last_name) AS reporter_name,
    u.email AS reporter_email,
    COALESCE(CONCAT_WS(' - ', l.building_name, l.room_number), 'Location Unspecified') AS location_details
FROM items AS i
INNER JOIN users AS u ON u.user_id = i.reporter_user_id
LEFT JOIN locations AS l ON l.location_id = i.location_id
WHERE i.status IN ('LOST', 'FOUND')
ORDER BY i.created_at DESC, i.item_id DESC;
"""

QUERY_2_LOCATION_SUMMARY = """
SELECT
    l.location_id,
    l.building_name,
    l.room_number,
    COUNT(i.item_id) AS total_items_logged,
    SUM(CASE WHEN i.status = 'FOUND' THEN 1 ELSE 0 END) AS total_found,
    SUM(CASE WHEN i.status = 'LOST' THEN 1 ELSE 0 END) AS total_lost,
    SUM(CASE WHEN i.status = 'CLAIMED' THEN 1 ELSE 0 END) AS total_claimed
FROM locations AS l
LEFT JOIN items AS i ON i.location_id = l.location_id
GROUP BY l.location_id, l.building_name, l.room_number
ORDER BY total_items_logged DESC, l.building_name;
"""

QUERY_3_USERS_WITH_PENDING_CLAIMS = """
SELECT
    u.user_id,
    u.student_number,
    CONCAT(u.first_name, ' ', u.last_name) AS claimant_name,
    u.email,
    (SELECT COUNT(*)
     FROM claims AS c
     WHERE c.claimant_user_id = u.user_id
       AND c.status IN ('SUBMITTED', 'UNDER_REVIEW')) AS pending_claims
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM claims AS c
    WHERE c.claimant_user_id = u.user_id
      AND c.status IN ('SUBMITTED', 'UNDER_REVIEW')
)
ORDER BY pending_claims DESC, u.user_id;
"""

QUERY_4_RECENT_VALUABLES = """
SELECT
    i.item_id,
    i.title,
    i.category,
    i.description,
    i.status,
    i.created_at
FROM items AS i
WHERE (i.category LIKE '%Electronics%' OR i.category LIKE '%Valuables%')
  AND i.created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
ORDER BY i.created_at DESC, i.item_id DESC;
"""

QUERY_5_FULL_CLAIM_AUDIT = """
SELECT
    c.claim_id,
    i.title AS item_title,
    i.category AS item_category,
    i.status AS item_status,
    CONCAT(reporter.first_name, ' ', reporter.last_name) AS reported_by,
    CONCAT(claimant.first_name, ' ', claimant.last_name) AS claimant_name,
    c.claim_reason,
    c.status AS claim_status,
    COALESCE(CONCAT(a.first_name, ' ', a.last_name), 'Unassigned') AS reviewed_by_admin,
    COALESCE(c.admin_notes, 'No review notes provided') AS review_notes,
    c.created_at AS submitted_at
FROM claims AS c
INNER JOIN items AS i ON i.item_id = c.item_id
INNER JOIN users AS claimant ON claimant.user_id = c.claimant_user_id
INNER JOIN users AS reporter ON reporter.user_id = i.reporter_user_id
LEFT JOIN administrators AS a ON a.admin_id = c.admin_id
ORDER BY c.created_at DESC, c.claim_id DESC;
"""

QUERY_6_CONTESTED_LOCATIONS = """
SELECT
    l.location_id,
    l.building_name,
    l.room_number,
    COUNT(DISTINCT i.item_id) AS contested_items,
    SUM(contested.claimant_count) AS competing_claims,
    MAX(contested.claimant_count) AS most_claimants_for_one_item
FROM locations AS l
INNER JOIN items AS i ON i.location_id = l.location_id
INNER JOIN (
    SELECT
        c.item_id,
        COUNT(DISTINCT c.claimant_user_id) AS claimant_count
    FROM claims AS c
    GROUP BY c.item_id
    HAVING COUNT(DISTINCT c.claimant_user_id) >= 2
) AS contested ON contested.item_id = i.item_id
GROUP BY l.location_id, l.building_name, l.room_number
HAVING COUNT(DISTINCT i.item_id) >= 1
ORDER BY competing_claims DESC, contested_items DESC;
"""

QUERY_7_ADMIN_PERFORMANCE = """
SELECT
    a.admin_id,
    CONCAT(a.first_name, ' ', a.last_name) AS admin_name,
    a.department,
    COUNT(c.claim_id) AS assigned_claims,
    SUM(CASE WHEN c.status IN ('APPROVED', 'REJECTED') THEN 1 ELSE 0 END) AS completed_claims,
    SUM(CASE WHEN c.status = 'APPROVED' THEN 1 ELSE 0 END) AS approved_claims,
    SUM(CASE WHEN c.status = 'REJECTED' THEN 1 ELSE 0 END) AS rejected_claims,
    SUM(CASE WHEN c.status = 'UNDER_REVIEW' THEN 1 ELSE 0 END) AS under_review_claims,
    COUNT(DISTINCT i.category) AS item_categories_handled,
    COALESCE(ROUND(
        100.0 * SUM(CASE WHEN c.status = 'APPROVED' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN c.status IN ('APPROVED', 'REJECTED') THEN 1 ELSE 0 END), 0), 1
    ), 0) AS approval_rate_pct,
    CASE
        WHEN SUM(CASE WHEN c.status IN ('APPROVED', 'REJECTED') THEN 1 ELSE 0 END) > (
            SELECT AVG(admin_totals.completed_count)
            FROM (
                SELECT
                    a2.admin_id,
                    SUM(CASE WHEN c2.status IN ('APPROVED', 'REJECTED') THEN 1 ELSE 0 END) AS completed_count
                FROM administrators AS a2
                LEFT JOIN claims AS c2 ON c2.admin_id = a2.admin_id
                GROUP BY a2.admin_id
            ) AS admin_totals
        ) THEN 'Above average'
        ELSE 'At or below average'
    END AS completion_workload
FROM administrators AS a
LEFT JOIN claims AS c ON c.admin_id = a.admin_id
LEFT JOIN items AS i ON i.item_id = c.item_id
GROUP BY a.admin_id, a.first_name, a.last_name, a.department
ORDER BY completed_claims DESC, a.admin_id;
"""

QUERY_8_HIGH_ACTIVITY_USERS = """
SELECT
    u.user_id,
    u.student_number,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    COUNT(DISTINCT i.item_id) AS total_items_reported,
    COUNT(DISTINCT c.claim_id) AS total_claims_submitted,
    COUNT(DISTINCT i.item_id) + COUNT(DISTINCT c.claim_id) AS total_activity
FROM users AS u
LEFT JOIN items AS i ON i.reporter_user_id = u.user_id
LEFT JOIN claims AS c ON c.claimant_user_id = u.user_id
GROUP BY u.user_id, u.student_number, u.first_name, u.last_name
HAVING total_activity > (
    SELECT AVG(user_totals.activity_count)
    FROM (
        SELECT
            u2.user_id,
            COUNT(DISTINCT i2.item_id) + COUNT(DISTINCT c2.claim_id) AS activity_count
        FROM users AS u2
        LEFT JOIN items AS i2 ON i2.reporter_user_id = u2.user_id
        LEFT JOIN claims AS c2 ON c2.claimant_user_id = u2.user_id
        GROUP BY u2.user_id
    ) AS user_totals
)
ORDER BY total_activity DESC, u.user_id;
"""
