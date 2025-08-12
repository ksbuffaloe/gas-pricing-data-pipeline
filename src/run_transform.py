from dotenv import load_dotenv
import os
from setup_db import get_db_type, run_sql_script

# Load .env from root
load_dotenv()

# Load DB URL from .env
DB_URL = os.getenv("DB_URL", "sqlite:///data/gas_prices.db")

# Determine database type
db_type = get_db_type()

#Run the SQL script for data transformation
def run_transform():
    script_name = "02_transform.sql"
    run_sql_script(script_name)
    print(f"Transformation script '{script_name}' executed for {db_type} database.")


if __name__ == "__main__":
    # Run the transformation SQL script
    run_transform()

