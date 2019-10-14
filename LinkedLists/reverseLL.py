# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:49:53 2018

@author: Aditya

Linked list reversed
"""

        
        
class Node(object):
    
    def __init__(self,val):
        self.value = val
        self.next_node = None

#.........now show with values......#
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.next_node = c
c.next_node = d


def rev_ll(head_node):

    previous = None
    while head_node:
        
        temp = head_node.next_node
        head_node.next_node = previous
        previous = head_node
        head_node = temp
        
    
    