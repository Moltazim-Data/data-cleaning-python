"""Clean the bundled sample CSV and report before/after quality checks.

Run from the repository root: python data_cleaning.py
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
INPUT_FILE = DATA_DIR / "customer_data.csv"
OUTPUT_FILE = DATA_DIR / "customer_data_cleaned.csv"
REPORT_FILE = DATA_DIR / "cleaning_summary.json"


def clean_dataframe(source: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    df = source.copy()
    before_rows = len(df)
    before_missing = int(df.isna().sum().sum())
    before_duplicates = int(df.duplicated().sum())

    # Normalize column names consistently and reject collisions rather than
    # silently producing duplicate names (e.g. "First Name" and "first_name").
    df.columns = (
        pd.Index(df.columns.astype(str))
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )
    if not df.columns.is_unique:
        duplicates = df.columns[df.columns.duplicated()].tolist()
        raise ValueError(f"Column names collide after normalization: {duplicates}")

    df = df.drop_duplicates().copy()
    numeric_cols = df.select_dtypes(include="number").columns
    other_cols = df.columns.difference(numeric_cols)

    for col in numeric_cols:
        median_value = df[col].median()
        if pd.notna(median_value):
            df[col] = df[col].fillna(median_value)

    for col in other_cols:
        modes = df[col].mode(dropna=True)
        if not modes.empty:
            df[col] = df[col].fillna(modes.iloc[0])

    summary = {
        "rows_before": int(before_rows),
        "rows_after": int(len(df)),
        "duplicate_rows_before": int(before_duplicates),
        "missing_cells_before": before_missing,
        "missing_cells_after": int(df.isna().sum().sum()),
        "columns": list(df.columns),
        "note": "Median/mode imputation is a demonstration baseline; review field semantics before real-world use."
    }
    return df, summary


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}. Run this script from the repository checkout."
        )
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    source = pd.read_csv(INPUT_FILE)
    cleaned, summary = clean_dataframe(source)
    cleaned.to_csv(OUTPUT_FILE, index=False)
    REPORT_FILE.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(f"Cleaned data saved to: {OUTPUT_FILE}")
    print(f"Cleaning summary saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
