import pandas as pd
import os

# Define the output date range
start_date = pd.to_datetime('2022-09-01')
end_date = pd.to_datetime('2024-11-04')
date_range = pd.DataFrame({'Period': pd.date_range(start=start_date, end=end_date, freq='B')})  # 'B' excludes weekends

# Initialize an empty DataFrame for the compiled data, with 'Period' as the first column
compiled_data = date_range.copy()

# Define the path where your updated .xlsx files are stored
directory_path = 'files'

# Loop through each .xlsx file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(directory_path, filename)

        # Load the .xlsx file and ensure the date format is correct
        data = pd.read_excel(file_path)
        data['Period'] = pd.to_datetime(data['Period'], dayfirst=True)

        # Rename the 'Net profit' column to the filename without extension for clarity
        file_label = os.path.splitext(filename)[0]
        data = data[['Period', 'Net profit']].rename(columns={'Net profit': file_label})

        # Merge each file’s data with the compiled_data on 'Period', filling any missing values with 0
        compiled_data = pd.merge(compiled_data, data, on='Period', how='left').fillna(0)

# Define the output file path
output_file = 'compiled_data.xlsx'

# Save the compiled DataFrame to an Excel file
compiled_data.to_excel(output_file, index=False)

print(f'Compiled data saved to {output_file}')
