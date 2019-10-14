# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:27:08 2018

@author: Aditya
"""

#cs,ms
a = [-1,2,3,-4,7]

cs = a[0]
ms = a[0]

for i in a[1:]:
    cs = max(cs+i,i)
    ms = max(cs,ms)

print(ms)
