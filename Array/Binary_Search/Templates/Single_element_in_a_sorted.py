

'''

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2




We want to remove the half every time we search here

If we have

1, 1, 2, 3, 3, 4, 4

Which side would we look from?

We should look for in the side with the odd number here


1  1  2  3  3  4  4
l        m        r

1  1  2  3  3  4  4
l  m  r

'''
from typing import List


def singleNonDuplicate(nums: List[int])-> int:

    l, r = 0, len(nums) -1
    while l <= r:
        m = l +  (r - l ) // 2
        # making sure not out of bounds
        if ((m -1 ) < 0 or nums[m - 1] != nums[m]) and ((m + 1 == len(nums) or nums[m + 1])):
            return nums[m]