"""

Greedy like algorithm behind it here

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

cur_subarray
max_subarray
i = 0
-2 not worth keeping, so skip it here

i = 1
cur_subarray = 1
max_subarray = 1

i = 2
cur_subarray = -2
max_subarray = 1

i = 3
-2 (cur_subarray) prior not worth keeping here
cur_subarray = 2
max_subarray = 4

and the above is what we expected from this equation so far here and that's very important so far here



"""
from String.String_Array.findMode import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray