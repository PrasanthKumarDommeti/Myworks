from os import *
from sys import *
from collections import *
from math import *



def firstNonRepeatingCharacter(s):  
    # Use a dictionary to count the occurrences of each character  
    frequency = {}  
    for char in s:  
        if char in frequency:  
            frequency[char] += 1  
        else:  
            frequency[char] = 1  
            
    # Step 2: Find the first unique character  
    for char in s:  
        if frequency[char] == 1:  
            return char  
            
    # Step 3: If no unique character found, return the first character  
    return s[0]  
  

