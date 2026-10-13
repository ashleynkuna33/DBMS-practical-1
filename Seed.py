# team name: code warriors
# student numbers: 4363144, 4429119, 4346572, 4426381, 4323138, 4323584
# filename: Seed.py

# useless password hash
DEMO_HASH = "$2b$10$5D17949VnIdkB7XwT3pMMOE2oEVsBlIYkB8l8FEJ/jiKPpy1PEwNy"

RESET_STATEMENTS = (
    ("claims", "DELETE FROM claims"),
    ("items", "DELETE FROM items"),
    ("locations", "DELETE FROM locations"),
    ("administrators", "DELETE FROM administrators"),
    ("users", "DELETE FROM users"),
)

SEED_USERS = f"""
INSERT INTO users (user_id, student_number, password_hash, first_name, last_name, email)
VALUES
    (1, 'STU22001', '{DEMO_HASH}', 'Thabo', 'Mbeki', '22001@myuwc.ac.za'),
    (2, 'STU22002', '{DEMO_HASH}', 'Sipho', 'Dlamini', '22002@myuwc.ac.za'),
    (3, 'STU22003', '{DEMO_HASH}', 'Anika', 'Patel', '22003@myuwc.ac.za'),
    (4, 'STU22004', '{DEMO_HASH}', 'Lian', 'van der Merwe', '22004@myuwc.ac.za'),
    (5, 'STU22005', '{DEMO_HASH}', 'Nandi', 'Zuma', '22005@myuwc.ac.za'),
    (6, 'STU22006', '{DEMO_HASH}', 'Lerato', 'Mokoena', '22006@myuwc.ac.za'),
    (7, 'STU22007', '{DEMO_HASH}', 'Zanele', 'Ndlovu', '22007@myuwc.ac.za'),
    (8, 'STU22008', '{DEMO_HASH}', 'Musa', 'Khumalo', '22008@myuwc.ac.za'),
    (9, 'STU22009', '{DEMO_HASH}', 'Busi', 'Naidoo', '22009@myuwc.ac.za');
"""

SEED_ADMINISTRATORS = f"""
INSERT INTO administrators (admin_id, staff_number, password_hash, first_name, last_name, email, department)
VALUES
    (1, 'ADM90001', '{DEMO_HASH}', 'Carol', 'Danvers', 'cdanvers@uwc.ac.za', 'Campus Security'),
    (2, 'ADM90002', '{DEMO_HASH}', 'David', 'Koma', 'dkoma@uwc.ac.za', 'Student Affairs'),
    (3, 'ADM90003', '{DEMO_HASH}', 'Amira', 'Jacobs', 'ajacobs@uwc.ac.za', 'Student Services');
"""

SEED_LOCATIONS = """
INSERT INTO locations (location_id, building_name, room_number, description)
VALUES
    (1, 'Main Library', 'Level 2 Study Area', 'Near the quiet study cubicles'),
    (2, 'Science Building', 'Lab 302', 'Computer Science laboratory'),
    (3, 'Student Centre', 'Food Court', 'Seating area near the main entrance'),
    (4, 'Sports Complex', 'Gymnasium', 'Main indoor basketball court'),
    (5, 'Innovation Hub', 'Reception', 'Main reception and help desk');
"""

SEED_ITEMS = """
INSERT INTO items (item_id, reporter_user_id, location_id, title, category, description, image_url, status, created_at)
VALUES
    (1, 1, 1, 'Dell XPS 15 Laptop', 'Electronics', 'Silver laptop with a black sleeve left on table 4.', NULL, 'LOST', NOW() - INTERVAL 2 DAY),
    (2, 2, 2, 'Graphing Calculator', 'Electronics', 'Casio FX-9860GII calculator found on a laboratory desk.', NULL, 'FOUND', NOW() - INTERVAL 3 DAY),
    (3, 3, 3, 'Leather Wallet', 'Valuables', 'Brown leather wallet containing a student card.', NULL, 'CLAIMED', NOW() - INTERVAL 8 DAY),
    (4, 4, 1, 'Blue Water Bottle', 'Personal Items', 'Hydro Flask water bottle with university stickers.', NULL, 'FOUND', NOW() - INTERVAL 1 DAY),
    (5, 5, 4, 'Gym Bag and Shoes', 'Personal Items', 'Black gym bag containing size 10 shoes.', NULL, 'LOST', NOW() - INTERVAL 6 DAY),
    (6, 6, 3, 'Student Access Card', 'Valuables', 'Student access card in a clear holder.', NULL, 'FOUND', NOW() - INTERVAL 4 DAY),
    (7, 7, 4, 'Smartwatch', 'Electronics', 'Black smartwatch with a cracked screen protector.', NULL, 'FOUND', NOW() - INTERVAL 5 DAY),
    (8, 8, 5, 'House Keys', 'Valuables', 'Two silver keys attached to a green keyring.', NULL, 'CLAIMED', NOW() - INTERVAL 9 DAY),
    (9, 1, 5, 'Wireless Earbuds', 'Electronics', 'White earbud case found at reception.', NULL, 'FOUND', NOW() - INTERVAL 1 DAY),
    (10, 1, 2, 'Database Textbook', 'Books', 'Database systems textbook with notes inside.', NULL, 'LOST', NOW() - INTERVAL 12 DAY),
    (11, 2, 1, 'Android Tablet', 'Electronics', 'Black tablet in a dark grey protective case.', NULL, 'FOUND', NOW() - INTERVAL 35 DAY),
    (12, 3, 2, 'USB Flash Drive', 'Electronics', 'Blue 64GB USB flash drive.', NULL, 'FOUND', NOW() - INTERVAL 11 DAY),
    (13, 4, 4, 'Denim Jacket', 'Clothing', 'Dark blue jacket with a torn inner label.', NULL, 'CLAIMED', NOW() - INTERVAL 7 DAY),
    (14, 1, 3, 'Over-Ear Headphones', 'Electronics', 'Black noise-cancelling headphones in a pouch.', NULL, 'LOST', NOW() - INTERVAL 2 DAY);
"""

SEED_CLAIMS = """
INSERT INTO claims (claim_id, item_id, claimant_user_id, admin_id, claim_reason, proof_details, status, admin_notes, created_at)
VALUES
    (1, 2, 3, NULL, 'I left my calculator after the CSC312 test.', 'My initials are written on the back.', 'SUBMITTED', NULL, NOW() - INTERVAL 2 DAY),
    (2, 2, 4, 1, 'The calculator looks like mine.', 'Could not provide a matching serial number.', 'REJECTED', 'Ownership could not be verified.', NOW() - INTERVAL 2 DAY),
    (3, 3, 4, 2, 'My wallet was lost at the food court.', 'The identification matches my name.', 'APPROVED', 'Identity confirmed in person.', NOW() - INTERVAL 7 DAY),
    (4, 4, 5, 1, 'The blue water bottle belongs to me.', 'A scratch is visible underneath.', 'UNDER_REVIEW', 'Waiting for physical verification.', NOW() - INTERVAL 1 DAY),
    (5, 6, 1, NULL, 'My student access card disappeared at lunch.', 'The back contains my student number.', 'SUBMITTED', NULL, NOW() - INTERVAL 3 DAY),
    (6, 6, 8, 2, 'I may have lost my access card at the centre.', 'The card has a damaged corner.', 'UNDER_REVIEW', 'Student number verification required.', NOW() - INTERVAL 2 DAY),
    (7, 7, 2, NULL, 'I left my smartwatch at the gym.', 'Watch face configuration and PIN available.', 'SUBMITTED', NULL, NOW() - INTERVAL 4 DAY),
    (8, 7, 5, 3, 'The smartwatch may be mine.', 'The reported strap colour does not match.', 'REJECTED', 'Ownership evidence did not match.', NOW() - INTERVAL 3 DAY),
    (9, 8, 6, 1, 'The house keys were on my keyring.', 'Matching lock demonstrated at security.', 'APPROVED', 'Keys returned to the verified owner.', NOW() - INTERVAL 8 DAY),
    (10, 9, 3, NULL, 'The earbuds disappeared during my visit.', 'Original case receipt available.', 'SUBMITTED', NULL, NOW() - INTERVAL 1 DAY),
    (11, 11, 1, 2, 'I lost my tablet near the library shelves.', 'Device serial number submitted.', 'UNDER_REVIEW', 'Proof of purchase is being checked.', NOW() - INTERVAL 3 DAY),
    (12, 12, 8, 3, 'The flash drive looks like mine.', 'Could not describe files stored on it.', 'REJECTED', 'Insufficient identifying details.', NOW() - INTERVAL 10 DAY),
    (13, 2, 8, NULL, 'A calculator of this model went missing.', 'The calculator may have a worn battery cover.', 'SUBMITTED', NULL, NOW() - INTERVAL 1 DAY),
    (14, 13, 7, 3, 'The denim jacket belongs to me.', 'The inner stitching matches my photograph.', 'APPROVED', 'Jacket handed to the claimant.', NOW() - INTERVAL 6 DAY),
    (15, 4, 6, 2, 'I also lost a blue water bottle.', 'The colour does not match the recovered bottle.', 'REJECTED', 'The item was not a match.', NOW() - INTERVAL 1 DAY),
    (16, 11, 3, NULL, 'My tablet may have been found in the library.', 'Can provide the device unlock code.', 'SUBMITTED', NULL, NOW() - INTERVAL 2 DAY),
    (17, 9, 4, NULL, 'I lost white wireless earbuds at reception.', 'A photograph of the case is available.', 'SUBMITTED', NULL, NOW() - INTERVAL 1 DAY);
"""

SEED_STATEMENTS = (
    ("users", SEED_USERS),
    ("administrators", SEED_ADMINISTRATORS),
    ("locations", SEED_LOCATIONS),
    ("items", SEED_ITEMS),
    ("claims", SEED_CLAIMS),
)
