'''
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Write a function called minSubArrayLen which accepts two parameters —
an array of positive integers and a positive integer.

The function should return the minimal length of a contiguous subarray
of which the sum is >= intger passed in. If there isn’t one, return 0.


This is aka "minimum size subarray sum" from leetcode.com





'''
from typing import List



'''

What are the 3 key components here?

1. A for loop 
2. A while loop inside there
3. res = min(res, right - left + 1) some conditino for updating here 
'''
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    right = 0
    sumOfCurrentWindow = 0


    res = float('inf')

    for right in range(0, len(nums)):
        sumOfCurrentWindow += nums[right]

        while sumOfCurrentWindow >= target:
            res = min(res, right - left + 1)
            sumOfCurrentWindow -= nums[left]
            left += 1

    return res if res != float('inf') else 0
