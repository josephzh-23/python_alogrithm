# remove duplicate


'''
Need 2 pointers i and j
i for iterating
j for placing the next non-duplicate number

2   2   2   1       The old array
2   1               The new array

Will return the number of non-duplicate values here
'''
from typing import List


def removeDup(nums:List[int]) ->int:
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1

    print(nums)
    return l
arr = [1, 2, 2, 2, 3]
removeDup(arr)