'''
Write a function called minSubArrayLen which accepts two parameters —
an array of positive integers and a positive integer.

The function should return the minimal length of a contiguous subarray
of which the sum is greater
 than or equal to the intger passed in. If there isn’t one, return 0.


This is aka "minimum size subarray sum" from leetcode.com


1. In this type of sliding window problem, we increase our right pointer one by one till our condition is true.

2. At any step if our condition does not match, we shrink the size of our window by increasing left pointer.
Again, when our condition satisfies, we start increasing the right pointer and follow step 1.
We follow these steps until we reach to the end of the array.

3. We follow this step until the end here


https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''

def minSubArraySize(arr, num):

    # keep track of smallest subarray length
    sum, l, r, minLen = 0, 0, 0, float('inf')

    while (l < len(arr)):
        '''
        if window's leading edge has NOT reached the end of the array
        AND window's values do NOT add up to num, grow window to right
        '''
        if r < len(arr) and sum < num:
            sum += arr[r]
            r+=1
        elif sum >= num:
            '''
            
            '''
            minLen = min(minLen, r - l)

            # decrease the sum by value at the window trailing edge here
            sum -= arr[l]
            l+=1
        else:
            break

    return 0 if minLen == float('inf') else minLen















