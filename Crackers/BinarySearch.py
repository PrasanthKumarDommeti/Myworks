from typing import *

def binarySearch(arr : List[int], n : int, x : int) :
    
  
    left = 0  
    right = n - 1  
    
    while left <= right:  
        mid = left + (right - left) // 2  
        
        # Check if x is present at mid  
        if arr[mid] == x:  
            return mid  # Return the index of the found element  
        # If x is greater, ignore the left half  
        elif arr[mid] < x:  
            left = mid + 1  
        # If x is smaller, ignore the right half  
        else:  
            right = mid - 1  
            
    # Element is not present in the array  
    return -1  


