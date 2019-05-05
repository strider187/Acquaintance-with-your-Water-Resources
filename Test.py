# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:52:54 2018

@author: Abstergo
"""

import pandas as pd
import numpy as np
import statistics as stat


dataset = pd.read_csv("Req_Data_1992.csv")
dataset = dataset.iloc[0:12,:]
mylist = []

for index, row in dataset.iterrows():
    mylist.append(row['1992'])
    
dataset.append(stat.median(mylist))
        