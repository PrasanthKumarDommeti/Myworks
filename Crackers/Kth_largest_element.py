from os import *  
from sys import *  
from collections import *  
from math import *  

from sys import stdin, stdout  

def kthLargest(arr, size, k):  
    # Sort the array in descending order  
    arr.sort(reverse=True)  
    
    # Get the k-th largest element (k is 1-indexed)  
    return arr[k-1]  

# Taking input using fast I/0  
def takeInput():  
    N, K = list(map(int, stdin.readline().strip().split(" ")))  
    arr = list(map(int, stdin.readline().strip().split(" ")))  
    return N, K, arr  

tc = int(input())  
while tc > 0:  
    N, K, arr = takeInput()  
    stdout.write(str(kthLargest(arr, N, K)) + "\n")  
    tc -= 1