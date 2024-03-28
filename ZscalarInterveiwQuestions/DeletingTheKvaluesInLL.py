from os import *
from sys import *
from collections import *
from math import *

'''
    # Linked List Node class for reference

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
'''

def removeNodes(head_ref, key):
    # Write your code here.
     # Store head node 
    temp = head_ref 
    prev = None
  
    # The first value must be occured at key
    while (temp != None and temp.data == key): 
        head_ref = temp.next  # Changed head 
        temp = head_ref         # Change Temp 
  
    
    while (temp != None): 
  
        # Itterate the prev & temp
        while (temp != None and temp.data != key): 
            prev = temp 
            temp = temp.next
  
        # If key was not present in linked list 
        if (temp == None): 
            return head_ref 
  
        # Unlink the node from linked list when temp.data was matched
        prev.next = temp.next
  
        # Update Temp for next iteration of outer loop 
        temp = prev.next
    return head_ref 