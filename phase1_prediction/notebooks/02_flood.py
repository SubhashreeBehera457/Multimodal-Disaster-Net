"""
Phase 1 — Track 1B — Flood Risk Prediction (Odisha)
Author: Subhashree Behera
"""
import requests
import pandas as pd

# Odisha coastal region — Puri district (flood-prone)
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 19.8135,
    "longitude": 85.8312,
    "start_date": "2018-01-01",
    "end_date": "2023-12-31",
    "daily": "precipitation_sum,rain_sum",
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)
rainfall = pd.DataFrame(response.json()["daily"])

print(f"Shape      : {rainfall.shape}")
print(f"Date range : {rainfall['time'].min()} to {rainfall['time'].max()}")
print(rainfall.head())

rainfall.to_csv("../data/rainfall_odisha.csv", index=False)
print("Saved: rainfall_odisha.csv")