import pandas as pd
import logging

def drop_problematic_data(df: pd.DataFrame) -> pd.DataFrame:
    ########################################################################################
    # We first drop NAs based on criteria.                                                 #
    # In pandas, this directly maps to the Dataframe.dropna function.                      #
    # This function demos different common parameter combinations and usecases for dropna. #
    ########################################################################################

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


    #######################################################################################
    # Now we drop potential duplicated rows                                               #
    # In pandas, this maps to the Dataframe.drop_duplicates function.                     #
    # This function demos different common  usecases for drop_duplicates.                 #
    #######################################################################################

    # drop a duplicated row if all columns have the same value
    '''
    df = df.drop_duplicates()
    '''

    # drop a duplicated row, but keep the last duplicate rather than the first
    '''
    df = df.drop_duplicates(keep='last')
    '''

    # drop a duplicated row where the defined columns share same values
    df = df.drop_duplicates(subset=['id'])

    return df



