import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting seaborn styling for plots

sns.set()

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

# Removing of the first few records, and record with incorrect data

df1 = df1.loc['2018-04-20':]

df1 = df1.drop(pd.Timestamp('2019-02-08'))

# Add columns with year, month, and weekday name

df1['Year'] = df1.index.year
df1['Month'] = df1.index.month
df1['Weekday'] = df1.index.weekday

# Plotting the "first look" chart

view = df1['2018-09':'2019-03']

plt.figure(figsize=(10.24, 7.68))

plt.plot(df1['PM10'], color='red', label='PM10')
plt.plot(df1['PM25'], color='blue', label='PM25')
plt.legend(loc='best')
plt.title("PMs: 2018/04 - 2019/05")
plt.xticks(rotation=60)

plt.axes([0.15, 0.6, 0.25, 0.25])

plt.plot(view['PM10'], color='red')
plt.plot(view['PM25'], color='blue')
plt.title(label="PMs: 2018/09 - 2019/03")
plt.xticks(rotation=60)

plt.show()

# Line plot of the full time series of PM10 (there is a very strong correlation between PM2.5 and PM10,
# therefore only PM10 was used for further analysis), Temperatura and Wilgotność

plt.figure(figsize=(10.24, 7.68))

plt.subplot(3, 1, 1)
plt.plot(df1['PM10'], color='red')
plt.ylabel(r'PM10 $[µg/m^3]$')
# plt.xticks(color='w')

plt.subplot(3, 1, 2)
plt.plot(df1['Temperatura'], color='blue')
plt.ylabel(r'Temperature $[^oC]$')
# plt.xticks(color='w')

plt.subplot(3, 1, 3)
plt.plot(df1['Wilgotność'], color='green')
plt.ylabel(r'Humidity [%]')
# plt.xlabel('Date')

plt.show()

# TODO: Add dots plot: PM10, Wind