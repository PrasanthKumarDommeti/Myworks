from math import *
from collections import *
from sys import *
from os import *

# Following is the List Node Class
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    temp = node.next
    node.data=temp.data
    node.next=temp.next
    del temp
    return node
    

    
