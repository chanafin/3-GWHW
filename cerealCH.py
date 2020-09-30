# -*- coding: utf-8 -*-

"Import Dependencies"
import os
import csv

"Join, Open and Read the CSV" 
closed_file = os.path.join('cereal.csv')
with open(closed_file, 'r') as open_file:
    
    cereal_reader = csv.reader(open_file)
    next(cereal_reader, None)
    "Loop through cereal_reader, identify the columns you wish to analyze"  
    for i in cereal_reader:
        fiber_count = i[7]
        cereal_name = i[0]
        "Run an if statement based on the condition you wish to explore" 
        if float(fiber_count) >= 5:
            "Use an f-string to include the defined variables within your loop"
            print(f'{cereal_name} has {fiber_count} grams of fiber')
    
    