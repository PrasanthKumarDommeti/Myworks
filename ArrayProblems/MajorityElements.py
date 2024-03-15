class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        m=0
        # Calculate the max values occured in the values
        for key, value in c.items():
            m = max(m,value)
        # Calaculate the matched maxmum values with the occurenced values and return corresponding key 
        for key,value in  c.items():
            if value == m :
                return key
