'''

A range a set from a to b here

'''
from typing import List



'''
Here it becomes [0, 1, 2, 4, 5, 7] here and then 

[0 -> 2, 4-> 5 
'''
def summaryRanges(nums: List[int]) -> List[str]:
    ranges = []
    i = 0

    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1

        if start != nums[i]:
            ranges.append(str(start) + "->" + str(nums[i]))
        else:
            ranges.append(str(nums[i]))

        i += 1

    return ranges