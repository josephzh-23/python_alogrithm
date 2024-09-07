'''
We will try to do this with binary search here

'''


def binarySearch(A, low, high, searchKey):
    m = 0
    while (low <= high):
        m = (high + low) // 2
        # Check if searchKey is present at mid
        if (A[m] == searchKey):
            return 1
        # If searchKey greater, ignore left half
        if (A[m] < searchKey):
            low = m + 1
        # If searchKey is smaller, ignore right half
        else:
            high = m - 1
    # if we reach here, then element was
    # not present
    return 0


def checkTwoSum(A, arr_size, sum):
    # sort the array
    A.sort()
    l = 0
    r = arr_size - 1

    #  Traversing all element in an array search for searchKey
    i = 0
    while i < arr_size - 1:
        searchKey = sum - A[i]
        # calling binarySearch function
        if binarySearch(A, i + 1, r, searchKey) == 1:
            return 1
        i = i + 1

    return 0


a = [1, 4, 45, 6, 10, -8]
n = [4]
