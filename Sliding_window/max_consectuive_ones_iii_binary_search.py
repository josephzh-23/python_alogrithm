'''

Do prolbem
Given a binary array nums and an integer k, return the maximum number of consecutive

1's in the array if you can flip at most k 0's.

'''

def maxConsecOnesIII(nums):
    n = len(nums)
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]
    return prefix