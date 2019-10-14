# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:09:02 2018

@author: Aditya

MEMOIZATION

"""

d1 = {}
def factorial(n):
    if n<2:
        return 1
    if not n in d1:
        d1[n] = n * factorial(n-1)
        print("first time input")
    print("second time input")
    return d1[n]
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def  factorialfactori (k):
    
    if k < 2: 
        return 1
    
    return k * factorial(k - 1)

factorial = Memoize(factorial)