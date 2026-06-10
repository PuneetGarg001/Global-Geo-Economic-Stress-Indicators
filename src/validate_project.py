from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"

MAIN_COLUMNS = [
    "country_code",
    "country_name",
    "iso3",
    "region",
    "income_group",
    "year",
    "gdp_growth",
    "inflation",
    "unemployment",
    "gdp_per_capita",
    "population",
    "food_production_index",
    "cereal_yield",
    "cereal_production_tonnes",
    "agricultural_land_pct",
    "dietary_energy_supply_adequacy",
    "economic_stress_score",
    "data_completeness_score",
]

SCORE_COMPONENTS = [
    "inflation_score",
    "unemployment_score",
    "gdp_growth_score",
    "income_vulnerability_score",
    "food_pressure_score",
]


def pct(series: pd.Series) -> float:
    return round(float(series.mean() * 100), 2)


def validate() -> dict:
    metadata = pd.read_csv(DATA_DIR / "country_metadata.csv")
    main = pd.read_csv(DATA_DIR / "country_year_indicators.csv")
    score = pd.read_csv(DATA_DIR / "economic_stress_score.csv")
    dictionary = pd.read_csv(DATA_DIR / "indicator_dictionary.csv")

    errors: list[str] = []
    warnings: list[str] = []

    if list(main.columns) != MAIN_COLUMNS:
        errors.append("country_year_indicators.csv does not match the expected schema.")

    duplicate_keys = int(main.duplicated(["country_code", "year"]).sum())
    if duplicate_keys:
        errors.append(f"Found {duplicate_keys} duplicate country-year rows.")

    if not main["year"].between(1960, 2025).all():
        errors.append("Some rows fall outside the expected 1960-2025 year range.")

    merged_scores = main[["country_code", "year", "economic_stress_score"]].merge(
        score[["country_code", "year", "final_economic_stress_score"]],
        on=["country_code", "year"],
        how="inner",
    )
    score_delta = (
        merged_scores["economic_stress_score"]
        - merged_scores["final_economic_stress_score"]
    ).abs()
    if score_delta.dropna().max() != 0:
        errors.append("Final score differs between main and score files.")

    score["component_count"] = score[SCORE_COMPONENTS].notna().sum(axis=1)
    scored = score[score["final_economic_stress_score"].notna()].copy()
    low_evidence_scored = int((scored["component_count"] <= 2).sum())
    severe_low_evidence = int(
        ((scored["stress_category"] == "Severe") & (scored["component_count"] <= 2)).sum()
    )

    if low_evidence_scored:
        warnings.append(
            f"{low_evidence_scored} scored rows use only one or two score components."
        )
    if severe_low_evidence:
        warnings.append(
            f"{severe_low_evidence} Severe rows use only one or two score components."
        )

    recent_2025_completeness = float(
        main.loc[main["year"] == 2025, "data_completeness_score"].mean()
    )
    if recent_2025_completeness < 50:
        warnings.append(
            "2025 has low average completeness; avoid making strong current-year claims."
        )

    return {
        "status": "passed" if not errors else "failed",
        "errors": errors,
        "warnings": warnings,
        "row_count": int(len(main)),
        "country_count": int(main["country_code"].nunique()),
        "year_count": int(main["year"].nunique()),
        "min_year": int(main["year"].min()),
        "max_year": int(main["year"].max()),
        "duplicate_country_year_rows": duplicate_keys,
        "metadata_rows": int(len(metadata)),
        "dictionary_rows": int(len(dictionary)),
        "scored_rows": int(scored.shape[0]),
        "unscored_rows": int(score["final_economic_stress_score"].isna().sum()),
        "low_evidence_scored_rows": low_evidence_scored,
        "severe_low_evidence_rows": severe_low_evidence,
        "average_completeness": round(float(main["data_completeness_score"].mean()), 2),
        "average_2025_completeness": round(recent_2025_completeness, 2),
        "missing_percent": {
            column: pct(main[column].isna()) for column in main.columns
        },
        "stress_category_counts": {
            str(k): int(v) for k, v in score["stress_category"].value_counts(dropna=False).items()
        },
    }


def write_markdown_report(summary: dict) -> None:
    REPORTS_DIR.mkdir(exist_ok=True)
    lines = [
        "# Data Quality Summary",
        "",
        f"Status: **{summary['status']}**",
        "",
        "## Dataset Size",
        "",
        f"- Rows: {summary['row_count']:,}",
        f"- Countries: {summary['country_count']}",
        f"- Years: {summary['min_year']}-{summary['max_year']}",
        f"- Scored rows: {summary['scored_rows']:,}",
        f"- Unscored rows: {summary['unscored_rows']:,}",
        "",
        "## Key Warnings",
        "",
    ]
    if summary["warnings"]:
        lines.extend(f"- {warning}" for warning in summary["warnings"])
    else:
        lines.append("- No warnings found.")

    lines.extend(
        [
            "",
            "## Missingness",
            "",
            "| Column | Missing % |",
            "| --- | ---: |",
        ]
    )
    for column, missing_pct in summary["missing_percent"].items():
        lines.append(f"| {column} | {missing_pct:.2f} |")

    lines.extend(
        [
            "",
            "## Stress Category Counts",
            "",
            "| Category | Rows |",
            "| --- | ---: |",
        ]
    )
    for category, count in summary["stress_category_counts"].items():
        lines.append(f"| {category} | {count:,} |")

    (REPORTS_DIR / "data_quality_summary.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main() -> None:
    summary = validate()
    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / "validation_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    write_markdown_report(summary)
    print(json.dumps(summary, indent=2))
    if summary["errors"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
