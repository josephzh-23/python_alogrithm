
# a list of integers here

# https://leetcode.com/problems/number-of-ways-to-split-array/description/
def prefixSum(nums):
    n = len(nums)
    prefix = [0] * n     # prefix

    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]











