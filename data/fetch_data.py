import pandas as pd
import pickle
import os

# grab vaccination data + location metadata straight from GitHub
vacc_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"
loc_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv"

print("Fetching vaccinations.csv...")
df_vacc = pd.read_csv(vacc_url)

print("Fetching locations.csv...")
df_loc = pd.read_csv(loc_url)

# merge on location
df = df_vacc.merge(df_loc, on="location", how="left")

# drop rows missing the key metric
df = df.dropna(subset=["people_fully_vaccinated_per_hundred"])

# these aren't real countries — aggregates and income buckets OWID adds
non_countries = [
    "World", "Africa", "Asia", "Europe", "European Union",
    "North America", "Oceania", "South America",
    "High income", "Upper middle income",
    "Lower middle income", "Low income",
]
df = df[~df["location"].isin(non_countries)]

# save to pickle in the same data/ folder
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "processed.pkl")

with open(out_path, "wb") as f:
    pickle.dump(df, f)

print(f"Done — saved {len(df)} rows to {out_path}")
