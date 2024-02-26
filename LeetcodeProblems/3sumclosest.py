# Two pointer approaches
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mindiff = float('inf')
        nums.sort()
        n = len(nums)
        ans = 0
        # 'i' is an iterator and elemnt in sum of targets
        for i in range(n):
            # Two pointers are working to getting the 
            j = i + 1
            k = n - 1

            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]

                if sum_val == target:
                    return target
                else:
                    diff = abs(target - sum_val)

                    if diff < mindiff:
                        mindiff = diff
                        ans = sum_val

                if sum_val < target:
                    j += 1
                elif sum_val > target:
                    k -= 1

        return ans