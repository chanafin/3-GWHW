# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:16:11 2020

@author: chris
"""

import os
import csv

total_months = 0
profit_loss = 0
maxprofit = [" ", 0]
maxloss = [" ", 9999999999999999999999]
netchangelist = []

closedfile = os.path.join('budget_data.csv')

with open(closedfile, 'r') as openfile:
    pybank_data = csv.reader(openfile, delimiter = ',')
    next(pybank_data)
    nextrow = next(pybank_data)
    total_months = total_months + 1
    profit_loss = profit_loss + int(nextrow[1])
    previouschange = int(nextrow[1])
    
    
    for i in pybank_data:
        date_col = i[0]
        pl_col = int(i[1])
        
        total_months = total_months + 1
        
        profit_loss = profit_loss + pl_col
        
        netchange = pl_col - previouschange
        netchangelist.append(pl_col)
        
        if netchange > maxprofit[1]:
            maxprofit = [date_col, pl_col]
        if netchange < maxloss[1]:
            maxloss = [date_col, pl_col]



total_change = sum(netchangelist)
avg_change = int(total_change /total_months)


#%%

output = os.path.join('bank.txt')
with open(output, "w") as txt_file:
    financial_analysis = (
    f"\n\nFinancial Analyis\n"
    f"-------------------------\n"
    f'Total Months: {total_months}\n'
    f'Total $: ${profit_loss:,d}\n'
    f'Average Change: ${avg_change:,d}\n'
    f'Greatest increase in profit: ${maxprofit[1]:,d} in {maxprofit[0]} \n'
    f'Greatest increase in loss: ${maxloss[1]:,d} in {maxloss[0]} \n')
    print(financial_analysis, end="")
    txt_file.write(financial_analysis)