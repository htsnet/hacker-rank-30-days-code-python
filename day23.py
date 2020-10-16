# BST Level-Order Traversal

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:20:25 2020

@author: hamil
"""


import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

       

    def levelOrder(self,root):
        if root is None:
            return
        
        orderToProcess = []
        orderToProcess.append(root)
        
        while len(orderToProcess) > 0:
            node = orderToProcess.pop(0)
            print(node.data, end=" ")
            
            if node.left is not None:
                orderToProcess.append(node.left)
                
            if node.right is not None:
                orderToProcess.append(node.right)
            
        return
        




        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
