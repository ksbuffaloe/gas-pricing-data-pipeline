import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Use environment variable or fallback to default path
sqlite_path = os.getenv("SQLITE_DB_PATH", "data/gas_prices.db")

# Get the absolute path to the project root (one level up from src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create path to the SQL file inside the sql/ folder
sql_file_path = os.path.join(BASE_DIR, "sql", "01_setup_schema.sql")

def run_sql_script():
    if not os.path.exists(sql_file_path):
        print(f"SQL file not found at {sql_file_path}")
        return

    try:
        with sqlite3.connect(sqlite_path) as conn:
            cursor = conn.cursor()
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
                cursor.executescript(sql_script)
                print("SQL schema applied successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")

if __name__ == "__main__":
    run_sql_script()
