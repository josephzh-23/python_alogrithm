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
from typing import List



'''
So the way you handle this problem is basically 

How to solve this problem here? So basically what happened was 


'''


def minSwaps(data: List[int]) -> int:
    N = len(data)
    all_ones_count = sum(data)          # all_ones_count never changes

    left = 0
    right = 0
    print(all_ones_count)
    ones_in_window = 0
    max_ones = 0


    '''
    Imagine you have [1, 1, 0, 1, 1, 1, 1] to fix the above you would need 
   What you are doing is basically 
   1) at one pt, r = 6, one_in_window = 5, 
   2) since r >= all_ones_count , we start contracting
       ->  [1, 0, 1, 1,1, 1] and we exit 
       
       
   3) Add data[right],      [ 1, 0, 1, 1, 1, 1], 
   becomes [1, 0, 1, 1, 1, 1] and then [0, 1, 1, 1,1 ]
    but the max_ones becomes 6 at some point in this process
    '''
    while right < N:
        ones_in_window += data[right]
        right += 1

        if right >= all_ones_count:
            max_ones = max(max_ones, ones_in_window)
            ones_in_window -= data[left]
            left += 1

            # in this case becomes 6 - 5
    return all_ones_count - max_ones
# minSubArrayLen(data)
# minSubArrayLen(data)
data = [1, 1, 0, 1, 1, 1, 1]
print(minSwaps(data))

# answer 1











