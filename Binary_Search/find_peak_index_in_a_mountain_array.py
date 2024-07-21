from typing import List


def peakIndexInMountainArray(self, arr: List[int]) -> int:

    '''

    If arr[mid] < arr[mid + 1],  we move to the upper half of the range by setting l = mid + 1 as our peak index is
    definitely greater than mid

    '''
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < arr[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l