import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from data_processing import extract, clean, transform, combine
import os

data_dir = os.path.join(str(ROOT), 'data_sources', 'data') 

def calculate_salary_statistics():
    input_file_path = os.path.join(data_dir, 'sample_data.csv')
    df = extract.read_csv(input_file_path)
    df = clean.drop_problematic_data(df)
    df = transform.fill_data(df)
    df = transform.cast_data(df)
    df = df.set_index('id')

    # perform some combines
    input_file_path2 = os.path.join(data_dir, 'sample_data.csv')
    df2 = extract.read_csv(input_file_path2)
    df2 = clean.drop_problematic_data(df2)
    df2 = transform.fill_data(df2)
    df2 = transform.cast_data(df2)
    df2 = df2.set_index('id')

    df_concat = combine.concat_data_rows([df, df2])
    print(df_concat)

if __name__ == "__main__":
    calculate_salary_statistics()
