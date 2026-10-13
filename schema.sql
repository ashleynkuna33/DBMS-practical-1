CREATE DATABASE IF NOT EXISTS lost_and_found_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lost_and_found_db;

CREATE TABLE IF NOT EXISTS users (
    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    student_number VARCHAR(20) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id),
    UNIQUE KEY uq_users_student_number (student_number),
    UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS administrators (
    admin_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    staff_number VARCHAR(20) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(80) NOT NULL,
    last_name VARCHAR(80) NOT NULL,
    email VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (admin_id),
    UNIQUE KEY uq_administrators_staff_number (staff_number),
    UNIQUE KEY uq_administrators_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS locations (
    location_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    building_name VARCHAR(120) NOT NULL,
    room_number VARCHAR(120) NOT NULL,
    description TEXT NULL,
    PRIMARY KEY (location_id),
    UNIQUE KEY uq_locations_building_room (building_name, room_number)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS items (
    item_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    reporter_user_id INT UNSIGNED NOT NULL,
    location_id INT UNSIGNED NULL,
    title VARCHAR(180) NOT NULL,
    category VARCHAR(80) NOT NULL,
    description TEXT NOT NULL,
    image_url VARCHAR(2048) NULL,
    status ENUM('LOST', 'FOUND', 'CLAIMED') NOT NULL DEFAULT 'LOST',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (item_id),
    KEY idx_items_reporter (reporter_user_id),
    KEY idx_items_location (location_id),
    KEY idx_items_status_date (status, created_at),
    CONSTRAINT fk_items_reporter FOREIGN KEY (reporter_user_id) REFERENCES users (user_id) ON DELETE RESTRICT,
    CONSTRAINT fk_items_location FOREIGN KEY (location_id) REFERENCES locations (location_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS claims (
    claim_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    item_id INT UNSIGNED NOT NULL,
    claimant_user_id INT UNSIGNED NOT NULL,
    admin_id INT UNSIGNED NULL,
    claim_reason TEXT NOT NULL,
    proof_details TEXT NOT NULL,
    status ENUM('SUBMITTED', 'UNDER_REVIEW', 'APPROVED', 'REJECTED') NOT NULL DEFAULT 'SUBMITTED',
    admin_notes TEXT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (claim_id),
    UNIQUE KEY uq_claims_item_claimant (item_id, claimant_user_id),
    KEY idx_claims_claimant_status (claimant_user_id, status),
    KEY idx_claims_admin (admin_id),
    KEY idx_claims_status (status),
    CONSTRAINT fk_claims_item FOREIGN KEY (item_id) REFERENCES items (item_id) ON DELETE RESTRICT,
    CONSTRAINT fk_claims_claimant FOREIGN KEY (claimant_user_id) REFERENCES users (user_id) ON DELETE RESTRICT,
    CONSTRAINT fk_claims_admin FOREIGN KEY (admin_id) REFERENCES administrators (admin_id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
