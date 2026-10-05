# Disable FK checks to reset/clean tables before seeding
DISABLE_FOREIGN_KEYS = "SET FOREIGN_KEY_CHECKS = 0;"
ENABLE_FOREIGN_KEYS = "SET FOREIGN_KEY_CHECKS = 1;"

# Truncate commands
TRUNCATE_CLAIMS = "TRUNCATE TABLE claims;"
TRUNCATE_ITEMS = "TRUNCATE TABLE items;"
TRUNCATE_LOCATIONS = "TRUNCATE TABLE locations;"
TRUNCATE_ADMINISTRATORS = "TRUNCATE TABLE administrators;"
TRUNCATE_USERS = "TRUNCATE TABLE users;"

# Seed USERS table
SEED_USERS = """
INSERT INTO users (student_number, password_hash, first_name, last_name, email)
VALUES 
    ('STU22001', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Thabo', 'Mbeki', '22001@myuwc.ac.za'),
    ('STU22002', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Sipho', 'Dlamini', '22002@myuwc.ac.za'),
    ('STU22003', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Anika', 'Patel', '22003@myuwc.ac.za'),
    ('STU22004', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Lian', 'van der Merwe', '22004@myuwc.ac.za'),
    ('STU22005', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Nandi', 'Zuma', '22005@myuwc.ac.za');
"""

# Seed ADMINISTRATORS table
SEED_ADMINISTRATORS = """
INSERT INTO administrators (staff_number, password_hash, first_name, last_name, email, department)
VALUES 
    ('ADM90001', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'Carol', 'Danvers', 'cdanvers@uwc.ac.za', 'Campus Security'),
    ('ADM90002', '$2b$12$eImiTXuWVxfM37uY4JANjO...', 'David', 'Koma', 'dkoma@uwc.ac.za', 'Student Affairs');
"""

# Seed LOCATIONS table
SEED_LOCATIONS = """
INSERT INTO locations (building_name, room_number, description)
VALUES 
    ('Main Library', 'Level 2 Study Area', 'Near the quiet study cubicles'),
    ('Science Building', 'Lab 302', 'Computer Science laboratory'),
    ('Student Centre', 'Food Court', 'Seating area near the main entrance'),
    ('Sports Complex', 'Gymnasium', 'Main indoor basketball court');
"""

# Seed ITEMS table
SEED_ITEMS = """
INSERT INTO items (reporter_user_id, location_id, title, category, description, image_url, status)
VALUES 
    (1, 1, 'Dell XPS 15 Laptop', 'Electronics', 'Silver laptop with a black sleeve left on table 4.', 'https://img.uwc.ac.za/dell_xps.jpg', 'LOST'),
    (2, 2, 'Graphing Calculator', 'Electronics', 'Casio FX-9860GII calculator found on desk.', NULL, 'FOUND'),
    (3, 3, 'Leather Wallet', 'Valuables', 'Brown leather wallet containing student ID.', 'https://img.uwc.ac.za/wallet.jpg', 'CLAIMED'),
    (4, 1, 'Blue Water Bottle', 'Personal Items', 'Hydro Flask water bottle with university stickers.', NULL, 'FOUND'),
    (5, 4, 'Gym Bag & Shoes', 'Personal Items', 'Black Nike gym bag containing size 10 shoes.', NULL, 'LOST');
"""

# Seed CLAIMS table
SEED_CLAIMS = """
INSERT INTO claims (item_id, claimant_user_id, admin_id, claim_reason, proof_details, status, admin_notes)
VALUES 
    (1, 2, 1, 'I lost my Dell XPS laptop on Monday afternoon while studying.', 'Serial Number: CN-0XY123-UWC', 'APPROVED', 'Serial number verified against proof of purchase.'),
    (2, 3, NULL, 'The Casio calculator belongs to me; left it after CSC312 test.', 'Name written on back in black marker', 'SUBMITTED', NULL),
    (3, 4, 2, 'Dropped my brown wallet at the food court around lunchtime.', 'Contains driver license matching name', 'APPROVED', 'Identity confirmed in person at security desk.'),
    (4, 5, 1, 'My blue water bottle went missing from the main library.', 'Has a scratch on the bottom rim', 'UNDER_REVIEW', 'Awaiting physical verification from security desk.');
"""