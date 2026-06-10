# Data

This folder contains processed outputs for the Global Geo-Economic Stress Indicators project.

## Files

- `country_metadata.csv`: country-level metadata including region, income group, and map coordinates.
- `country_year_indicators.csv`: country-year panel from 1960 to 2025 with macroeconomic and food-system indicators.
- `economic_stress_score.csv`: component scores and final stress category for each country-year row.
- `indicator_dictionary.csv`: source, unit, interpretation, and missing-value notes for each field.
- `validation_report.json`: structural validation summary exported from the notebook workflow.

## Source Attribution

The dictionary identifies World Bank and FAOSTAT-derived indicators. When publishing, cite these sources clearly in the README and project report. The derived score is analytical and should not be presented as an official index.

## Known Caveat

Rows with low component availability can still receive a final score because the score is computed from available components. Use `data_completeness_score` and component counts when interpreting country-year results.
