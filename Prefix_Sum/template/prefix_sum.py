
# a list of integers here

# https://leetcode.com/problems/number-of-ways-to-split-array/description/


'''


Why is prefix sum important?
array = [1, 2, 2, 3]
Because imagine  prefix = [1, 3, 5, 7]

For example:
And then prefix[10] - prefix[2] = sum of subarray from 3 to 10 here
nums[3] + .... + nums[10]

'''
# when do we use a contiguous array since the solution is prefix sum here
def prefixSum(nums):
    n = len(nums)
    prefix = [0] * n     # prefix
    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix










