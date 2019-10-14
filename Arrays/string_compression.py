# -*- coding: utf-8 -*-
"""
Created on Sat May 26 14:50:03 2018

@author: Aditya

problem : string compression
"""

s= "aaabbccddaaAA"

temp = s[0]
count  = 0
L1 = []
for i in s:

    if(temp!=i):
        L1.append(temp+str(count))
        temp = i
        count=0
    if(temp==i):
        count+=1
    
    s1 = i + str(count)
    
L1.append(temp+str(count))
result = ''.join(map(str,L1))