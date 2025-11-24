import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from data_processing import extract, clean
import os

data_dir = os.path.join(str(ROOT), 'data_sources', 'data') 

def calculate_salary_statistics():
    input_file_path = os.path.join(data_dir, 'sample_data.csv')
    df = extract.read_csv(input_file_path)
    df = clean.dropnas(df)
    print(df)

if __name__ == "__main__":
    calculate_salary_statistics()
