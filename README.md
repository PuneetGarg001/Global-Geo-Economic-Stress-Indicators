# Global Geo-Economic Stress Indicators

An analytical country-year dataset for studying economic and food-system stress across 217 countries from 1960 to 2025.

The project combines World Bank and FAOSTAT-derived indicators into a documented stress-score dataset with metadata, an indicator dictionary, a source notebook, and validation checks. It is designed as a final-year data analytics project and portfolio-ready GitHub repository.

The main source notebook is `notebooks/Global Geo-Economic Stress Indicators.ipynb`.

## Project Highlights

- 14,322 country-year observations
- 217 countries and economies
- 1960-2025 panel coverage
- Economic stress scoring from inflation, unemployment, GDP growth, income vulnerability, and food pressure components
- EDA notebook with country trends, regional comparison, heatmaps, clustering, Random Forest feature importance, and regional model evaluation
- Data dictionary with source, unit, interpretation, and missing-value notes
- Validation script for schema checks, duplicate checks, score consistency, missingness, and evidence-level warnings

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
|-- docs/
|   |-- colab_note.md
|   |-- linkedin_post.md
|   |-- notebook_audit.md
|   `-- project_review.md
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
| `country_year_indicators.csv` | Main country-year panel with original indicators and final stress score |
| `economic_stress_score.csv` | Component scores and final stress category |
| `indicator_dictionary.csv` | Definitions, source codes, units, and interpretation notes |
| `validation_report.json` | Exported structural validation summary |

## Methodology

The stress score is a derived analytical index using available macroeconomic and food-system components:

- inflation pressure
- unemployment pressure
- GDP growth weakness
- income vulnerability
- food production or supply pressure

Higher scores indicate higher estimated stress. The score is not an official World Bank, FAOSTAT, or government index.

The notebook also trains a Random Forest model using stress-related features. In the current version, this should be described as an explainability or score-approximation model because the target score is derived from related components. To turn it into a true predictive model, use lagged features and a time-based validation split.

## Important Limitation

Some country-year rows have incomplete component data. In the current export, rows can still receive a final score when only one or two components are available. This is useful for exploratory coverage, but it should be interpreted with caution. The validation script flags these low-evidence scores.

For serious analysis, use `data_completeness_score` and component availability together with the final score.

## Run Validation

```bash
pip install -r requirements.txt
python src/validate_project.py
```

This writes:

- `reports/validation_summary.json`
- `reports/data_quality_summary.md`

## Current Quality Snapshot

- Validation status: passed
- Duplicate country-year rows: 0
- Scored rows: 12,762
- Rows with only one or two score components: 2,013
- Severe rows with only one or two score components: 283
- Average completeness: 66.76%
- Average 2025 completeness: 20.97%

## What I Learned

This project strengthened my skills in data cleaning, open-data integration, feature engineering, analytical index design, exploratory modeling, validation, and communicating uncertainty. A major lesson was that a strong data project should explain both the score and the confidence behind the score.

## Next Improvements

- Add confidence labels based on component availability
- Refactor the notebook into clearer sections: data loading, cleaning, EDA, scoring, modeling, evaluation
- Change the ML section into either score explainability or true forecasting
- Add visualizations for trends, regions, and missingness
- Add a reproducible data-ingestion pipeline from World Bank and FAOSTAT APIs
- Add tests for scoring thresholds and category assignment
