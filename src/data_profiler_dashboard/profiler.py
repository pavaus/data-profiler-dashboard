import pandas as pd


def get_dataset_summary(dataframe: pd.DataFrame) -> dict[str, int]:
    """
    Return high-level dataset metrics.
    """
    return {
        "row_count": len(dataframe),
        "column_count": len(dataframe.columns),
        "duplicate_row_count": int(dataframe.duplicated().sum()),
    }


def get_column_profile(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Return column-level profile metrics.
    """
    row_count = len(dataframe)

    profile = pd.DataFrame(
        {
            "column_name": dataframe.columns,
            "data_type": [str(dtype) for dtype in dataframe.dtypes],
            "non_null_count": dataframe.notna().sum().values,
            "null_count": dataframe.isna().sum().values,
            "unique_count": dataframe.nunique(dropna=True).values,
        }
    )

    profile["null_percentage"] = (
        profile["null_count"] / row_count * 100 if row_count else 0
    )

    profile["unique_percentage"] = (
        profile["unique_count"] / row_count * 100 if row_count else 0
    )

    return profile