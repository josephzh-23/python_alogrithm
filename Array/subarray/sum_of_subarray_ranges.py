'''


How to find the max and min of each subarray sum here this is important here

The basic solution is here
max_i - min_ i = range_i
max_i+1 - min_i+1 = range_i+1

- Sum (max) - Sum (min) = sum (range)


How to find the range and the number here

Part 1 here:
Sum of subarray minimum is basically

1. prevSmaller, nextSmaller


l = left index of the smaller elem (prevSmaller)
r  = right index of the smaller elem  (nextSmaller)

Solution: (i - l) * (R - i)


Part 2:
And then we have to do the same for nextGreater and prevGreater here

-


'''

from typing import List


def subArrayRanges(nums: List[int]) -> int:
    n = len(nums)

    stack = []
    nextSmaller = [n] * n
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            nextSmaller[stack.pop()] = i
        stack.append(i)

    stack.clear()
    prevSmaller = [-1] * n
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            prevSmaller[stack.pop()] = i
        stack.append(i)

    stack.clear()
    nextGreater = [n] * n
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            nextGreater[stack.pop()] = i
        stack.append(i)

    stack.clear()
    prevGreater = [-1] * n
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            prevGreater[stack.pop()] = i
        stack.append(i)


    print("the stacks are ", nextSmaller, prevSmaller)
    ret = 0
    for i in range(n):
        l = prevGreater[i]
        r = nextGreater[i]
        ret += nums[i] * (i - l) * (r - i)
    for i in range(n):
        l = prevSmaller[i]
        r = nextSmaller[i]
        ret -= nums[i] * (i - l) * (r - i)
    return ret



print(subArrayRanges([1, 2, 3]))