'''


Random pick with weight

1. Leetcode here
Convert into a range of cumulative sum

2.Have the weight of each index as a range in the cumulative sum

3. Use a binary search on the prefix sum array here to find the
smallest prefix sum >= what we are looking for here




Probablility is w[i] / sum(w)
'''
import random
from typing import List


class Solution:
    def __init__(self, weights: List[int]):

        # Initialize an empty list to store cumulative weights
        self.cumulative_weights = [0]
        # Build up the cumulative weight list for later binary search
        for weight in weights:
            self.cumulative_weights.append(self.cumulative_weights[-1] + weight)

    def pickIndex(self) -> int:
        # Generate a random number between 1 and the total sum of weights
        target = random.randint(1, self.cumulative_weights[-1])
        # Perform a binary search to find the target within the cumulative weights
        left, right = 1, len(self.cumulative_weights) - 1
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2


            # Since we want to find the first element that is not less than the target,
            # move the right pointer to mid if the middle cumulative weight is >= target
            if self.cumulative_weights[mid] >= target:
                right = mid
            # Otherwise, move the left pointer to one after the current middle
            else:
                left = mid + 1


        # The final index will be left - 1, since the cumulative_weights includes
        # an extra 0 at the beginning that we added during initialization
        return left - 1
