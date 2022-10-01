

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

#Which city has the higher number of sales
#Get City and State

def get_state(address):
    return address.split(',')[2].split(' ')[1]

def get_city(address):
    return address.split(',')[1]

#all_data['State'] = all_data['Purchase Address'].apply(lambda x: get_state(x))
#all_data.head()
all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' ' + get_state(x))
all_data.head()


#all_data.drop(columns = 'State', inplace = True)
#all_data.drop(columns = 'City', inplace = True)
#all_data.head()


#Which city has the higher number of sales
# Plot the above data
results = all_data.groupby('City').sum()
results

cities = [city for city, df in all_data.groupby('City')]

plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation = 'vertical', size = 8)
plt.xlabel('Cities')
plt.ylabel('Sales in USD ($)')
plt.show()

#Best time to advertise a product
#convert into date time
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

#get hours, minutes
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()

