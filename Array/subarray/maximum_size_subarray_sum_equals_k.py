'''
Another important concept here

Given an integer array nums and an integer k

return max length of a subarray that equals sum here
'''



def maxSizeSubarraySumEqualsK(nums, k):
    '''
    1) Say you want to find k, then find prefix[i] - k, (the complement remember two sum)
    if yes, then we found a pair of indices for a subarray with sum k.

    2) Use map to store {index: prefixSum}

        ! update the index when you see duplicate (u want longest, not shortest)

    '''
    map = {}
    longestSubarray = 0
    prefixSum = 0
    for i, n in enumerate(nums):
        prefixSum += n

        # condition 1:
        # if prefixSum == k:, that means the sum of the array up to this index is equal to k
        # i is 0 based
        if prefixSum == k:
            longestSubarray = i + 1

        # If prefixSum - k exists in indices,
        # that means there is already a subarray with sum k ending at the current i,
        # we need to update this like there is no tomorrow

        # This is the catch here
        if prefixSum - k in map:

            longestSubarray = max(i- map[prefixSum - k], longestSubarray )

        if prefixSum not in map:
            map[prefixSum] = i
    print(longestSubarray)
    return longestSubarray

maxSizeSubarraySumEqualsK([1,-1,5,-2,3],  3)
