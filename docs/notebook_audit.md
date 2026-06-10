# Notebook Audit

This audit is based on `notebooks/Global Geo-Economic Stress Indicators.ipynb`.

## What Your Notebook Does Well

- Loads all four project datasets and previews them.
- Creates a combined working dataset for analysis.
- Checks missing values before modeling.
- Includes useful EDA visuals: country trends, regional averages, heatmaps, and correlation plots.
- Attempts segmentation with K-Means clustering.
- Uses Random Forest feature importance to explain drivers of the stress score.
- Adds model tuning, saved model output, sample prediction, MAE, R2, and region-level evaluation.

## Main Issues To Fix

### 1. Merge Keys Are Too Broad

The notebook merges `country_year_indicators.csv` and `economic_stress_score.csv` on `country_code`, `country_name`, `year`, and `region`. This works only if names and region labels match perfectly. For a cleaner final project, merge country-year data on `country_code` and `year`, then keep metadata from one trusted source.

### 2. Column Suffixes Make The Dataset Messy

After merging, columns such as `region_x`, `region_y`, `income_group_x`, and `income_group_y` appear. The analysis uses `region_x`, which works, but it looks accidental. Rename columns after merging so the notebook reads professionally.

### 3. Missing-Value Filling Uses Future Information

The notebook uses `ffill().bfill()` within each country. The backward fill uses future values to fill past years, which is risky for time-series analysis and model evaluation. Prefer forward fill only, interpolation with clear limits, or model-specific imputation inside a pipeline.

### 4. The Model Has Target Leakage

The Random Forest predicts `economic_stress_score` using raw and derived stress components. Because the target score is derived from related components, the model is mostly learning your scoring formula, not discovering an independent real-world relationship.

Better framing:

- Use the model as a score approximation or explainability model.
- Or predict a future score using lagged features, such as previous-year inflation, unemployment, GDP growth, and food pressure.

### 5. Random Train-Test Split Is Weak For Panel Data

The notebook uses a random split across country-year rows. This can mix the same country and nearby years into both train and test sets. For a stronger project, use a time-based split, group split by country, or walk-forward validation.

### 6. 2025 Clustering Is Not Reliable

The clustering uses the latest year, which is 2025. The exported validation shows 2025 has low average completeness. Clustering on that year may reflect imputation more than real observations. Use 2022 or 2023, or choose the latest year with acceptable completeness.

### 7. Correlation P-Values Are Overconfident

Pearson correlation is calculated on country-year panel rows. Because repeated years within countries are not independent, p-values can look stronger than they really are. Keep the correlation plots, but describe them as exploratory.

## Best Next Version

1. Keep the current notebook as `v1_exploration`.
2. Add a cleaned `v2_methodology` notebook or script.
3. Add `component_count` and `evidence_level`.
4. Recompute or flag final scores when fewer than three components are available.
5. Reframe ML as either explainability or forecasting.
6. Add a short methodology section with the score formula, weights, thresholds, and limitations.

## Suggested Project Title

**Global Geo-Economic Stress Indicators: A Country-Year Analytical Index Using Macroeconomic and Food-System Signals**
