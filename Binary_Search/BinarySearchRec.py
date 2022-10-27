# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binarySearchRec(arr, low, high, x):


    if low <= high:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearchRec(arr, low, mid - 1, x)

        else:
            return binarySearchRec(arr, mid + 1, high, x)

    else:
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearchRec(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")