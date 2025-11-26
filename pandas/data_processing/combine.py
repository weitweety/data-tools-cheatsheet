import pandas as pd
import logging
from datetime import datetime
from typing import List

def concat_data_rows(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    # pd.concat() is common when we need to concat two data frames
    # along index or columns

    # simply concat the dfs on index axis. Keep the original index
    # if there are duplicate indexes across dfs then the output will keep the indexes
    # duplicated
    '''
    df = pd.concat(df_list)
    '''

    # if we have duplicate indexes from various dfs, maybe we want hierarchical index
    # that could help us distinguish the original df. keys and names are two helpful parameters
    '''
    keys_for_df = ['df'+str(x) for x in range(len(df_list))]
    colnames_for_indexes = ['original_df', 'id']

    df = pd.concat(df_list, keys = keys_for_df, names = colnames_for_indexes)
    '''

    # clear existing index and reset a new one. so there's a new index column
    # as 0, 1, .......
    df = pd.concat(df_list, ignore_index=True)

    return df