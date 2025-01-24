def find_first_smaller_or_equal(arr, target):
    low = 0

    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] > target:

            high = mid - 1

        else:

            low = mid + 1

    if low > 0 and arr[low - 1] <= target:

        return low - 1

    else:

        return None  # No value found