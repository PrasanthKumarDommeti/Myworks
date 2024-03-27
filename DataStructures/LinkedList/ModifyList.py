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
# It can passes the half of the test cases and remaining half will be time exceed limit errors was occured
def modifyLL(head):
	first = head
	while first !=None and first.next!=None:
		temp=first
		x = None
		while temp.next!=None:
			x=temp
			temp=temp.next
		if x!=None:
			x.next=None
		temp.next=first.next
		first.next=temp
		first = first.next.next

	return head
    
    
