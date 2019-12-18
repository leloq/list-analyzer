# Python script for easy pivot analysis of columns in Excel files
Python-based tool to make column specific pivot analysis of columns of excel tables. Outputs tables of distribution of values, absolute amount of values and percentage. Usable through command line.

# Pre-Requisites
python (> version 3.0)
pip install pandas, numpy, PrettyTable

# How to use it
1. Clone repository
2. Save to-be-analyzed excel file in folder where also main.py is located
3. Start script with command "python main.py"
4. Enter exact name of Excel file ("example.xlsx"). Afterwards, included columns of Excel table get listed
5. Select indices of to-be-analyzed columns, comma separated ("2, 3, 6")

Optional: In main.py, change noResults and html to change number of displayed in results and if they are displayed in html or string format.
