#!/usr/bin/env python
# coding: utf-8

import sys
import re

with open (sys.argv[1],'r') as file:
    for line in file:
	for i in re.findall('\+?\d{0,3}\s?\(?[-.\s]?\d{1,5}\)?[-.\s]?\d{1,5}[-.\s]?\d{1,5}',line):
	      print(i)

