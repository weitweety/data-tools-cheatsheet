import pandas as pd
import logging

def dropnas(df: pd.DataFrame) -> pd.DataFrame:
    # In pandas, this directly maps to the Dataframe.dropna function.
    # This function demos different common parameter combinations and usecases for dropna.

    # drop all rows (indexes) with any column value being NA
    '''
    df = df.dropna(axis='index')
    '''

    # drop all rows (indexes) with ALL column values being NA
    '''
    df = df.dropna(axis='index', how='any')
    '''

    # drop all rows (indexes) when specific subset of columns including any NA
    df = df.dropna(axis='index', subset=['name', 'salary'])

    # same logic applies for columns
    '''
    df = df.dropna(axis='columns')
    '''
    return df


