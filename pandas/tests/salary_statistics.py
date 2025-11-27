import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from data_processing import extract, clean, transform, combine, aggregate
import os

data_dir = os.path.join(str(ROOT), 'data_sources', 'data') 

def calculate_salary_statistics():
    # source file being json:
    input_file_path = os.path.join(data_dir, 'sample_data.json')
    df = extract.read_json(input_file_path)

    '''
    # source file being csv:
    input_file_path = os.path.join(data_dir, 'sample_data.csv')
    df = extract.read_csv(input_file_path)
    '''
    '''
    # source file being excel:
    input_file_path = os.path.join(data_dir, 'sample_data.xlsx')
    df = extract.read_excel(input_file_path)
    '''

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

    # on pandas, we could also directly compute new column values
    # from existing columns, if necessary
    df_concat["salary_per_month"] = df_concat["salary"] // 12

    # try to show some statistics with sample aggregate functions
    df_avg_department_salary = aggregate.avg_salary_groupby_department(df_concat)
    print(df_avg_department_salary)

    df_minmax_department_salary = aggregate.min_max_salary_groupby_department(df_concat)
    print(df_minmax_department_salary)


if __name__ == "__main__":
    calculate_salary_statistics()
