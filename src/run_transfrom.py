import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Get your DB URL from .env
db_url = os.getenv("DB_URL")

# Path to your SQL file
SQL_FILE = "sql/02_transfrom.sql"

def run_transform():
    # Connect to the database
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    # Read the SQL file
    with open(SQL_FILE, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.execute(sql_script)

    # Commit the changes
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_transform()
    print("Transformation completed successfully!")
    