'''

Try to revisit a problem as well
Idea is abasillcay

Calculating Area: When we encounter a bar shorter than the one at the top of the stack, we pop the stack.
The height
of our potential rectangle is the height of the bar at the popped index.
The width is determined by the difference
between the current index and the new top of the stack.

The area =
(i−stack[top−1]−1)×heights[stack[top]].

When we reach the end then:
(heights.length−stack[top−1]−1)×heights[stack[top]]

'''
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] # pair [index, height]

    for i, h in enumerate(heights):

        # keep most up to date starting point here
        start = i
        # while it's still greater than the cur height
        while start and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height* (i - index))
            start = index

        stack.append((start, h))


    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) -i))
    return maxArea

largestRectangleArea([2, 1, 5, 6, 2, 3])
