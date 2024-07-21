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

def minSubArraySize(fruits, num):

    # keep track of smallest subarray length
    sum, l, r, minLen = 0, 0, 0, float('inf')
    count = dict()

    # the above is the solution that we had before much better
    # much better solution than before

    total = 0
    while r < len(fruits):
        '''
        Increase the frutis anyways at this point and hten 
        '''
        count[fruits[r]] +=1

        # increase the l
        while len(count) > 2:
            f = fruits[l]

            count[f]-=1
            total -=1
            l+=1
            if not count[f]:
                count.pop(f)

    return 0 if minLen == float('inf') else minLen















