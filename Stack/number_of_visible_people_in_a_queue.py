'''
Interesting problem here

From 0 to n -1, array of heights height[i] : simple enough here
then
[10, 6, 8, 5, 11, 9]

Build arr

'''
'''
A person to the right of a taller person will never be seen by anyone other than this taller person. So we'll
record their contribution to the taller person (comment 1).

A person to the left of a taller person will never see anyone but this taller person. So we'll
record that
they've seen this one person and get rid of them since they've already made their contribution (comment 2).

'''
from typing import List


def canSeePersonsCount(heights: List[int]) -> List[int]:
    # used to store the index here
    stack = []
    ans = [0] * len(heights)

    for i in range(len(heights)):

        '''
        The cur height of person > then the person in stack 
        '''
        while stack and heights[i] > heights[stack[-1]]:
            # and then here when popped the
            popped = stack.pop()
            print('popped is' , popped)
            ans[popped] += 1

        '''

        '''
        if stack:
            print('the last index is', stack[-1])
            # (1) contributing to the taller person
            ans[stack[-1]] += 1
        stack.append(i)

    return ans


print("Monotonic increasing stack:")

heights = [10, 6, 8, 5, 11, 9]
print(canSeePersonsCount(heights))
