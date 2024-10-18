'''

https://leetcode.com/problems/reverse-pairs/description/
'''


def countPairs(arr, left, mid, right):
    count, j = 0, mid + 1

    # iterate over the left half and count the valid reverse pairs

    for i in range(left, mid):

        # the one here makes a lot of sense here
        while i<=right and arr[i] > arr[j] * 2:
            j+=1

            # add the # of reverse paris foudn
    # and then using the pair porgramming from before does maek

# function to merge the 2 subarrayehere
def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    # and these are the starting points here
    leftArr = len(n1) * [0]
    rightArr = len(n2) * [0]

    # copy the left half of the array into left arr
    for i in range(n1):
        leftArr[i] = arr[l + i]

    # copy the right half into the rightArr
    for i in range(n2):
        rightArr[i] = arr[mid + 1 - i]

    i, j, k = 0, 0, l

    # merge the left and right into the original array
    while (i < n1 and j < n2):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1;

    # copy any remaining elements from the left array
    while (i < leftArr.length):
        arr[k] = leftArr[i];
        i += 1
        k += 1

    # copy anything left from the right array here

    while (j < rightArr.length):
        arr[k] = rightArr[j];
        j += 1
        k += 1
