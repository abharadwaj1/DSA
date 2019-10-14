# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:58:12 2018

@author: Aditya
"""
stack - ordered collection of items where the addition of new items
 and the removal of existing items always takes place at the same end.

top and base

LIFO

class Stack(object): # [1,2,4,3]-->top
    
    def __init__(self):
        self.stk = []
    
    def push(self,item):
        self.stk.append(item)
    
    def pop(self):
        self.stk.pop()  # return self.stk.pop()
    
    def peek(self):
        return self.stk[len(self.stk)-1] #top
    
    def isEmpty(self):
        return self.stk == []
    
    def show(self):
        return self.stk







