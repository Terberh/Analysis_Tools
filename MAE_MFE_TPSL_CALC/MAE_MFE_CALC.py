import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'path_to_your_excel_file.xlsx'  # Replace with the correct file path
data = pd.read_excel(file_path)

# Ensure columns are numeric
data['MAE'] = pd.to_numeric(data['MAE'], errors='coerce')
data['MFE'] = pd.to_numeric(data['MFE'], errors='coerce')

# Calculate statistics for MAE
mae_mean = data['MAE'].mean()
mae_median = data['MAE'].median()
mae_std_dev = data['MAE'].std()

# Calculate statistics for MFE
mfe_mean = data['MFE'].mean()
mfe_median = data['MFE'].median()
mfe_std_dev = data['MFE'].std()

# Plot MAE distribution
plt.figure(figsize=(10, 5))
plt.hist(data['MAE'], bins=20, alpha=0.7, color='blue', edgecolor='black')
plt.axvline(mae_mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mae_mean:.2f}')
plt.axvline(mae_median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {mae_median:.2f}')
plt.title('Distribution of MAE')
plt.xlabel('MAE')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Plot MFE distribution
plt.figure(figsize=(10, 5))
plt.hist(data['MFE'], bins=20, alpha=0.7, color='orange', edgecolor='black')
plt.axvline(mfe_mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mfe_mean:.2f}')
plt.axvline(mfe_median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {mfe_median:.2f}')
plt.title('Distribution of MFE')
plt.xlabel('MFE')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Print calculated statistics
print("Statistics for MAE:")
print(f"Mean: {mae_mean:.2f}, Median: {mae_median:.2f}, Std Dev: {mae_std_dev:.2f}")

print("Statistics for MFE:")
print(f"Mean: {mfe_mean:.2f}, Median: {mfe_median:.2f}, Std Dev: {mfe_std_dev:.2f}")

# Recommend profit targets and stop losses
conservative_target = mfe_mean
aggressive_target = mfe_mean + mfe_std_dev
tight_stop = mae_mean
conservative_stop = mae_mean + mae_std_dev

print("\nRecommendations:")
print(f"Conservative Profit Target: {conservative_target:.2f}")
print(f"Aggressive Profit Target: {aggressive_target:.2f}")
print(f"Tight Stop Loss: {tight_stop:.2f}")
print(f"Conservative Stop Loss: {conservative_stop:.2f}")
