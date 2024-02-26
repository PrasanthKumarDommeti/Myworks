# Brute-force Solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            #we can elemenate the duplicates using tuple
                            ans.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
        
        res = []
        for i in ans:
            res += list(i),
        return res