import math as mt
  
def mostFrequent(arr, n):
  
    # Insert all elements in Hash.
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1
  
    # find the max frequency
    max_count = 0
    res = -1
    for i in Hash: 
        if (max_count < Hash[i]): 
            res = i
            max_count = Hash[i]
          
    return max_count
  
t = int(input())
for i in range(t):
    n = int(input())
    x= list(map(int, input().split()))
    print(n-mostFrequent(x, n))