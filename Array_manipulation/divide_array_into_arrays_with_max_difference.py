'''


'''
from typing import List


def divideArray(nums: List[int], k: int) -> List[List[int]]:
    # Sort the input array to make sure that subarrays with a maximum size difference of k can be found.
    nums.sort()
    # Initialize an empty list to store the resulting subarrays.
    divided_arrays = []
    # Calculate the length of the input list.
    nums_length = len(nums)

    # Iterate over the array in steps of 3, as we want subarrays of size 3.
    for i in range(0, nums_length, 3):
        # Generate a subarray of size 3 from the sorted list.
        subarray = nums[i: i + 3]

        # Check if the subarray has 3 elements and the maximum size difference condition holds.
        # If not, return an empty list as the condition cannot be met.
        if len(subarray) < 3 or subarray[2] - subarray[0] > k:
            return []

        # If the condition is met, add the valid subarray to the result list.
        divided_arrays.append(subarray)

    # Return the list of all valid subarrays after iterating through the entire input list.
    return divided_arrays
