
'''

How to deal with this problem here?

And then using this we have the code
- use a hashmpap

to find the sum that we see along the way here

Find the # of times that

1. This is key here:
we attempt to find the number of times the complement of the current cumulative sum,
(s - k), has already appeared.

2.

'''
from collections import Counter, defaultdict
from typing import List


def subarraySum(self, nums: List[int], k: int) -> int:
    # Initialize a counter to keep track of the cumulative sums encountered
    cumulative_sum_counter = Counter({0: 1})

    # 'count_subarrays' will store the total count of subarrays that sum up to 'k'
    count_subarrays = 0

    # 'cumulative_sum' holds the sum of numbers seen so far
    cumulative_sum = 0

    # Iterate through the list of numbers
    for num in nums:
        # Update the cumulative sum
        cumulative_sum += num

        # If there is a previous cumulative sum such that current_sum - k
        # is equal to that previous sum, then a subarray ending at the current
        # position would sum to 'k'
        count_subarrays += cumulative_sum_counter[cumulative_sum - k]

        # Increase the count of the current cumulative sum by 1 in the counter
        cumulative_sum_counter[cumulative_sum] += 1

    # Return the total number of subarrays that sum up to 'k'
    return count_subarrays
