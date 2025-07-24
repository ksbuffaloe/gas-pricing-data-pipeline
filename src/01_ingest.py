import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# Load API key and URL from environment variables
API_KEY = os.getenv("API_KEY")
url = os.getenv("API_URL")

# Define parameters for the API request
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

# Make the GET request
response = requests.get(url, params=params)

# Parse JSON
data = response.json()

print(data)

# EIA v2 returns data in ['response']['data']
results = data['response']['data']