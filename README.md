# COVID-19 Vaccine Efficacy Trends — EDA

Exploratory data analysis of global COVID-19 vaccination data to uncover trends, disparities, and socioeconomic correlates across countries and age groups.

## Dataset

Source: [Our World in Data — COVID-19 Vaccinations](https://github.com/owid/covid-19-data)

- `https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv`
- `https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv`
- `https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-age-group.csv`
- `https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv` (for socioeconomic metadata)

## How to Run

```bash
pip install -r requirements.txt
python data/fetch_data.py
```

Then open and run the notebooks in order:

1. `notebooks/01_data_overview.ipynb` — data shape, nulls, top countries
2. `notebooks/02_time_series.ipynb` — vaccination trends over time
3. `notebooks/03_country_analysis.ipynb` — cross-country comparisons, GDP scatter
4. `notebooks/04_age_group_analysis.ipynb` — vaccination rates by age group
5. `notebooks/05_dose_gap_impact.ipynb` — booster uptake analysis
6. `notebooks/06_correlation_heatmap.ipynb` — socioeconomic correlations
7. `notebooks/07_pca_clustering.ipynb` — PCA + K-Means country clustering

## Key Findings

- Countries with higher HDI, GDP per capita, and median age consistently show higher vaccination coverage — life expectancy and vaccination rates correlate at r=0.63.
- Younger age groups (0-4, 5-9) have near-zero vaccination rates globally while 65+ groups cluster above 80%, revealing a stark age-based gap.
- Countries with high booster uptake also tend to have higher base vaccination rates (r=0.66, p<0.001), and the gap between high and low booster groups is ~20 percentage points.
- K-Means clustering (k=3) separates countries into distinct groups — high-income/high-coverage, middle-tier, and low-income/low-coverage — with clear separation in PCA space (73% variance explained by 2 components).
