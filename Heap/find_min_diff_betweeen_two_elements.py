'''

Given an unsorted array, find the minimum difference between any pair in the given array.
Input: {1, 5, 3, 19, 18, 25}
Output: 1
Explanation: Minimum difference is between 18 and 19


Can be done with map here
'''

def findMinimum(arr):
    arr = sorted(arr)
    minDiff = 0
    for i in range(1, len(arr)):
        if (arr[i]- arr[i- 1] < minDiff):
            minDiff = arr[i] - arr[i-1]
        return minDiff













