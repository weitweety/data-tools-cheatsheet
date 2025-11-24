#!/usr/bin/env python3
"""
Script to generate sample_data.xlsx file from the CSV data.
This ensures all three file formats (CSV, JSON, XLSX) have identical content.
"""

import pandas as pd
from pathlib import Path

# Define the data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 
             'Edward Norton', 'Fiona Apple', 'George Washington', 'Hannah Montana'],
    'age': [28, 34, 29, 31, 27, 35, 42, 26],
    'city': ['New York', 'San Francisco', 'Chicago', 'Boston', 
             'Seattle', 'Los Angeles', 'Washington DC', 'Austin'],
    'salary': [75000, 85000, 70000, 80000, 72000, 90000, 95000, 68000],
    'department': ['Engineering', 'Marketing', 'Sales', 'Engineering', 
                   'HR', 'Marketing', 'Engineering', 'Sales'],
    'join_date': ['2020-01-15', '2019-03-22', '2021-06-10', '2020-11-05', 
                  '2022-02-18', '2018-09-12', '2017-04-30', '2021-08-25']
}

# Create DataFrame
df = pd.DataFrame(data)

# Get the output directory (data_sources/data)
script_dir = Path(__file__).parent
data_dir = script_dir.parent / 'data'
data_dir.mkdir(parents=True, exist_ok=True)

# Write to XLSX
output_file = data_dir / 'sample_data.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Successfully created {output_file}")

