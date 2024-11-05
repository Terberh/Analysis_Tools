This python script will take Ninjatrader 8 correctly formatted back test data, and compile the data together into a single xlsx document, with correct date alignment.

Setup Guide:

Step 1: Install Required Packages

pip install pandas openpyxl

Step 2: Organize Your Files

Ensure your .xlsx files are saved in a folder named files within your project directory.

Double-check the directory structure. It should look like this:

YourProject/
├── files/
│   ├── file1.xlsx
│   ├── file2.xlsx
│   └── ...
├── compile_excel.py
├── .venv/       # The virtual environment folder

Step 3: Update and Review the Script

Open compile_excel.py in the PyCharm editor.

Verify that directory_path is set correctly. Since your files are in a folder named files within the project directory, the line should be:

directory_path = 'files'

Step 4: Update date to & from values

Step 5: Verify the Output

Check the project directory for compiled_data.xlsx.

Open the file to confirm it contains a single Period column covering the date range, with separate columns for Net Profit values from each .xlsx file.