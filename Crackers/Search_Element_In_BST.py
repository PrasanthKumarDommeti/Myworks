'''
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

from typing import List

def searchInBST(root, x):
    # Write your code here.
    
    if root==None:
        return False
    if root.data==x:
        return True
    if root.data<x:
        return searchInBST(root.right,x)
    elif root.data>x:
        return searchInBST(root.left,x)
