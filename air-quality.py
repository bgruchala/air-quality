import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Removing of the first few record

df1 = df1.loc['2018-04-20':]

# Plotting the "first look" chart

view = df1['2018-09':'2019-03']

plt.plot(df1['PM10'], color='red', label='PM10')
plt.plot(df1['PM25'], color='blue', label='PM25')
plt.legend(loc='best')
plt.title("PM's 2018/04 - 2019/05")
plt.xticks(rotation=60)

plt.axes([0.18, 0.6, 0.25, 0.25])

plt.plot(view['PM10'], color='red')
plt.plot(view['PM25'], color='blue')
plt.title(label="PM's 2018/09 - 2019/03", fontdict={'fontsize': 10})
plt.xticks(rotation=60)

plt.show()
