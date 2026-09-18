"""
Phase 1 — Track 1B — Cyclone Risk Prediction (Odisha coast)
"""
import pandas as pd

# skiprows=[1]: IBTrACS has a UNITS row right after headers
df = pd.read_csv(r"C:\Users\Subhashree Behera\Desktop\Multimodal-Disaster-Net\phase1_prediction\data\ibtracs.NI.list.v04r01.csv", skiprows=[1], low_memory=False)
df['LAT'] = pd.to_numeric(df['LAT'], errors='coerce')
df['LON'] = pd.to_numeric(df['LON'], errors='coerce')

print(f"Total storms   : {df['SID'].nunique()}")
print(f"Date range     : {df['ISO_TIME'].min()} to {df['ISO_TIME'].max()}")

# Odisha coast bounding box
odisha = df[
    (df['LAT'].between(17.0, 22.0)) &
    (df['LON'].between(84.0, 88.0))
].copy()

n_storms = odisha['SID'].nunique()
print(f"Odisha storms  : {n_storms}")
if n_storms < 20:
    print(f"Small sample ({n_storms}) — note this honestly in results")

odisha.to_csv("../data/cyclone_odisha_filtered.csv", index=False)
print("Saved: cyclone_odisha_filtered.csv")