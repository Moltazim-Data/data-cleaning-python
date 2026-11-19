# Data Cleaning with Python

A reproducible pandas workflow for preparing tabular data: inspect a CSV, remove exact duplicates, normalize column names, handle missing values and export a cleaned dataset with a quality summary.

## Workflow

1. Read the source CSV and inspect its shape and columns.
2. Remove exact duplicate rows.
3. Normalize column names and detect collisions.
4. Fill numeric missing values with medians and other columns with modes.
5. Export the cleaned file and a JSON quality summary.

## Files

- `data/customer_data.csv` — sample input (legacy filename; the fields describe restaurant bills/tips, not CRM customers).
- `data_cleaning.py` — reusable script.
- `notebooks/data_cleaning.ipynb` — walkthrough.
- `tests/test_data_cleaning.py` — behavior tests.
- `data/customer_data_cleaned.csv`, `data/cleaning_summary.json` — generated outputs.

## Run

Python 3.10+ recommended.

```bash
python -m pip install pandas pytest
python data_cleaning.py
python -m pytest -q
```

Paths are resolved relative to the script, so it can be run from another working directory.

## Notes

These are demonstration cleaning rules, not one-size-fits-all defaults. Review outliers, field meaning and downstream impact before imputing real data. All-null columns remain null. Check the sample dataset's provenance and license before redistribution.
