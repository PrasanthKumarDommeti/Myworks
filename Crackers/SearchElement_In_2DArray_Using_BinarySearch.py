def searchMatrix(arr: [[int]], target: int) -> bool:  
    if not arr or not arr[0]:  
        return False  
    
    M = len(arr)      # number of rows  
    N = len(arr[0])   # number of columns  
    
    left, right = 0, M * N - 1  # Search space as a linear array  

    while left <= right:  
        mid = (left + right) // 2  
        mid_value = arr[mid // N][mid % N]  # Translate mid to 2D index  
        
        if mid_value == target:  
            return True  
        elif mid_value < target:  
            left = mid + 1  
        else:  
            right = mid - 1  
            
    return False  

