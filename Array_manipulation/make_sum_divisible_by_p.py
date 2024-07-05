'''
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.



Find out where to cut the sub array here

we can quickly find out where to cut the subarray. If the current modulo value minus the target modulo value has been
seen before, the segment between that index and the current index could potentially be removed to satisfy the
problem's requirements.


2) If the sum modulo p equals k,

why do we need to mod it here? Because it could easily overflow so we take care of things here

3)


This is actually a prefix sum problem

'''
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Find the remainder of the sum of nums when divided by p
        remainder = sum(nums) % p
        # If the sum of nums is already divisible by p, the subarray length is 0
        if remainder == 0:
            return 0

        # Hash map to store the most recent index where a particular mod value is found
        mod_indices = {0: -1}
        # The current prefix sum mod p
        current_mod = 0
        # Initialize minimum length to the length of nums array
        min_length = len(nums)

        # Iterate through the numbers in the array to find the shortest subarray
        for index, num in enumerate(nums):
            # Update the current mod value
            current_mod = (current_mod + num) % p


            # Calculate the target mod value which would balance the current mod to make a divisible sum
            target_mod = (current_mod - remainder + p) % p

            # If the target mod value is found in the mod_indices
            if target_mod in mod_indices:
                # Update the min_length if a shorter subarray is found
                min_length = min(min_length, index - mod_indices[target_mod])
            # Update the mod_indices with the current index
            mod_indices[current_mod] = index

        # If min_length hasn't been updated, the required subarray doesn't exist
        return -1 if min_length == len(nums) else min_length























