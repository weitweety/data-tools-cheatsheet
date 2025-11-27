import pandas as pd
import logging
from datetime import datetime

def avg_salary_groupby_department(df: pd.DataFrame):
    # pandas provides really flexible aggregation definitions.
    # The aggregation contents are highly-relative to df contents.
    # To categorize sample usages into this file, we need
    # to make certain assumptions on the input DataFrame.

    # Required: columns ['department'(str), 'salary'(numeric)]
    '''
    df_filtered = df[["department", "salary"]]
    df_agg = df_filtered.groupby('department').mean()
    '''

    # .agg() is also quite handy -- just define the corresponding function
    # to be applied on the aggregated columns
    df_agg = df.groupby("department").agg({"salary": "mean"})
    return df_agg

def min_max_salary_groupby_department(df: pd.DataFrame):
    # .agg() is also quite handy -- just define the corresponding function
    # to be applied on the aggregated columns
    '''
    df_agg = df.groupby("department").agg({"salary": ["min", "max"]})
    '''

    # .agg() accept also *args and **kwargs, especially useful to define the
    # output column names
    df_agg = df.groupby("department").agg(
        min_salary=("salary", "min"),
        max_salary=("salary", "max")
    )
    return df_agg
