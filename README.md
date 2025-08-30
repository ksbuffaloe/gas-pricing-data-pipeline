# Gas Pricing Data Pipeline

This project ingests weekly U.S. gas price data from the EIA Open Data API, stores it in a database, and can automatically update on a schedule. It’s designed to support both local development and cloud deployment with an updating dashboard.
---

## Tech stack

- Python (`requests`, `pandas`, `sqlalchemy`, `dotenv`)
- Databases
    - SQLite for local testing
    - PostgreSQL (e.g. Supabase) for cloud deployment
- Secrets Management – .env locally, GitHub Secrets in CI/CD
- Scheduler – GitHub Actions cron job
- EIA Open Data API

---
## 🚀 How to run it

### 1️. Clone this repo

```bash
git clone https://github.com/ksbuffaloe/gas-pricing-data-pipeline.git
cd gas-pricing-data-pipeline
```

###  2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure environment variables and register for API key

- 1. Get a free API key from the [EIA API Registration Page](https://www.eia.gov/opendata/register.php).
- 2. Store this API key in your local .env and github secrets as `API_key`

```bash
# For local testing
DB_URL   = sqlite:///data/gas_prices.db

# For cloud deployment (comment out local, uncomment this when deploying, insert the link to whatever postgres cloud DB you choose )
# DB_URL = postgresql+psycopg2://user:password@host:5432/dbname

API_KEY  = your_api_key
API_URL  = "https://api.eia.gov/v2/petroleum/pri/gnd/data/"

```

### 5. Run the Database Schema Scripts

Important Note

Before running the pipeline, you must configure the correct database. Update the .env file by commenting/uncommenting the appropriate DB_URL for either SQLite or Cloud Postgres. Make sure this is set correctly before each run.

``` bash
python src/setup_db.py
```

### 6. Run the pipeline

``` bash
python src/main.py
```

## ☁️ How to Deploy to the Cloud

1. Provision a PostgreSQL database (e.g. Supabase or Render).

2. Store the connection string in your GitHub repo as a Secret named DB_URL.

3. Store your API_KEY and API_URL as Secrets as well.

4. GitHub Actions workflow (.github/workflows/run_pipeline.yml) runs your pipeline automatically every Tuesday at 7 AM MST.


## 📊 Next Steps

Add a dashboard (e.g. Streamlit or Dash) that reads from the cloud database.

- Deploy the dashboard to Streamlit Cloud, Render, or similar.
- Automate further transforms and visualizations.


```mermaid
flowchart TD
    A[User] --> B[Python Script: requests + pandas]
    B --> C[Process Data]
    C --> D[Store in Database]
    D --> E[GitHub Actions Workflow]
    E --> F[Dashboard / Report]
```

