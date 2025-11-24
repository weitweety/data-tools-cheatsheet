import pandas as pd
import logging
from datetime import datetime

def cast_data(df: pd.DataFrame) -> pd.DataFrame:
    cast_types = {
        "name": str,
        "age": int,
        "city": str,
        "salary": int,
        "department": str
    }

    df = df.astype(cast_types)

    # Convert datetime column separately using pd.to_datetime
    if "join_date" in df.columns:
        df["join_date"] = pd.to_datetime(df["join_date"])
    return df


def fill_data(df: pd.DataFrame) -> pd.DataFrame:
    # Dataframe.fillna is suitable for filling NA values with default values
    default_values = {
        "age": 0,
        "city": "None",
        "department": "None",
        "join_date": pd.to_datetime("1970-01-01")
    }

    df = df.fillna(value=default_values)
    return df