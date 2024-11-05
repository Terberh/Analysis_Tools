This python script will take Ninjatrader 8 exported back test data, and ammend the xlsx file to include non-trading days as $0.

Guide to install with PyCharm

Step 1: Set Up PyCharm

1. Open PyCharm and create a new project (or use an existing one).
2. Ensure that your project has a Python interpreter set up with pandas installed. If not, you can install it by running:

pip install pandas openpyxl
(openpyxl is needed if you're working with .xlsx files)

Step 2: Add the Python Script

1. In the project directory, create a new Python file, e.g., update_excel.py.
2. Copy the Python script provided into this file.
3. Replace '/path/to/your/file.xlsx' with the path to your Excel file, and '/path/to/your/updated_file.xlsx' with the desired output file path.

Step 3: Run the Script

1. In PyCharm, right-click on the update_excel.py file and select Run 'update_excel'.
2. If there are no issues, the script will run, and you’ll see the message Updated file saved at: <output_path> in the console.

Step 4: Check the Output

1. Open the output file in Excel to verify that it contains all dates, with non-trading days filled as specified.

Additional Notes

1. Path Adjustments: If using a relative path, place your Excel file within the project directory.
2. Error Handling: If the file path is incorrect or there’s an issue with the data format, PyCharm will display errors in the console, making it easier to troubleshoot.