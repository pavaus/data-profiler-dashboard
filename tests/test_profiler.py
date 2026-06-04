import pandas as pd

from data_profiler_dashboard.profiler import (
    get_column_profile,
    get_dataset_summary,
)


def test_get_dataset_summary():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Bob"],
            "age": [25, 30, 30],
        }
    )

    summary = get_dataset_summary(df)

    assert summary["row_count"] == 3
    assert summary["column_count"] == 2
    assert summary["duplicate_row_count"] == 1


def test_get_column_profile():
    df = pd.DataFrame(
        {
            "name": ["Alice", "Bob", None],
            "age": [25, 30, 30],
        }
    )

    profile = get_column_profile(df)

    assert len(profile) == 2