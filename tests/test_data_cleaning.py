import pandas as pd
import pytest
from data_cleaning import clean_dataframe


def test_cleaning_removes_exact_duplicates_and_fills_missing_values():
    raw = pd.DataFrame({
        " First Name ": ["Ava", "Ava", None],
        "Age": [20, 20, None],
        "score": [None, None, None],
    })
    cleaned, summary = clean_dataframe(raw)
    assert len(cleaned) == 2
    assert list(cleaned.columns) == ["first_name", "age", "score"]
    assert cleaned["first_name"].isna().sum() == 0
    assert cleaned["age"].isna().sum() == 0
    assert cleaned["score"].isna().sum() == 2
    assert summary["duplicate_rows_before"] == 1


def test_cleaning_rejects_column_name_collisions():
    raw = pd.DataFrame({"First Name": ["A"], "first_name": ["B"]})
    with pytest.raises(ValueError, match="collide"):
        clean_dataframe(raw)
