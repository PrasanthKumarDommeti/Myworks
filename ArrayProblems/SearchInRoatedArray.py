class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            # If target is present then return the index else return -1
            if nums[i]==target:
                return i
        return -1
        