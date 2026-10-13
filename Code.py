# team name: code warriors
# student numbers: 4363144, 4429119, 4346572, 4426381, 4323138, 4323584
# filename: Code.py

import argparse
from pathlib import Path

from DB import get_connection
import Queries
import Seed


QUERIES = (
    ("Query 1: Active Items Search (Medium)", Queries.QUERY_1_ACTIVE_ITEMS),
    ("Query 2: Location Summary (Medium)", Queries.QUERY_2_LOCATION_SUMMARY),
    ("Query 3: Users with Pending Claims (Medium)", Queries.QUERY_3_USERS_WITH_PENDING_CLAIMS),
    ("Query 4: Recent Valuables Filter (Medium)", Queries.QUERY_4_RECENT_VALUABLES),
    ("Query 5: Full Claim Audit Log (Complex)", Queries.QUERY_5_FULL_CLAIM_AUDIT),
    ("Query 6: Contested Locations (Complex)", Queries.QUERY_6_CONTESTED_LOCATIONS),
    ("Query 7: Admin Performance Analysis (Complex)", Queries.QUERY_7_ADMIN_PERFORMANCE),
    ("Query 8: High Activity Users (Complex)", Queries.QUERY_8_HIGH_ACTIVITY_USERS),
)


def initialize_schema(connection):
    schema_path = Path(__file__).resolve().with_name("schema.sql")
    statements = [statement.strip() for statement in schema_path.read_text(encoding="utf-8").split(";") if statement.strip()]

    with connection.cursor() as cursor:
        for statement in statements:
            cursor.execute(statement)

    connection.commit()
    print("Database tables are ready.")


def run_seeding(connection):
    with connection.cursor() as cursor:
        for table_name, statement in Seed.RESET_STATEMENTS:
            cursor.execute(statement)
            print(f"Cleared {table_name}.")

        for table_name, statement in Seed.SEED_STATEMENTS:
            cursor.execute(statement)
            print(f"Seeded {table_name}.")

    connection.commit()
    print("Sample data inserted successfully.")

# clean data dispaly
def display_rows(rows):
    if not rows:
        print("No records found.")
        return

    columns = tuple(rows[0].keys())
    formatted = [tuple("NULL" if row[column] is None else str(row[column]) for column in columns) for row in rows]
    widths = [max(len(column), *(len(row[i]) for row in formatted)) for i, column in enumerate(columns)]

    print(" | ".join(column.ljust(width) for column, width in zip(columns, widths)))
    print("-+-".join("-" * width for width in widths))

    for row in formatted:
        print(" | ".join(value.ljust(width) for value, width in zip(row, widths)))

    print(f"{len(rows)} row(s) returned.")


def run_queries(connection):
    with connection.cursor() as cursor:
        for title, statement in QUERIES:
            print(f"\n{title}")
            cursor.execute(statement)
            display_rows(cursor.fetchall())


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run the lost-and-found database queries.")
    parser.add_argument("--init-schema", action="store_true", help="Create missing database tables from schema.sql.")
    parser.add_argument("--reset-seed", action="store_true", help="Replace existing records with demonstration data.")
    args = parser.parse_args(argv)

    connection = None
    try:
        connection = get_connection()
        print("Database connected successfully.")

        if args.init_schema:
            initialize_schema(connection)

        if args.reset_seed:
            run_seeding(connection)

        run_queries(connection)
        return 0

    except Exception as error:
        if connection is not None:
            try:
                connection.rollback()
            except Exception:
                pass
        print(f"Database operation failed: {error}")
        return 1

    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    raise SystemExit(main())
