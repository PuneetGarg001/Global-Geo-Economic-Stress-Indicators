# Global Geo-Economic Stress Indicators

A data analytics project that builds and explores a country-year panel of geo-economic stress indicators across 217 countries from 1960 to 2025.

The project combines macroeconomic indicators and food-system signals from open data sources into an analytical stress-score dataset. It includes the original analysis notebook, processed datasets, metadata, and reproducible validation checks.

## Overview

This repository is organized around one main notebook:

`notebooks/Global Geo-Economic Stress Indicators.ipynb`

The notebook covers:

- data loading and merging
- missing-value analysis
- country-level and regional exploratory analysis
- economic stress trend visualization
- K-Means country segmentation
- Random Forest based feature-importance analysis
- model evaluation using MAE, R2, and regional performance checks
- correlation analysis between selected indicators and stress scores

## Dataset

The processed dataset contains:

- 14,322 country-year observations
- 217 countries and economies
- 66 years of coverage, from 1960 to 2025
- country metadata including region, income group, latitude, and longitude
- macroeconomic indicators including GDP growth, inflation, unemployment, GDP per capita, and population
- food-system indicators including food production, cereal yield, cereal production, agricultural land share, and dietary energy supply adequacy
- derived economic stress scores and stress categories

## Repository Structure

```text
.
|-- data/
|   |-- README.md
|   `-- processed/
|       |-- country_metadata.csv
|       |-- country_year_indicators.csv
|       |-- economic_stress_score.csv
|       |-- indicator_dictionary.csv
|       `-- validation_report.json
|-- notebooks/
|   `-- Global Geo-Economic Stress Indicators.ipynb
|-- reports/
|   |-- data_quality_summary.md
|   `-- validation_summary.json
|-- src/
|   `-- validate_project.py
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Data Files

| File | Description |
| --- | --- |
| `country_metadata.csv` | Country metadata, region, income group, latitude, and longitude |
| `country_year_indicators.csv` | Main country-year panel with indicators and final stress score |
| `economic_stress_score.csv` | Component scores and stress categories |
| `indicator_dictionary.csv` | Data dictionary with source, unit, and interpretation notes |
| `validation_report.json` | Exported validation summary |

## Methodology

The economic stress score is a derived analytical index based on available macroeconomic and food-system components:

- inflation pressure
- unemployment pressure
- GDP growth weakness
- income vulnerability
- food pressure

Higher values indicate higher estimated stress. The score is an analytical project output and should not be interpreted as an official index.

## Validation

Run the validation script:

```bash
pip install -r requirements.txt
python src/validate_project.py
```

The validation checks:

- expected schema
- duplicate country-year rows
- year range
- score consistency across files
- missing-value percentages
- low-evidence score warnings based on available score components

## Current Validation Snapshot

- Validation status: passed
- Duplicate country-year rows: 0
- Scored rows: 12,762
- Unscored rows: 1,560
- Average data completeness: 66.76%
- Average 2025 completeness: 20.97%

## Limitations

Some years and countries have incomplete source data. Scores based on fewer available components should be interpreted carefully. The 2025 data is especially incomplete and should be treated as provisional.

The machine-learning section in the notebook is best interpreted as feature-importance and score-explanation analysis. For future forecasting, the project should use lagged features and time-based validation.

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy

## Future Improvements

- Add confidence labels based on component availability
- Refactor the notebook into a cleaner final-report version
- Add time-based validation for forecasting experiments
- Add dashboard-ready visualizations
- Automate data collection from source APIs
