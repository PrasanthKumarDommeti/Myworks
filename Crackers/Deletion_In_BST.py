from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
def bstDelete(root, key):  
    # Base case: If the tree is empty  
    if root is None:  
        return root  

    # Otherwise, recur down the tree  
    if key < root.data:  
        root.left = bstDelete(root.left, key)  # Traverse to the left subtree  
    elif key > root.data:  
        root.right = bstDelete(root.right, key)  # Traverse to the right subtree  
    else:  
        # This is the node to be deleted  

        # Case 1: Node with only one child or no child  
        if root.left is None:  
            return root.right  # If no left child, return right child  
        elif root.right is None:  
            return root.left  # If no right child, return left child  

        # Case 2: Node with two children  
        # Get the inorder successor (smallest in the right subtree)  
        min_larger_node = findMin(root.right)  

        # Copy the inorder successor's content to this node  
        root.data = min_larger_node.data  

        # Delete the inorder successor  
        root.right = bstDelete(root.right, min_larger_node.data)  

    return root  
def findMin(node):  
    current = node  
    while current.left is not None:  
        current = current.left  
    return current 
