# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:47:53 2020

@author: chris
"""

import os
import csv

voterid = []
Khanvote = []
Correyvote = []
Livote = []
Otooleyvote = []


closedfile = os.path.join('election_data.csv')
#%%

with open(closedfile, 'r') as openfile:
    pypoll = csv.reader(openfile, delimiter = ',')
    next(pypoll)
    
    for i in pypoll:
        voterid_col = i[0]
        candidate_col = i[2]
          
        voterid.append(voterid_col)
        
        if candidate_col == 'Khan':
            Khanvote.append(candidate_col)
        if candidate_col == 'Correy':
            Correyvote.append(candidate_col)  
        if candidate_col == 'Li':
            Livote.append(candidate_col)
        if candidate_col == "O'Tooley":
            Otooleyvote.append(candidate_col)
#%%

total_votes = len(voterid)
Khan = len(Khanvote)
Correy = len(Correyvote)
Li = len(Livote)
Otooley = len(Otooleyvote)

winners_circle = [Khan, Correy, Li, Otooley]
winner = max(winners_circle)


khanpct = Khan / total_votes
correypct = Correy / total_votes
lipct = Li / total_votes
otooleypct = Otooley / total_votes

#%%
     
print('Election Results')
print('------------------')
print(f'Total Votes: {total_votes:,d}')
print('------------------')
print(f'Khan: {khanpct:,.2%} [{Khan:,d}]')
print(f'Correy: {correypct:,.2%} [{Correy:,d}]')
print(f'Li: {lipct:,.2%} [{Li:,d}]')
print(f"O'Tooley: {otooleypct:,.2%} [{Otooley:,d}]")
print('------------------')
print(f'Winner: var{winner}')
print('------------------')

