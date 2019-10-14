# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:31:16 2018

@author: Aditya
"""

class M:    
    def public(self):
        print ("Use Tab to see me!")
        
    def _private(self):
        print ("You won't be able to Tab to see me!")
        
object = M()
object.public()
object._private()

import ctypes

class DynamicArray:
    
    def __init__(self):
        self.n = 0 #len()
        self.capacity = 1 #getsizeof()
        self.Array = self.create_array(self.capacity)
        
    def __length__(self):
        return self.n
    
    def __getitem__(self,index):
        
        if not 0 <= index < self.n:
            return IndexError("out of bounds")
        
        return self.Array[index]
    
    def append(self,element):
        
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        
        self.Array[self.n]=element
        self.n+=1
    
    def _resize(self,new_capacity):
        
        NewArray = self.create_array(new_capacity)
        
        for i in range(self.n):
            NewArray[i] = self.Array[i]
        
        self.Array = NewArray
        self.capacity = new_capacity
    
    def create_array(self,new_capacity):
        return (new_capacity * ctypes.py_object)()
            
            
            
            
            
            
            
            
            
            