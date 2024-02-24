def firstMissingPositive(self, nums: List[int]) -> int:
        n = max(nums)
        l = set(nums)
        # It was helped to you to get the all are negstive it will be return as 1 simply
        if n<0:
            return 1
        
        for i in range(1,n):
            if i not in l:
                return i
            else:
                l.remove(i)
        # All num in list are sequence then return max element +1 will be the answer
        return n+1