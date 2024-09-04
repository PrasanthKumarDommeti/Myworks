def firstAndLastPosition(arr, n, k):
   

    # Write your code here
    def bst(arr,n,k,bias):
        low = 0
        high = n-1
        i=-1
        while low <=high:
            mid = (low+high)//2
            if k<arr[mid]:
                high = mid-1
            elif k>arr[mid]:
                low = mid+1
            else:
                i=mid
                if bias:
                    high=mid-1
                else:
                    low = mid+1
        return i

    left = bst(arr,n,k,True)
    right = bst(arr,n,k,False)
    return [left,right]

    


	 
