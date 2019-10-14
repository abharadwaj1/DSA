# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:59:28 2018

@author: Aditya
"""



class Node(object):
    
    def __init__(self,val):
        self.value = val
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d


def n_to_last(n,head_node):
    
    head1 = head_node
    count = 0
    while head1:
        temp = head1.next_node
        head1 = temp
        count+=1
    step = count-n
    for i in range(step):
        temp = head_node.next_node
        head_node = temp
    return temp.value
        
    
