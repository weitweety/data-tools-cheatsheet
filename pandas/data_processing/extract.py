import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def read_csv(file_path: str) -> pd.DataFrame:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        
        logger.info(f"Extracting data from {file_path}")
        df = pd.read_csv(file_path)
        
        logger.info(f"Successfully extracted {len(df)} records from {file_path}")
        return df
        
    except Exception as e:
        logger.error(f"Error extracting data from {file_path}: {str(e)}")
        raise

def read_json(file_path: str) -> pd.DataFrame:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"JSON file not found: {file_path}")

        logger.info(f"Extracting data from {file_path}")
        # possible orient: split, records, index, columns, values
        # our json file is formatted as records orient
        df = pd.read_json(file_path, orient="records")

        logger.info(f"Successfully extracted {len(df)} records from {file_path}")
        return df

    except Exception as e:
        logger.error(f"Error extracting data from {file_path}: {str(e)}")
        raise

def read_excel(file_path: str) -> pd.DataFrame:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"EXCEL file not found: {file_path}")

        logger.info(f"Extracting data from {file_path}")
        # the default read_excel would use the excel header as column names.
        # This is usually desired. Otherwise, set header=None
        df = pd.read_excel(file_path)

        logger.info(f"Successfully extracted {len(df)} records from {file_path}")
        return df

    except Exception as e:
        logger.error(f"Error extracting data from {file_path}: {str(e)}")
        raise