from _testcapi import INT_MIN

'''
Brute force on how to find the maximum sum of an array of given size k
1. This corresponds to the fixed sliding window 

2.

'''
def maxSum(arr, n, k):

    # Initialize result
    max_sum = INT_MIN

    # Consider all blocks
    # starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]

        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4
n = len(arr)