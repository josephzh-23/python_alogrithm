'''

Every elem appears only once here,

Can only appear once here
'''
from typing import List


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif x< arr[mid]:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1



# if we want to perform this here then we have the code

def singleNonDuplicate(nums:List[int]):
    length = len(nums) -1
    for (x, i) in enumerate(nums):
        if not binary_search(nums, i,length, x):
            binary_search(nums, i + 1, length, x)
        else:
            break









