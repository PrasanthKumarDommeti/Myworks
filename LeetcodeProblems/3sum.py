#Brute Force approaches
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set has no duplicates that why we using set datastructure
        ans=set()
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=nums[i]+nums[j]+nums[k]
                    if temp==0:
                        ans.add((nums[i],nums[j],nums[k]))
        return ans