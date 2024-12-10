This python script will take will create a distribution table of MAE & MFE data. It will then calculate the mean and median from the data, and advise take profit, and stop loss calculations based on std deviations from mean values.

Setup Guide:

Step 1: Export xlsx back test data from NT8. Delete all columns apart from Avg. MAE & Avg. MFE, remove all '$' from values, rename Column heads to 'MAE' & 'MFE'

Example;
MAE     MFE
562     322
321     234
...     ...

Step 2: Install Required Packages

pip install pandas openpyxl
pip install matplotlib

Step 3: Organize Your Files

Ensure your .xlsx files are saved in a folder named files within your project directory.

Double-check the directory structure. It should look like this:

YourProject/
├── files/
│   ├── file1.xlsx
│   ├── file2.xlsx
│   └── ...
├── compile_excel.py
├── .venv/       # The virtual environment folder

Step 4: Update and Review the Script

Open compile_excel.py in the python environment.

Verify that directory_path is set correctly. Since your files are in a folder named files within the project directory, the line should be:

directory_path = 'files'

Step 5: Update date to & from values

Step 6: Verify the Output

Check the project directory for compiled_data.xlsx.

Open the file to confirm it contains a single Period column covering the date range, with separate columns for Net Profit values from each .xlsx file.