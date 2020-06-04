# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:12:35 2020

@author: kjpeng
"""

import pandas as pd
import matplotlib.pyplot as plt


#read CSV 
df = pd.read_csv('performance.csv')
data = df.loc[:,['date','year_revenue']]

data = data.set_index('date')

print('data',data)