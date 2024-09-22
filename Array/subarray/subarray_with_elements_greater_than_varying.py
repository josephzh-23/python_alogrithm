from typing import List
'''
What's the solution here as said before we can have here is basically here 




'''

def validSubarraySize(self, nums: List[int], threshold: int) -> int:
    # Find the length of the array
    n = len(nums)

    # Initialize arrays to keep track of the closest smaller element's index to the left and right
    left_smaller_indices = [-1] * n
    right_smaller_indices = [n] * n

    # Initialize an empty list to use as a stack
    stack = []

    # Forward pass to find the left smaller elements for each index
    for i, value in enumerate(nums):
        # Remove from stack all elements larger than or equal to current
        while stack and nums[stack[-1]] >= value:
            stack.pop()
        # If stack is not empty, update left smaller index for current element
        if stack:
            left_smaller_indices[i] = stack[-1]
        # Add current index to stack
        stack.append(i)

    # Clear stack to reuse it for the backward pass
    stack.clear()

    # Backward pass to find the right smaller elements for each index
    for i in range(n - 1, -1, -1):
        # Remove from stack all elements larger than or equal to the current
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        # If stack is not empty, update right smaller index for current element
        if stack:
            right_smaller_indices[i] = stack[-1]
        # Add current index to stack
        stack.append(i)

    # Iterate over the array elements to find the valid subarray
    for i, value in enumerate(nums):
        # Calculate the length of the subarray where the current element is the minimum
        k = right_smaller_indices[i] - left_smaller_indices[i] - 1
        # Check if this element's value is greater than the threshold divided by the subarray size
        if value > threshold // k:
            # If so, this is a valid subarray size, return it
            return k

    # If no valid subarray is found, return -1.
    return -1
