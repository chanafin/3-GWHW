# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:39:13 2020

@author: chris
"""

import os
import csv
    
closed_file = os.path.join('cereal.csv')
with open(closed_file, 'r') as open_file:
    
    cereal_reader = csv.reader(open_file)
    next(cereal_reader, None)
    
    
    for i in cereal_reader:
        fiber_count = i[7]
        cereal_name = i[0]
        if float(fiber_count) >= 5:
            print(f'{cereal_name} has {fiber_count} grams of fiber')
    
    