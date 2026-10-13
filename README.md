# CSC312 Practical Assignment 2 — Lost and Found Database
A MySQL-backed Python demonstration of a university lost-and-found system, including reporting lost and found items, ownership claims, review by administrators, and eight medium/complex retrieval queries.

## Requirements
Python 3.9 or newer, MySQL 8.0 or newer, and an existing MySQL database that your account can access.

## Setup
1. Install dependencies using `python -m pip install -r requirements.txt`.
2. Copy `.env.example` to `.env` and fill in your own database host, port, username, password, and database name. The `.env` file is excluded from Git.
3. Create the MySQL database if it does not already exist. University-provided databases may already exist.
4. Run `python Code.py --init-schema --reset-seed` to create any missing tables, insert demonstration records, and execute all eight queries.
5. Run `python Code.py` to execute the queries again without changing database records.

**Warning:** `--reset-seed` deletes all rows in `claims`, `items`, `locations`, `administrators`, and `users`, then replaces them with demonstration data. Use this option only in a disposable assignment database. The reset runs in a transaction, so a seeding error rolls back the deletes and inserts. It does not drop tables.

`--init-schema` creates missing tables. It does not alter existing tables, so start with an empty database or verify that your existing table structures match `schema.sql`.

## Files
- `Code.py`: command-line entry point, schema initialization, optional data reset, and query output.
- `DB.py`: MySQL connection using environment variables.
- `Queries.py`: eight retrieval queries.
- `Seed.py`: demonstration records and reset operations.
- `schema.sql`: five related MySQL tables, keys, constraints, and indexes.
- `requirements.txt`: Python dependencies.
- `.env.example`: database configuration template.

## Query coverage
1. Active lost-and-found items with their reporters and locations.
2. Total, lost, found, and claimed items per location.
3. Users with submitted or under-review claims.
4. Valuable or electronic items reported in the last 30 days.
5. Claim audit information including reporters, claimants, and administrators.
6. Locations with items claimed by at least two distinct users.
7. Administrator approval, rejection, and workload metrics.
8. Users with reporting and claim activity above the average.

## Submission
git repo: https://github.com/ashleynkuna33/DBMS-practical-1
