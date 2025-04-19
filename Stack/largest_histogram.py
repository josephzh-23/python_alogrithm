'''

Workgin on this example right here means a lot
These 2 are very important for now here

left[i] will store the index of the first bar to the left that is shorter than height[i],

 and right[i] will store the index of the first bar to the right that is shorter than height[i].

 Non-decreasing stack

 For each bar h with index i:

1. We pop from the stack while the bar at the top of the stack has a height greater than or equal to h. Each time we pop, we update the right bound for the popped index because we just found a shorter bar on the right.

2. If the stack is not empty after popping, it means the bar on the top of the stack is the first bar to the left of h that is shorter, so we update the left[i] to that index.

We then push i onto the stack, since it might be the potential left bound for a future bar.


'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Get the total number of bars in the histogram
        num_bars = len(heights)

        # Initialize stacks for indexes of bars
        stack = []

        # Initialize arrays to record the first smaller bar on the left of each bar
        smaller_left_index = [-1] * num_bars

        # Initialize arrays to record the first smaller bar on the right of each bar
        smaller_right_index = [num_bars] * num_bars

        # Iterate over all heights to compute the smaller_left_index and smaller_right_index
        for index, height in enumerate(heights):

            # Pop elements from the stack while the current height is less than
            # the top element's height in the stack to find the right boundary
            while stack and heights[stack[-1]] >= height:
                smaller_right_index[stack[-1]] = index
                stack.pop()
            # If the stack is not empty, the current element at the top is the previous
            # bar of smaller height (left boundary)
            if stack:
                smaller_left_index[index] = stack[-1]
            # Push this bar onto stack
            stack.append(index)

        # Calculate the maximum area of rectangle in histogram
        max_area = 0
        for i, h in enumerate(heights):
            # Update max_area with the larger area found
            max_area = max(max_area, h * (smaller_right_index[i] - smaller_left_index[i] - 1))

        return max_area