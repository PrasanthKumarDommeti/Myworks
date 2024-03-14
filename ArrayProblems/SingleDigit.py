class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c= Counter(nums)
        # Itterarte over through the frequencies
        for key,value in c.items():
            # Single valued frequency occured
            if value ==1: 
                #return key
                return key