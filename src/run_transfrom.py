import sqlite3
from dotenv import load_dotenv
import os

# Get the current file's directory (src/)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Move up one level to project root (i.e., gas-pricing-data-pipeline/)
project_root = os.path.dirname(base_dir)

# Load .env from root
load_dotenv(os.path.join(project_root, ".env"))

# Use environment variable or fallback to default SQLite DB path
sqlite_path = os.getenv("SQLITE_DB_PATH", os.path.join(project_root, "data", "gas_prices.db"))

# Path to the SQL file
SQL_FILE = os.path.join(project_root, "sql", "02_transfrom.sql")

def run_transform():
    if not os.path.exists(SQL_FILE):
        print(f"SQL file not found at {SQL_FILE}")
        return

    try:
        with sqlite3.connect(sqlite_path) as conn:
            cursor = conn.cursor()
            with open(SQL_FILE, 'r') as file:
                sql_script = file.read()
                cursor.executescript(sql_script)  # executescript for multiple statements
            print("Transformation SQL script executed successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")

if __name__ == "__main__":
    run_transform()
    print("Transformation completed successfully!")
