# LinkedIn Post Draft

Today I worked on a final-year data analytics project: **Global Geo-Economic Stress Indicators**.

The goal is to build a country-year dataset that combines macroeconomic indicators and food-system pressure signals into an interpretable stress score across 217 countries from 1960 to 2025.

What I focused on:

- collecting and structuring country-level and country-year indicators
- creating an economic stress score from inflation, unemployment, GDP growth, income vulnerability, and food pressure components
- adding an indicator dictionary with sources, units, and interpretation notes
- validating the dataset for schema consistency, duplicates, coverage, and missingness

One important learning: a model or index is not only about producing a final score. It also needs transparency. I found that some rows can receive a score even when only a few components are available, so I am adding data-completeness checks and confidence labels before treating the result as decision-ready.

This project helped me practice data cleaning, feature engineering, validation, documentation, and responsible interpretation of analytical scores.

Tech stack: Python, Pandas, data validation, World Bank indicators, FAOSTAT indicators, GitHub.

#DataAnalytics #Python #Pandas #FinalYearProject #DataScience #OpenData #GitHub
