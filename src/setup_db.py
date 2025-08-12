import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import make_url
from dotenv import load_dotenv

load_dotenv()

# Load DB URL from .env
DB_URL = os.getenv("DB_URL", "sqlite:///data/gas_prices.db")

# Determine which SQL folder to use based on DB type
def get_db_type():
    url = make_url(DB_URL)
    if url.get_backend_name().startswith("sqlite"):
        return "sqlite"
    elif url.get_backend_name().startswith("postgresql"):
        return "postgres"
    else:
        raise ValueError(f"Unsupported database type: {url.get_backend_name()}")

def run_sql_script(script_name):
    db_type = get_db_type()
    script_path = os.path.join("sql", db_type, script_name)

    if not os.path.exists(script_path):
        raise FileNotFoundError(f"SQL file not found: {script_path}")

    engine = create_engine(DB_URL)
    with engine.begin() as conn:
        with open(script_path, "r") as file:
            sql_script = file.read()

            if db_type == "sqlite":
                raw_conn = conn.connection
                raw_conn.executescript(sql_script)
            else:
                statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]
                for stmt in statements:
                    conn.execute(text(stmt))

    print(f"Executed {script_name} for {db_type} database.")

if __name__ == "__main__":
    run_sql_script("01_setup_schema.sql")
