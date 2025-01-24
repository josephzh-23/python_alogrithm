from Binary_Search.Basic.find_last_match import upper_bound


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
arr = [1, 2, 2,3,4, 5]
# print(lower_bound(arr, 2))
# print(upper_bound(arr, 2))
