from DB import get_connection
import Seed as seed
import Queries


def run_seeding(cursor):
    """Disables foreign key constraints, resets tables, and populates initial sample data."""
    print("\n" + "=" * 60)
    print("1. SEEDING DATABASE DATA")
    print("=" * 60)

    # Disable foreign keys to clear existing tables safely
    cursor.execute(seed.DISABLE_FOREIGN_KEYS)

    tables_to_truncate = [
        ("CLAIMS", seed.TRUNCATE_CLAIMS),
        ("ITEMS", seed.TRUNCATE_ITEMS),
        ("LOCATIONS", seed.TRUNCATE_LOCATIONS),
        ("ADMINISTRATORS", seed.TRUNCATE_ADMINISTRATORS),
        ("USERS", seed.TRUNCATE_USERS),
    ]

    for table_name, truncate_stmt in tables_to_truncate:
        cursor.execute(truncate_stmt)
        print(f"Cleared table: {table_name}")

    # Re-enable foreign key checks
    cursor.execute(seed.ENABLE_FOREIGN_KEYS)

    # Insert initial seed records in order of dependency
    seed_statements = [
        ("USERS", seed.SEED_USERS),
        ("ADMINISTRATORS", seed.SEED_ADMINISTRATORS),
        ("LOCATIONS", seed.SEED_LOCATIONS),
        ("ITEMS", seed.SEED_ITEMS),
        ("CLAIMS", seed.SEED_CLAIMS),
    ]

    for table_name, insert_stmt in seed_statements:
        cursor.execute(insert_stmt)
        print(f"Populated table: {table_name}")

    print("Database successfully seeded.")


def run_queries(cursor):
    """Executes and formats all 8 retrieval queries from Queries.py."""
    print("\n" + "=" * 60)
    print("2. EXECUTING RETRIEVAL QUERIES")
    print("=" * 60)

    queries_list = [
        ("Query 1: Active Items Search (Medium)", Queries.QUERY_1_ACTIVE_ITEMS),
        ("Query 2: Location Summary (Medium)", Queries.QUERY_2_LOCATION_SUMMARY),
        (
            "Query 3: Users with Pending Claims (Medium)",
            Queries.QUERY_3_USERS_WITH_PENDING_CLAIMS,
        ),
        (
            "Query 4: Recent Valuables Filter (Medium)",
            Queries.QUERY_4_RECENT_VALUABLES,
        ),
        (
            "Query 5: Full Claim Audit Log (Complex)",
            Queries.QUERY_5_FULL_CLAIM_AUDIT,
        ),
        (
            "Query 6: Contested Locations (Complex)",
            Queries.QUERY_6_CONTESTED_LOCATIONS,
        ),
        (
            "Query 7: Admin Performance Analysis (Complex)",
            Queries.QUERY_7_ADMIN_PERFORMANCE,
        ),
        (
            "Query 8: High Activity Users (Complex)",
            Queries.QUERY_8_HIGH_ACTIVITY_USERS,
        ),
    ]

    for title, query_sql in queries_list:
        print(f"\n--- {title} ---")
        cursor.execute(query_sql)
        results = cursor.fetchall()

        if not results:
            print("No records found.")
        else:
            for row in results:
                print(row)


def main():
    """Main execution flow."""
    conn = get_connection()
    if conn is None:
        print("Failed to establish database connection. Exiting.")
        return

    try:
        # PyMySQL connection provides dictionary cursors directly via context manager
        # (cursorclass is already configured inside DB_CONFIG in DB.py)
        with conn.cursor() as cursor:
            run_seeding(cursor) # run once
            conn.commit()

            run_queries(cursor)

    except Exception as e:
        print(f" An error occurred during database operations: {e}")
        conn.rollback()

    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed cleanly.")


if __name__ == "__main__":
    main()