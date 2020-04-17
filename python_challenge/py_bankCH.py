# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv

months = []
profits = []

closedfile = os.path.join('budget_data.csv')
#%%

with open(closedfile, 'r') as openfile:
    pybank_data = csv.reader(openfile, delimiter = ',')
    next(pybank_data)
    
    for i in pybank_data:
        months_col = i[0]
        profits_col = i[1]
        
        months.append(months_col)
        profits.append(profits_col)
        
#%%
total_months = len(months)
profits = [int(i) for i in profits]
total_profit = sum(profits)

#%%

##bankzip = zip(months, profits)
##print(bankzip)


#%%
#def average(i):
    #length = len(i)
    #total = 0
    #for j in i:
        #total += i
    #avg = total / length
    #return avg


#%%
    

print('Financial Analyis')
print('------------------')
print(f'Total Months: {total_months}')
print(f'Total $: ${total_profit:,d}')
print('Average Change: ')
print('Greatest increase in profit: $')
print('Greatest increase in loss: $')


#TO DO: Min/ Max and Total Functions
