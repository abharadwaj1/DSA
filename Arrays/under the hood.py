# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:40:11 2018

@author: Aditya
"""

import sys

n = 10
d = {}
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data) 
    d[i] = b
    data.append(n)