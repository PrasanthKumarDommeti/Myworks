def maxSubarray(nums):
    if len(nums)==1:
        return nums[0]
    meh = 0 # minimum ended here
    msf = -sys.maxsize-1 #max so far
    for i in range(len(nums)):
        meh = meh+nums[i]
        if meh < nums[i]:
            meh = nums[i]
        if msf < meh:
            msf = meh
    return msf

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))

# output : 6
