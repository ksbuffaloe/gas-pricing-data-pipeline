import requests
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
url = os.getenv("API_URL")
db_url = os.getenv("DB_URL")

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

    engine = create_engine(db_url)

    # Ensure the 'inserted_at' column is not present in the DataFrame to get a new timestamp
    if 'inserted_at' in df.columns:
        df = df.drop(columns=['inserted_at'])

    with engine.connect() as conn:
        # ✅ Only delete if we have good data
        conn.execute(text("DELETE FROM raw_prices;"))
        df.to_sql('raw_prices', conn, if_exists='append', index=False, method='multi')

    print(f"Inserted {len(df)} rows into raw_prices!")


if __name__ == "__main__":
    run_ingest()
