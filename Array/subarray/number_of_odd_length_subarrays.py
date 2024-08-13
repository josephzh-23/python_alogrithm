from typing import List
'''

This is the follow up problem from sum of odd length arrays
'''

def numOddLengthSubarrays( arr: List[int]) -> int:
    n = len(arr)
    answer = 0

    numOfOddLengthArray= 0
    # get the number of subarrays first here

    for left in range(n):
        for right in range(left, n):
            if (right - left + 1) % 2 == 1:
                numOfOddLengthArray+=1

    print(numOfOddLengthArray)