# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:09:47 2019

@author: Aditya
"""
OOP implementation-

class BT(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.LC = None
        self.RC = None
    
    def insertleftchild(self,newnode):
        if self.LC == None:
            self.LC = BT(newnode) #if LC wasn't there before
        else:
            temp = BT(newnode)
            temp.LC = self.LC
            self.LC = temp
    
    def insertrightchild(self,newnode):
        if self.RC == None:
            self.RC = BT(newnode) #if LC wasn't there before
        else:
            temp = BT(newnode)
            temp.RC = self.RC
            self.RC = temp
    
    def insertheirarchyleft(self,newnode):
        if self.LC == None:
            self.LC = BT(newnode)        
        else:
            parentnode = BT(self.LC)
            parentnode.LC = BT(newnode)
            self.LC = parentnode
            
    def insertheirarchyright(self,newnode):
        if self.RC == None:
            self.RC = BT(newnode)        
        else:
            parentnode = BT(self.RC)
            parentnode.RC = BT(newnode)
            self.RC = parentnode
        
    def preorder(self):
       print(self.key)
       if self.LC:
           self.LC.preorder()
#       print("this is now in - ",self.key) # 9,8,4,2 Backtracking
       if self.RC:
           self.RC.preorder()
           
    def inorder(self):
       if self.LC:
           self.LC.inorder()
       print(self.key)
       if self.RC:
           self.RC.inorder()
         
    def postorder(self):
       if self.LC:
           self.LC.postorder()
           #print("this is now in left - ",self.key) # 9,8,4,2 Backtracking
       if self.RC:
           self.RC.postorder()
           #print("this is now in right - ",self.key) # 9,8,4,2 Backtracking
       print(self.key)
        
        
        
    "  Example: [1[2[4[8],5],3[6,7]]]
    tree = BT(1)
    tree.LC = 2
    tree.RC = 3
    tree.insertheirarchyleft(4)
    tree.insertheirarchyright(7)
    tree.LC.LC.insertheirarchyleft(8)
    tree.LC.LC.LC.insertheirarchyleft(9)
    tree.LC.insertheirarchyright(5)
    tree.RC.insertheirarchyleft(6)
" btw use tree.LC.key if you use insertheirarchyleft

tree = BT('A')
tree.LC = 'B'
tree.RC = 'C'
tree.insertheirarchyleft('D')
tree.insertheirarchyright('F')
tree.RC.insertheirarchyleft('E')
tree.RC.LC.insertheirarchyright('G')
tree.RC.RC.insertheirarchyleft('H')
tree.RC.RC.insertheirarchyright('I')






# Binary tree implementation using list of lists


def BT(r):
    return [r,[],[]]

def insertleft(root,newbranch):
    t = root.pop(1)
    
    if len(t)>1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
    
    return root

def insertright(root,newbranch):
    t = root.pop(2)
    
    if len(t)>1:
        root.insert(2,[newbranch,[],t])
    else:
        root.insert(1,[newbranch,[],[]])
    
    return root

def getrootvalue(root):
    return root[0]

def setrootvalue(root,newroot):
    root[0] = newroot

def getleftchild(root):
    return root[1]

def getrightchild(root):
    return root[2]



