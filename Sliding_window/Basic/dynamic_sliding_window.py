'''
Write a function called minSubArrayLen which accepts two parameters —
an array of positive integers and a positive integer.

The function should return the minimal length of a contiguous subarray
of which the sum is >= intger passed in. If there isn’t one, return 0.


This is aka "minimum size subarray sum" from leetcode.com


1. In this type of sliding window problem, we increase our right pointer one by one till our condition is true.

2. At any step if our condition does not match, we shrink the size of our window by increasing left pointer.
Again, when our condition satisfies, we start increasing the right pointer and follow step 1.
We follow these steps until we reach to the end of the array.

3. We follow this step until the end here


https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''
from typing import List



'''
So the way you handle this problem is basically 

How to solve this problem here? So basically what happened was 


'''




def minSubarrayLength( target: int, nums: List[int]) -> int:
    # Initialize the length of the array
    length_of_nums = len(nums)
    # Set an initial answer value to a large number (beyond possible maximum)
    min_length = length_of_nums + 1
    # Initialize the sum of the current subarray and the start index j
    sum_of_subarray = start_index = 0
    # Loop over the elements in the array with their indices
    for end_index, value in enumerate(nums):
        # Add the current number to the sum of the current subarray
        sum_of_subarray += value
        # Shrink the subarray from the left (increase the start index)
        # until the sum is no longer greater or equal to the target
        while start_index < length_of_nums and sum_of_subarray >= target:
            # Update the minimum length if a shorter subarray is found
            min_length = min(min_length, end_index - start_index + 1)
            # Subtract the element at start_index from sum as we are excluding it from the subarray
            sum_of_subarray -= nums[start_index]
            start_index += 1
    # If min_length is updated, return it; otherwise, no such subarray exists and return 0
    return min_length if min_length <= length_of_nums else 0

# answer 1











