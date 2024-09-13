'''

1- Design and implement a divide and conquer algorithm for finding a position of the
largest number in an array of n numbers.
For example, if the input array A[1..9] = [2,5,8,3,6,9,1,6,5],

your algorithm should return 6. [4 mark]
'''

'''
If using Divide conquer, use the following approach

n = # of elements to be counted in array
'''


def count(arr, x, n):
    i = first(arr, 0, n - 1, x)

    # If x doesn't exist in
    # arr[] then return -1
    if i == -1:
        return i
    # Notice here we are only looking at the index
    # after the index i that we find
    j = last(arr, i, n-1, x, n)

    # then return the count
    return j-i+1

# This represents modified version of binSearch
def first(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        midVal = arr[mid]

        if (mid == 0 or x > arr[mid - 1]) and midVal == x:
            return mid

        elif x > midVal:
            first(arr, mid + 1, high, x)
        else:
            first(arr, low, mid - 1, x)

    else:
        return -1


# if x is present in arr[] then return
# the index of LAST occurrence of x
# in arr[0..n-1], otherwise returns -1
def last(arr, low, high, x, n):
    if high >= low:

        # low + (high - low)/2
        mid = (low + high) // 2

        if (mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)
    return -1
# driver program to test above functions
arr = [1, 2, 2, 3, 3, 3, 3]
x = 3  # Element to be counted in arr[]
n = len(arr)
c = count(arr, x, n)
print ("%d occurs %d times "%(x, c))