def find_last_smaller_equal(arr, target):

    low, high = 0, len(arr) - 1

    result = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] <= target:

            result = mid

            low = mid + 1

        else:

            high = mid - 1

    return result



# Example usage

array = [2, 5, 8, 10, 12, 15]

target = 11

index = find_last_smaller_equal(array, target)

# print(f"Last value smaller or equal to {target} is: {array[index]} (at index {index})")