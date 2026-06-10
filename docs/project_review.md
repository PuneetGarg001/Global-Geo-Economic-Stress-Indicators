# Project Review

## What Is Right

- The project has a useful and resume-worthy theme: combining macroeconomic pressure and food-system indicators into a country-year stress dataset.
- The exported data has a clean panel shape: 217 countries, 66 years, 14,322 rows, and no duplicate country-year keys.
- The dataset includes a proper indicator dictionary, which is a strong signal of data maturity.
- Keeping both raw component scores and final categories is good analytical practice because reviewers can inspect how the final result was formed.
- The validation report already confirms core structural checks.
- The source notebook includes EDA, clustering, feature importance, model tuning, model persistence, and regional evaluation, which gives the project a complete analysis story.

## Where It Needs Improvement

- The final score can be calculated when only one or two components are present. This creates overconfident results, especially for early years and 2025.
- Current-year interpretation is weak. In the exported data, 2025 average completeness is low, so it should be presented as preliminary.
- Missingness is high for some important indicators, especially unemployment and dietary energy supply adequacy.
- The methodology needs a clear explanation of normalization, weights, category thresholds, and why those choices are reasonable.
- The notebook's machine-learning section currently predicts a derived score from features used to create that score. This is useful for explainability, but it should not be described as an independent predictive model unless lagged/future prediction is added.
- The notebook uses backward filling for missing values, which can leak future information into earlier years.

## Suggested Fixes Before Final Submission

1. Add a confidence label based on component count, for example `Low evidence`, `Moderate evidence`, and `High evidence`.
2. Suppress or flag final scores when fewer than three components are available.
3. Treat 2025 as provisional unless the source data is complete enough.
4. Add a methodology section with formulas, weights, thresholds, and source citations.
5. Add charts for top stressed countries, regional averages, missingness by year, and score distribution.
6. Change the ML framing to "explainability model" or rebuild it as a true forecasting model with lagged features and time-based validation.

## Resume Framing

Built a 14K-row country-year geo-economic stress dataset covering 217 countries from 1960-2025, combining World Bank and FAOSTAT indicators into a documented analytical stress index with validation checks, data dictionary, and reproducible quality reporting.
