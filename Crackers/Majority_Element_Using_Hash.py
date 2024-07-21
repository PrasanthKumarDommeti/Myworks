from math import *
from collections import *
from sys import *
from os import *

#def findMajorityElement(arr, n):
	# Write your code here.
	
def findMajorityElement(arr, n):  
    # Boyer-Moore Voting Algorithm  
    
    # Step 1: Find a candidate for majority element  
    candidate = None  
    count = 0  
    
    for num in arr:  
        if count == 0:  
            candidate = num  
        count += (1 if num == candidate else -1)  
    
    # Step 2: Verify if the candidate is indeed the majority element  
    if candidate is not None:  
        count = sum(1 for num in arr if num == candidate)  
        if count > n // 2:  
            return candidate  
    
    return -1  # If there is no majority element