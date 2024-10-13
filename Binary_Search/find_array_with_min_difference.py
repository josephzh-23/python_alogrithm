'''
Find the value which has the smallest difference with the target value here
And basically this is important

The difference with the other algorithms is, when we continue search on left side or right side, we need to include the current index.

We keep searching until we have less than or equal to
two possible indexes left. Then we find the value between the two.


'''
def min_diff(arr, val):
    lo, hi = 0, len(arr) - 1
    while lo < hi-1:
        mid = lo + (hi - lo) // 2
        if arr[mid] > val:
            hi = mid
        else:
            lo = mid
    if abs(arr[lo] - val) <= abs(arr[hi] - val):
        return lo
    return hi