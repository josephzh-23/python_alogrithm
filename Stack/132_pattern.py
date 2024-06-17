'''


This is the first problem here , and then the brute force way here

Monotonic stack problem
[3, 1, 4, 2]
- maintain the minimum value that came before the stack value here
stack : n: [3, 1, 4]
min:   3   3   1

It's ok if just removing some smaller values here,
n[k] the most flexibility here and then once u reach the end
and you can return false if not returning true or not here

- 2 ^ n solutino here

'''
from typing import List


def find132Pattern(nums: List[int])-> bool:

    stack = []
    curMin = nums[0]

    for n in nums[1:]:
        while stack and n >=stack[-1][0]:
            stack.pop()

        '''
        Check if a value > n that came before it and 
        n > the min value that came before stack[-1][0] 
        '''
        if stack and n < stack[-1][0] and n >stack[-1][1]:
            return True

        stack.append([n, curMin])
        # this is used to expand the range here
        curMin = min(curMin, n)

    return False








