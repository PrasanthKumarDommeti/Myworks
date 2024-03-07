class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for num in nums:
            # Checking the elemt and sorted element must be greter th
            if i<1 or num>nums[i-1]:
                nums[i]=num
                i+=1
        return i
        
        

        