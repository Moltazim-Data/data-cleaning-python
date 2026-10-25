# Data Cleaning with Python

A beginner-friendly data preparation project using Python and pandas. The workflow covers inspecting a raw customer dataset, identifying common quality issues, cleaning fields, and exporting a cleaned dataset.

## Workflow

- Inspect dataset shape, column names, types, and missing values.
- Identify duplicate rows.
- Standardize column names.
- Handle missing values using the rules implemented in the script.
- Export the cleaned data for downstream analysis.

## Project structure

```text
data-cleaning-python/
├── data/
│   ├── customer_data.csv
│   └── customer_data_cleaned.csv
├── data_cleaning.py
├── notebooks/
│   └── data_cleaning.ipynb
├── .gitignore
└── README.md
```

## Run

Use Python 3.10+ and install pandas if it is not already available:

```bash
python -m pip install pandas
python data_cleaning.py
```

Run the script from the repository root so relative paths to `data/` resolve correctly. Review the cleaning rules in `data_cleaning.py` before applying the workflow to a different dataset; missing-value treatment should be chosen based on field meaning, not applied blindly.

## Before using the output

- Compare row counts before and after cleaning.
- Confirm duplicate-removal and missing-value rules are appropriate.
- Check data types and key columns after export.
- Keep raw input separate from cleaned output so the transformation can be reviewed.

## Tools

Python, pandas, Jupyter Notebook, Git, and GitHub.

This project demonstrates data preparation fundamentals. Add a small validation test suite and a before/after quality summary to make the workflow stronger and easier to verify.
