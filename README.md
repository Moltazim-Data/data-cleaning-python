# Data Cleaning with Python

A small data preparation project using Python and pandas. The workflow inspects a CSV, removes exact duplicate rows, normalizes column names, imputes numeric missing values with medians and non-numeric missing values with modes, and exports a cleaned file plus a quality summary.

## Files

- `data/customer_data.csv` — bundled sample input. **Despite the legacy filename, its columns describe restaurant bills/tips (for example `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, and `size`), not a customer CRM table.**
- `data_cleaning.py` — reproducible cleaning script.
- `notebooks/data_cleaning.ipynb` — step-by-step notebook.
- `tests/test_data_cleaning.py` — checks duplicate handling, missing-value behavior, and column-name collisions.
- `data/customer_data_cleaned.csv` and `data/cleaning_summary.json` — generated outputs.

## Run

Python 3.10+ recommended. From the repository root:

```bash
python -m pip install pandas pytest
python data_cleaning.py
python -m pytest -q
```

The script uses paths relative to its own file, so it can be launched from another working directory too.

## Cleaning rules and limitations

- Exact duplicate rows are removed; business-key duplicates require a domain-specific rule.
- Column names are trimmed, lowercased, and spaces are replaced with underscores. Normalization collisions raise an error.
- Numeric missing values use the median; other columns use the most frequent observed value.
- All-null columns remain null because there is no observed value to impute.
- These are demonstration defaults, not universal rules. Check outliers, field meaning, and downstream effects before using the method on real data.

The input is a sample dataset. Check its provenance and license before redistribution or commercial use.
