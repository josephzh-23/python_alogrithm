'''
The same as maximum_subarray_sum_equals_k problem here

Init a prefix_sum = 0 and maxLen = 0 here,

Create a hash table having (prefix_sum, index) tuples.

The steps:

1. Accumulate arr[i] to prefix_sum.
2. If prefix_sum == k, update maxLen = i+1.

3. Check whether prefix_sum is present in the hash table or not.
 If not present, then add it to the hash table as (prefix_sum, i) pair.

 4. Prefix sum -k: is the complement here
Check if (prefix_sum-k) is present in the hash table or not. If present,

If prefixSum - k already exists, then
hat means there is a subarray with sum k ending at the current i.
 The length will be i - indices[prefixSum - k]

 5.
'''
from Prefix_Sum.template.prefix_sum import prefixSum


def longestSubarraySumEqualsK(nums, k):

    # an integer prefix sum that keeps track of the cur sum
    prefix = 0

    # at the start everything is 0 here
    longestSubarray = 0
    # { first index: prefix sum here }
    indices = {}


    prefix = prefixSum(nums)

    for (i, num) in enumerate(nums):

        if prefix[i] == k:
            longestSubarray = i + 1

        # we have already seen the complement of the prefix
        if prefix[i] - k in indices:

            # the following is important here
            longestSubarray = max(longestSubarray, i - indices[prefix - k])

        if prefix[i] not in indices:
            indices[prefix[i]] = i

    return longestSubarray










