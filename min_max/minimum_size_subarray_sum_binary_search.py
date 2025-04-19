'''

First, a prefix sum array v is built where v[i] represents the sum of the subarray from the
 start to the i-th index.
 This allows quick calculation of the sum of any subarray by subtracting two prefix sums.


For each index i, we want to find the largest subarray ending at i


whose sum is >=  to the target. To do this efficiently,

 we use binary search on the prefix sum array.
If v[i] (the sum of the array from 0 to i) is >= target, we calculate
how much we need to subtract from v[i] to make the remaining sum at least the target. This subtraction forms the search target, and binary search helps to quickly find the right subarray.

The binary search (bs function) looks for the largest index where the prefix sum is less than or equal to v[i] - target. This gives the left boundary of the desired subarray.

Edge Cases:
If the entire array sum is less than the target (v[n-1] < target), return 0 because it's impossible to find such a subarray.
If any individual prefix sum is greater than or equal to the target, update the minimum subarray length.


'''
import bisect

from Prefix_Sum.template.prefix_sum import prefixSum


def minSubArrayLength(target, nums):

    n = len(nums)
    v = prefixSum(nums)

    print(v)


    if (v[n - 1] < target):return 0;
    if (v[0] >= target):return 1;

    mini = n

    for i in range(n):

        '''
        The binary search (bs function) looks for the largest index where the prefix sum is less than or equal to v[i] - target. This gives the left boundary of the desired subarray.
        '''
        if v[i] >= target:
            mini = min(mini, i + 1)
            ind = bisect.bisect_left(v, i -1, v[i] - target)




minSubArrayLength(5,  nums = [2,3,1,2,4,3])