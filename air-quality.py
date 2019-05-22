import pandas as pd
import numpy as np

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

# Converting strings to datetime objects

# Using the list comprehension

# df1['date'] = [pd.to_datetime(i) for i in df1['Czas mierzenia']]

# Using map and lambda functions

df1['date'] = df1['Czas mierzenia'].map(lambda x: pd.to_datetime(x[0:10]))

# Indexing df1 with DatetimeIndex

df1 = df1.set_index('date')

