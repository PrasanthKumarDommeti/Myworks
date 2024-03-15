class Solution:
    def jump(self,nums:List[int])->int:
        # This can be solved by using the 2 pointers approache
        start,end,count=0,0,0
        # iterate over the last value 
        for i in range(len(nums)-1):
            # Calculate the max value to minimize the steps
            start=max(start,i+nums[i])
            # Incase the zero has been occured the value must be change and increament count with 1
            if end==i:
                end=start
                count+=1
        return count
    
       