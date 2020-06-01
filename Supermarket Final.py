#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("supermarket.csv",parse_dates= ['Date'])
df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')

df['Time'] ='-' + df['Time'].astype(str)
df["BasketID"] = df["Date"].astype(str) + df["Time"].astype(str) + df["Basket"].astype(str)

Introduction = """
Introduction
I have used numpy and pandas libray for the data analsyis required.
I have used the pandas.read_csv method for importing the supermarket.csv file.  
To parse the dates, I have used the parse_dates parameter of the read_csv method as half of the values are in a different format.
I have then converted it into the standard format.
To make a unique key identifier of each basket, I have joined the columns 'Date','Time' and 'Basket' to make a new column 'BasketID'.
I have also appended a '-' before the time to split the date from the unique id
Following is the processed dataframe:
"""

print(Introduction)
print(df.head(5))

dept = df.iloc[0:,0] 
product = df.iloc[0:,1]
checkout = df.iloc[0:,2]
date = df.iloc[0:,3]
time = df.iloc[0:,4]
basketid = df.iloc[0:,7]
total = df.iloc[0:,6]

unique,x = np.unique(basketid,return_counts = True) 

q1 = """

Q1.
The following histogram shows the distribution of basket sizes measured by the number of items in a basket.   
Here, we can see that the most popular basket sizes are baskets with 1-5 items in the basket.
"""

print(q1)
sns.set(style='whitegrid', palette="deep", font_scale=1.1, rc={"figure.figsize": [8, 5]})
g = sns.distplot(x, bins=20, kde=False, rug=True,).set(xlabel='Number of Items', ylabel='Number of Baskets')
plt.show()


from collections import defaultdict
size = defaultdict(int) 

for i in basketid:
    size[i] += 1 
    
dollars = defaultdict(int)

for i in range(len(basketid)):
    dollars[(basketid[i])] += total[i]
    
q2 = """

Q2
The following scatter plot shows us the the relation between each individual basket and dollar value of the basket. 
The table below the plot lists how much money does store get from each size of the basket.
"""

print(q2)
plt.scatter(list(size.values()), list(dollars.values()), edgecolors='g')
plt.xlabel('Number of items')
plt.ylabel('Dollars')
plt.title('Items vs Dollars')
plt.show()

baskets = defaultdict(int) 
for i in size.keys():
    baskets[size[i]] += dollars[i]
    
print('Items \t\t\t Dollars')
for n,g in zip(list(baskets.keys()),list(baskets.values())):
    print(n,g,sep='\t\t\t')
    
    
print("The second scatter plot shows us money from each size of the basket. We can infer from this plot that light (small baskets) customers are more important as they generate more revenue.")    
plt.scatter(list(baskets.keys()), list(baskets.values()))
plt.xlabel('Number of items in a basket')
plt.ylabel('Dollars Earned')
plt.title('Items vs Dollars')
plt.show()

dates = list(size.keys())

for i in range(len(dates)):
    dates[i] = dates[i].split("-")[0]
    
import datetime  
from datetime import date 
import calendar 
  
def findDay(date): 
    month, day, year = (int(i) for i in date.split('/'))     
    born = datetime.date(year, month, day) 
    return born.strftime("%A") 

days = []
for i in dates:
    days.append(findDay(i))
    
monday=0
tuesday=0
wednesday=0
thursday=0
friday=0
saturday=0
sunday=0

for i in size.keys():
    k = i.split("-")[0]
    today = findDay(k)
    if today=="Monday":
        monday += size[i]
    elif today=="Tuesday":
        tuesday += size[i]
    elif today=="Wednesday":
        wednesday += size[i]
    elif today=="Thursday":
        thursday += size[i]
    elif today=="Friday":
        friday += size[i]
    elif today=="Saturday":
        saturday += size[i]
    elif today=="Sunday":
        sunday += size[i]
        
q3a = """

Q3.A.
The follwing table shows the number of baskets on each day of the week.
The bar graph visualizes the above relationship.
We can clearly see through the chart, that SATURDAY is the busiest day of the week. 
"""

shoppingTrips=[monday,tuesday,wednesday,thursday,friday,saturday,sunday]
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(q3a)
print('Days \t\t Baskets')
for n,g in zip(weekdays,shoppingTrips):
    print(n,g,sep='\t\t')
    
plt.bar(weekdays,shoppingTrips,color = "red")
plt.xlabel("Days")
plt.ylabel("Number of Baskets")
plt.title("Busiest Day of Week")
plt.show()

dmonday=0
dtuesday=0
dwednesday=0
dthursday=0
dfriday=0
dsaturday=0
dsunday=0

for i in dollars.keys():
    k = i.split("-")[0]
    today = findDay(k)
    if today=="Monday":
        dmonday += dollars[i]
    elif today=="Tuesday":
        dtuesday += dollars[i]
    elif today=="Wednesday":
        dwednesday += dollars[i]
    elif today=="Thursday":
        dthursday += dollars[i]
    elif today=="Friday":
        dfriday += dollars[i]
    elif today=="Saturday":
        dsaturday += dollars[i]
    elif today=="Sunday":
        dsunday += dollars[i]
        
profit=[dmonday,dtuesday,dwednesday,dthursday,dfriday,dsaturday,dsunday]

q3b = """

Q3. B.
The follwing table shows the dollars earned on each day of the week.
The bar graph visualizes the above relationship.
We can clearly see through the chart, that SATURDAY is the most profitbale day of the week, as it is also the busiest day

"""

print(q3b)
print('Days \t\t Dollars Earned')
for n,g in zip(weekdays,profit):
    print(n,g,sep='\t\t')
    
plt.bar(weekdays,profit,color = "blue")
plt.xlabel("Days")
plt.ylabel("Dollars Earned")
plt.title("Most Profitable Day of Week")
plt.show()

summary="""
Summary 

Through the data analysis of the supermarket transactions dataset, we can hence conclude that the population
mostly buys less number of items in one trip. They prefer to spend less rather than buying a lot of items.
Hence, the light basket customers are more important. The supermarket can install more express counters 
for less number of items to increase the sales.
We can also conclude that Friday and Saturday are the most busiest and the most profitable days of the week.
The supermarket should ensure that enough staff is available on these days to assist the customers.

"""

print(summary)


# In[ ]:




