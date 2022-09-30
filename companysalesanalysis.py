

import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter


df = pd.read_csv("Desktop\SalesAnalysis\Sales_Data\Sales_April_2019.csv")
df


#list all files in a directory using os library
files = [file for file in os.listdir('Desktop\SalesAnalysis\Sales_Data')]
for file in files:
    print(file)


#Merging Data
all_data = pd.DataFrame()
for file in files:
        df = pd.read_csv("Desktop/SalesAnalysis/Sales_Data/"+file)
        all_data = pd.concat([all_data, df])

all_data.head()


#Clean Data
nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()

all_data = all_data.dropna(how='all')
all_data.head()

#Find 'Or' and drop
#temp_df = all_data[all_data['Order Date'].str[0:2] =='Or']
#temp_df.head() #Shows the rows with errors
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.head() 

#Drops the rows with errors
#Adding Additional columns
#Adding month column to the dataframe
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
all_data.head()


#Converting columns in to necessary data types
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


# Adding a sales column
all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
all_data.head()

#What was the best month for sales and how much was earned that month?
all_data.groupby('Month').sum()

# Plot the above data
results = all_data.groupby('Month').sum()
months = range(1, 13)


plt.bar(months, results['Sales'])
plt.xticks(months)
plt.xlabel('Month Number')
plt.ylabel('Sales in USD ($)')
plt.show()


