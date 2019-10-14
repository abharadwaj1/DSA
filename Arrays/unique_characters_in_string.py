# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:36:14 2018

@author: Aditya
"""

def uni_char(s):
    from collections import Counter
    repeat = Counter()
    for i in s:
        repeat[i]+=1
    if max(repeat.values())>1:
        return False
    else:
        return True


def uni_char1(s):
    return len(set(s)) == len(s)