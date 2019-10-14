# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:21:15 2018

@author: Aditya
"""

class Deque(object):      # assuming   rear<--[1,2,4,3]-->front
    
    def __init__(self):
        self.dq = []
    
    def enqueue_front(self,item):
        self.dq.append(item)
    
    def enqueue_rear(self,item):
        self.dq.insert(0,item)
        
    def dequeue_front(self):
        self.dq.pop()
    
    def dequeue_rear(self):
        self.dq.pop(0)
    
    def show(self):
        return self.dq
    
    def size(self):
        return len(self.dq)
    
    def isEmpty(self):
        return self.dq == []


