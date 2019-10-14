# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:52:43 2018

@author: Aditya
"""

class Queue(object): # rear<--[4,3,2,1]-->front
    
    def __init__(self):
        self.q = []
    
    def enqueue(self,item):
        self.q.insert(0,item) #if you use append() then use pop(0)
    
    def dequeue(self):
        self.q.pop()
    
    def isEmpty(self):
        return self.q == []
    
    def size(self):
        return len(self.q)

    def show(self):
        return self.q


