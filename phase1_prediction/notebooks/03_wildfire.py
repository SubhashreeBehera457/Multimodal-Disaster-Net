"""
Phase 1 — Track 1B — Wildfire Risk Prediction (Uttarakhand)
Author: Subhashree Behera
"""
import requests
import pandas as pd

# Uttarakhand approx center: 30.0668°N, 79.0193°E
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 30.0668,
    "longitude": 79.0193,
    "start_date": "2018-01-01",
    "end_date": "2023-12-31",
    "daily": "temperature_2m_max,relative_humidity_2m_mean,wind_speed_10m_max",
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)
weather = pd.DataFrame(response.json()["daily"])
weather.to_csv("../data/uttarakhand_weather.csv", index=False)

print(f"Shape      : {weather.shape}")
print(f"Date range : {weather['time'].min()} to {weather['time'].max()}")
print(weather.head())