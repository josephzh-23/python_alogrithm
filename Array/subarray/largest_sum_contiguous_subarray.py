'''
Input: arr = {-2,-3,4,-1,-2,1,5,-3}
Output: 7
Explanation: The subarray {4,-1, -2, 1, 5} has the largest sum 7.


The idea of Kadane’s algorithm is to maintain a variable

max_ending_here that stores the maximum sum contiguous
subarray ending at current index and a variable

max_so_far stores the maximum sum of contiguous subarray found so
far, Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if
it is greater than max_so_far.'''

def GFG(a, size):
    max_so_far = float('-inf')
    # Use float('-inf') instead of maxint
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
