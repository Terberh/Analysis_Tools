import pandas as pd
from datetime import timedelta

# Load the data from the Excel file
file_path = 'NQ15SMALong.xlsx'  # Replace with your actual file path
output_path = 'Updated_NQL.xlsx'  # Output file path

# Load the data
df = pd.read_excel(file_path)

# Convert 'Period' column to datetime format
df['Period'] = pd.to_datetime(df['Period'], dayfirst=True)

# Set start and end date for inserting missing dates
start_date = pd.to_datetime('2022-11-09')  # Start date
end_date = df['Period'].max()  # Maximum date from the original data

# Generate a complete date range excluding weekends
date_range = pd.bdate_range(start=start_date, end=end_date)

# Identify the missing dates to insert (only those in the desired range)
missing_dates = date_range.difference(df['Period'])

# Create a DataFrame for missing dates with the required values
missing_data = pd.DataFrame({
    'Period': missing_dates,
    'Net profit': 0.0,       # Set to $0.00
    'Gross profit': 0.0,     # Set to $0.00
    'Gross loss': 0.0,       # Set to $0.00
    'Commission': 0.0,       # Set to $0.00
    'Cum. max. drawdown': 0.0, # Cumulative values initialized
    'Max. drawdown': 0.0     # Cumulative values initialized
})

# Fill cumulative columns with the last available values from the original DataFrame
cumulative_cols = ['Cum. max. drawdown', 'Max. drawdown']
for col in cumulative_cols:
    last_value = df[col].iloc[-1] if not df[col].empty else 0
    missing_data[col] = last_value

# Append missing data to the original DataFrame and sort by Period
df_complete = pd.concat([df, missing_data]).sort_values('Period').reset_index(drop=True)

# Save the updated DataFrame to a new Excel file
df_complete.to_excel(output_path, index=False)

# Print original total and final total net profit for verification
original_total_net_profit = df['Net profit'].sum()
print("Original total net profit:", original_total_net_profit)

final_total_net_profit = df_complete['Net profit'].sum()
print("Final total net profit:", final_total_net_profit)
print("Updated file saved at:", output_path)
