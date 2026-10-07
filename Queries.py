SEED_USERS = """
INSERT INTO users (student_number, password_hash, first_name, last_name, email)
VALUES 
    ('STU22001', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Thabo', 'Mbeki', '22001@myuwc.ac.za'),
    ('STU22002', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Sipho', 'Dlamini', '22002@myuwc.ac.za'),
    ('STU22003', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Anika', 'Patel', '22003@myuwc.ac.za'),
    ('STU22004', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Lian', 'van der Merwe', '22004@myuwc.ac.za'),
    ('STU22005', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Nandi', 'Zuma', '22005@myuwc.ac.za');
"""

SEED_ADMINISTRATORS = """
INSERT INTO administrators (staff_number, password_hash, first_name, last_name, email, department)
VALUES 
    ('ADM90001', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Carol', 'Danvers', 'cdanvers@uwc.ac.za', 'Campus Security'),
    ('ADM90002', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'David', 'Koma', 'dkoma@uwc.ac.za', 'Student Affairs');
"""

SEED_LOCATIONS = """
INSERT INTO locations (building_name, room_number, description)
VALUES 
    ('Main Library', 'Level 2 Study Area', 'Near the quiet study cubicles'),
    ('Science Building', 'Lab 302', 'Computer Science laboratory'),
    ('Student Centre', 'Food Court', 'Seating area near the entrance'),
    ('Sports Complex', 'Gymnasium', 'Main indoor basketball court');
"""

SEED_ITEMS = """
INSERT INTO items (reporter_user_id, location_id, title, category, description, status)
VALUES 
    (1, 1, 'Dell XPS 15 Laptop', 'Electronics', 'Silver laptop with a black sleeve left on table 4.', 'LOST'),
    (2, 2, 'Graphing Calculator', 'Electronics', 'Casio FX-9860GII calculator found on desk.', 'FOUND'),
    (3, 3, 'Leather Wallet', 'Valuables', 'Brown leather wallet containing student ID.', 'CLAIMED'),
    (4, 1, 'Blue Water Bottle', 'Personal Items', 'Hydro Flask water bottle with university stickers.', 'FOUND'),
    (5, 4, 'Gym Bag & Shoes', 'Personal Items', 'Black Nike gym bag containing size 10 shoes.', 'LOST');
"""

SEED_CLAIMS = """
INSERT INTO claims (item_id, claimant_user_id, admin_id, claim_reason, proof_details, status, admin_notes)
VALUES 
    (1, 2, 1, 'I lost my Dell XPS laptop on Monday afternoon while studying.', 'Serial Number: CN-0XY123-UWC', 'APPROVED', 'Serial number verified against proof of purchase.'),
    (2, 3, NULL, 'The Casio calculator belongs to me; left it after CSC312 test.', 'Name written on back in marker', 'SUBMITTED', NULL),
    (3, 4, 2, 'Dropped my brown wallet at the food court around lunchtime.', 'Contains driver license matching name', 'APPROVED', 'Identity confirmed in person.'),
    (4, 5, 1, 'My blue water bottle went missing from the main library.', 'Has a scratch on the bottom rim', 'UNDER_REVIEW', 'Awaiting verification from security desk.');
"""

QUERY_1_ACTIVE_ITEMS = """
SELECT 
    i.item_id,
    i.title,
    i.category,
    i.status,
    CONCAT(u.first_name, ' ', u.last_name) AS reporter_name,
    u.email AS reporter_email,
    COALESCE(CONCAT(l.building_name, ' - ', l.room_number), 'Location Unspecified') AS location_details
FROM items i
INNER JOIN users u ON i.reporter_user_id = u.user_id
LEFT JOIN locations l ON i.location_id = l.location_id
WHERE i.status IN ('LOST', 'FOUND')
ORDER BY i.created_at DESC;
"""

QUERY_2_LOCATION_SUMMARY = """
SELECT 
    l.building_name,
    COUNT(i.item_id) AS total_items_logged,
    COUNT(CASE WHEN i.status = 'FOUND' THEN 1 END) AS total_found,
    COUNT(CASE WHEN i.status = 'LOST' THEN 1 END) AS total_lost
FROM locations l
INNER JOIN items i ON l.location_id = i.location_id
GROUP BY l.location_id, l.building_name
ORDER BY total_items_logged DESC;
"""

QUERY_3_USERS_WITH_PENDING_CLAIMS = """
SELECT 
    u.user_id,
    u.student_number,
    CONCAT(u.first_name, ' ', u.last_name) AS claimant_name,
    u.email
FROM users u
WHERE u.user_id IN (
    SELECT DISTINCT claimant_user_id 
    FROM claims 
    WHERE status = 'SUBMITTED'
);
"""

QUERY_4_RECENT_VALUABLES = """
SELECT 
    item_id,
    title,
    category,
    description,
    created_at
FROM items
WHERE (category LIKE '%Electronics%' OR category LIKE '%Valuables%')
  AND created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
ORDER BY created_at DESC;
"""

QUERY_5_FULL_CLAIM_AUDIT = """
SELECT 
    c.claim_id,
    i.title AS item_title,
    i.category AS item_category,
    CONCAT(u_claimant.first_name, ' ', u_claimant.last_name) AS claimant_name,
    c.status AS claim_status,
    COALESCE(CONCAT(a.first_name, ' ', a.last_name), 'Unassigned / Pending') AS reviewed_by_admin,
    COALESCE(c.admin_notes, 'No review notes provided') AS review_notes
FROM claims c
INNER JOIN items i ON c.item_id = i.item_id
INNER JOIN users u_claimant ON c.claimant_user_id = u_claimant.user_id
LEFT JOIN administrators a ON c.admin_id = a.admin_id
ORDER BY c.created_at DESC;
"""

QUERY_6_CONTESTED_LOCATIONS = """
SELECT 
    l.location_id,
    l.building_name,
    COUNT(DISTINCT i.item_id) AS items_with_claims,
    COUNT(c.claim_id) AS total_claims_filed
FROM locations l
INNER JOIN items i ON l.location_id = i.location_id
INNER JOIN claims c ON i.item_id = c.item_id
GROUP BY l.location_id, l.building_name
HAVING COUNT(c.claim_id) >= 1
ORDER BY total_claims_filed DESC;
"""

QUERY_7_ADMIN_PERFORMANCE = """
SELECT 
    a.admin_id,
    CONCAT(a.first_name, ' ', a.last_name) AS admin_name,
    a.department,
    COUNT(c.claim_id) AS total_claims_processed,
    SUM(CASE WHEN c.status = 'APPROVED' THEN 1 ELSE 0 END) AS approved_claims,
    SUM(CASE WHEN c.status = 'REJECTED' THEN 1 ELSE 0 END) AS rejected_claims
FROM administrators a
INNER JOIN claims c ON a.admin_id = c.admin_id
GROUP BY a.admin_id, admin_name, a.department
HAVING COUNT(c.claim_id) >= 1
ORDER BY total_claims_processed DESC;
"""

QUERY_8_HIGH_ACTIVITY_USERS = """
SELECT 
    u.user_id,
    u.student_number,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    COUNT(DISTINCT i.item_id) AS total_items_reported,
    COUNT(DISTINCT c.claim_id) AS total_claims_submitted
FROM users u
LEFT JOIN items i ON u.user_id = i.reporter_user_id
LEFT JOIN claims c ON u.user_id = c.claimant_user_id
GROUP BY u.user_id, u.student_number, full_name
HAVING (COUNT(DISTINCT i.item_id) + COUNT(DISTINCT c.claim_id)) > (
    SELECT AVG(activity_count)
    FROM (
        SELECT (COUNT(DISTINCT items.item_id) + COUNT(DISTINCT claims.claim_id)) AS activity_count
        FROM users
        LEFT JOIN items ON users.user_id = items.reporter_user_id
        LEFT JOIN claims ON users.user_id = claims.claimant_user_id
        GROUP BY users.user_id
    ) AS user_totals
)
ORDER BY (total_items_reported + total_claims_submitted) DESC;
"""