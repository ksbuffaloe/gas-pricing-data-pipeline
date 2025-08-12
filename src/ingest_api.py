import requests
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from setup_db import get_db_type, run_sql_script

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = os.getenv("API_URL")

# Load DB URL from .env
DB_URL = os.getenv("DB_URL", "sqlite:///data/gas_prices.db")

# Determine database type
db_type = get_db_type()


# Define the parameters for the API request given to us by the API documentation
params = {
    "api_key": API_KEY,
    "frequency": "weekly",
    "data[0]": "value",
    "facets[series][]": [
        "EMD_EPD2DXL0_PTE_R40_DPG",
        "EMD_EPD2D_PTE_R40_DPG",
        "EMM_EPM0R_PTE_R40_DPG",
        "EMM_EPM0U_PTE_R40_DPG",
        "EMM_EPM0_PTE_R40_DPG",
        "EMM_EPMMR_PTE_R40_DPG",
        "EMM_EPMMU_PTE_R40_DPG",
        "EMM_EPMM_PTE_R40_DPG",
        "EMM_EPMPR_PTE_R40_DPG",
        "EMM_EPMPU_PTE_R40_DPG",
        "EMM_EPMP_PTE_R40_DPG",
        "EMM_EPMRR_PTE_R40_DPG",
        "EMM_EPMRU_PTE_R40_DPG",
        "EMM_EPMR_PTE_R40_DPG"
    ],
    "start": "2021-01-01",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset": 0,
    "length": 5000
}

def run_ingest():
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()['response']['data']
    df = pd.DataFrame(data)
    print(f"Fetched {len(df)} rows from API.")
    if df.empty:
        print(" No data returned from API, keeping old data.")
        return  # Stop! Don’t clear old rows.

    df.rename(columns={
        'area-name': 'area_name',
        'product-name': 'product_name',
        'process-name': 'process_name',
        'series-description': 'series_description'
    }, inplace=True)

    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['period'] = pd.to_datetime(df['period'], format='%Y-%m-%d')

    # Sort by period and reset index
    df = df.sort_values(by='period').reset_index(drop=True)

    #Create a SQLAlchemy engine
    engine = create_engine(DB_URL)

    with engine.begin() as conn:
        conn.execute(text("DELETE FROM raw_prices;"))
        df.to_sql('raw_prices', conn, if_exists='append', index=False, method='multi')

    with engine.connect() as conn:
        count_after = conn.execute(text("SELECT COUNT(*) FROM raw_prices;")).scalar()
        print(f"Confirmed {count_after} rows now in raw_prices.")

if __name__ == "__main__":
    run_ingest()
