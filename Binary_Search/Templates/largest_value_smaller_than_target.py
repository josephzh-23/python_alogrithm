'''

This is for the case when the target value may not exist in the list, and we need to find the largest value which is smaller than the target value. The logic would be:

If the found value is larger than the target, we need to continue search on the left side.
If the found value is the same as the target, we can return the index directly.
If the found value is smaller than the target, we can store this index, as it can be a possible result. Then continue searching on the right side.
Below is the sample code in Python.

'''
def largest_samller(arr, val):
    lo, hi = 0, len(arr) - 1
    res = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > val:
            hi = mid - 1
        elif arr[mid] < val:
            res = mid
            lo = mid + 1
        else:
            return mid
    return res