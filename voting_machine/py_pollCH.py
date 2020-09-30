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

#%%
closedfile = os.path.join('election_data.csv')
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
#%%
winners_circle = [Khan, Correy, Li, Otooley]
winner = max(winners_circle)
winner_name = ' ' 

if winner == Khan:
    winner_name = "Khan"
elif winner == Correy:
    winner_name = 'Correy'
elif winner == Li:
    winner_name = "Li"
else: winner_name = "O'Tooley"
#%%

khanpct = Khan / total_votes
correypct = Correy / total_votes
lipct = Li / total_votes
otooleypct = Otooley / total_votes

#%%
output = os.path.join('poll.txt')
with open(output, "w") as txt_file:
    election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: [{total_votes:,d}]\n"
    f'Khan: {khanpct:,.2%} [{Khan:,d}]\n'
    f'Correy: {correypct:,.2%} [{Correy:,d}]\n'
    f'Li: {lipct:,.2%} [{Li:,d}]\n'
    f"O'Tooley: {otooleypct:,.2%} [{Otooley:,d}]\n"
    f"-------------------------\n"
    f'Winner: {winner_name}\n')
    print(election_results, end="")
    txt_file.write(election_results)
    