#!/usr/bin/env python
# coding: utf-8


import sys
import re
ens2gene={}
# first built my dictionary
with open ("mini.gtf",'r') as file:
    for line in file:
        matches = re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
#         print(matches)
        if matches:
            line = re.sub(matches[0][0],matches[0][1],line)
            print(line)

