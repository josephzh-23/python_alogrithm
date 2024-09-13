def lower_bound(arr, val):
    lo, hi = 0, len(arr) - 1
    res = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == val:
            res = mid
            hi = mid - 1
        elif arr[mid] > val:
            hi = mid - 1
        else:
            lo = mid + 1
    return res