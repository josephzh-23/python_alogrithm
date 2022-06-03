
# O log (n)
# Best case: O (1)


def linearSearch(arr, x):
    l = 0
    while x!= arr[l]:
        l += 1


# Return the index here
def binarySearch(arr, x):
    l = 0
    r = len(arr) - 1

    while (l <= r):

        # Use this to round down
        m = (r + l) // 2

         # If x greater, ignore left half
        if arr[m] < x:
            l = m + 1

        # If x is smaller, ignore right half, update right pter
        elif arr[m] >x :
            r = m - 1

        else:
            return m
    return -1


if __name__ == '__main__':
    arr = ["joe", "suryadi", "tyler"]
    x = "ry"

    result = binarySearch(arr, x)

    if result == -1:
        print("sorry nothing found")
    else:
        print("found at position ", result)


