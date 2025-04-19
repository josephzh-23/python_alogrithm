from typing import List

'''

we can use a stack to keep track of the indices of elements for which we haven't found the next greater number yet.


nums[stk[-1]] < nums[i %n ] 

    - found the next greter number for elem (index) at the top 
    
    Push the current index modulo the length of the array i % n onto the stack. This ensures we are in bounds of the array when the loop wraps around.
    
    
    Remember we need to circulate over this twice as said in the example here. 

'''


def nextGreaterElements(self, nums):
    """
    The above really makes sense here
    Finds the next greater element for each element in a circular array.

    :param nums: List[int] - List of integers where we need to find the next greater element for each.
    :return: List[int] - List containing the next greater elements.
    """
    # The number of elements in the input list.
    n = len(nums)

    # Initialize the result list with -1 for each element.
    result = [-1] * n

    # Stack to keep indexes of nums for which we haven't found the next greater element.
    stack = []

    # Iterate over the list twice to simulate circular array behavior.
    for i in range(2 * n):  # Shorthand for n << 1.
        # Get the index in the original nums array.
        index = i % n

        # While stack is not empty and the current element is > element at
        # the index of the last element in stack, update the result for the index at the
        # top of the stack.
        while stack and nums[stack[-1]] < nums[index]:
            result[stack.pop()] = nums[index]

        # For the first pass, we need to fill the stack with index.
        # Avoid pushing index onto the stack in the second pass to prevent duplicating work.
        if i < n:
            stack.append(index)

    # Return the result list containing next greater elements.
    return result
