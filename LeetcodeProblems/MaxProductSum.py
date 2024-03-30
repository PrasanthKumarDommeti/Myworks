class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minp = maxp = 1
        res = nums[0]
        for i in nums:
            # If the element is negeative then swap the element
            if i<0:
                maxp,minp = minp,maxp
            # You can calculate the min & max of the values
            maxp = max(maxp*i,i)
            minp = min(minp*i,i)
            # If you want the product then we can return max value
            res = max(res,maxp)
        return res
