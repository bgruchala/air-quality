import pandas as pd

# Assign spreadsheet filename to 'file'

file = 'data/201803190001 - dzienne.xlsx'
# TODO: Solve the problem with reading the original file.
#  The original file has been converted to xlsx format. Otherwise, an error occured.

# Load spreadsheet

xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1

df1 = xl.parse('Worksheet')

# Print the basic data from df1

print(df1.head())

print(df1.info())
