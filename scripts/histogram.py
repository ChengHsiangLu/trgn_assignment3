#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import csv
import sys
import argparse
from matplotlib import pyplot as plt
column=[]
with open("mini.gtf") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for idx, line in enumerate(tsv_file):
        if idx > 4:
            column.append(line[4])
            
fig, ax=plt.subplots(figsize=[50,8])
ax.hist(column, bins=20)
plt.show()
# print (column)
plt.savefig('plot.png') 

