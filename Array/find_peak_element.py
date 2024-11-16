'''

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.



Strickly greater than its neighbor
'''
from typing import List


def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        '''
        If nums[mid] is greater than nums[mid + 1],
         the peak must be at mid or to the left of mid. Thus, we set right to mid, effectively narrowing the search interval to the left half.
        
        '''
        if nums[mid] > nums[mid + 1]:
            right = mid

            '''
            
            if nums[mid] is less than or equal to nums[mid + 1], then a peak lies to the right. Thus, we set left to mid + 1, narrowing the search interval to the right half.
            '''
        else:
            left = mid + 1
    return left