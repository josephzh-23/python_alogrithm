

# this program is for swapping 0 and 1s only
# using sliding window technique

def minSwap(arr, n):
    minSwap, idx, temp = 0, 0, 0
    while idx< len(arr):

        # arr[0] != 1 need swap
        if arr[idx] != idx + 1:
            temp = arr[idx]
            arr[idx] = arr[arr[idx] -1]

            arr[temp -1] = temp