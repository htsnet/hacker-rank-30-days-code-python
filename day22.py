# Binary Search Trees


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

    def getHeight(self,root):
        #verify if the tree is empty
        if root is None:
            return 0
        else:
            #if not empty, call recursivelly the another function
            return max(self.actualHeight(root.left), self.actualHeight(root.right))
        
    def actualHeight(self,node):
        if node is None:
            return 0
        else:
            return 1 + max(self.actualHeight(node.left), self.actualHeight(node.right))
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
