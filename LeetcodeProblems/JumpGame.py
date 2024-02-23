def canJump(self, nums: List[int]) -> bool:
    s=0
     
    for i in nums:
        if s<0:
            return False
        elif i>s:
            s=i
        s-=1
    return True

input : [2,3,1,1,4]
output : True