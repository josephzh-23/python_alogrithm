"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
from String_Array.findMode import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Starting with the first value
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)

            # if the sum is negative at any point, then make it bigger
            if total < 0:
                total = 0
        return res
