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