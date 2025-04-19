'''

["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]


The solution employs a clever implementation of Reservoir Sampling to ensure that each potential index
for the target value is chosen with equal probability.

Let's step through the implementation provided in the Reference Solution Approach:

We start with the __init__ method of the Solution class, which simply stores the nums array as an instance variable for later use.

[], and then here

The pick method is where the logic for Reservoir Sampling comes into play. Here, we initialize two variables, n, which will track the number of times we've encountered the target value, and ans, which will hold our currently chosen index for the target.

We then loop through each index-value pair in nums using the enumerate function.

Inside the loop,

1. we check if the current value
v is equal to the target value. If it's not, we continue looping without doing anything further.

2.
However, if v is the target, we increment our count n. This count is crucial because it influences the probability of selecting the current index.

3.
Next, we generate a random number x between 1 and n using random.randint(1, n). This random number decides whether we should update our current answer ans to the current index i.

The condition if x == n: is the key to ensuring that each index has an equal chance of being chosen. This condition will be true exactly once in n occurrences on average, which aligns with the probability we want. When this condition is true, we set ans to i.

After the loop completes, ans will hold the index of one of the occurrences of the target value, chosen at random. We return ans.

'''
import bisect
import random

from Binary_Search.single_element_in_sorted_array import binary_search

class Solution:
    def __init__(self, nums: List[int]):
        """Initialize the Solution object with a list of numbers."""
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Pick a random index from the list of numbers where the number at that index equals the target.
        This uses Reservoir Sampling to ensure that each such index has an equal probability of being chosen.
        """
        count = 0  # Counter for the occurrence of the target
        chosen_index = None  # Variable to store the randomly chosen index

        # here is the code here
        # Enumerate over the list of numbers
        for index, value in enumerate(self.nums):
            # Check if the current value matches the target
            if value == target:
                count += 1  # Increment the counter for each occurrence
                # Generate a random number between 1 and the current count (both inclusive)
                random_number = random.randint(1, count)
                # If the generated number equals the current count, update the chosen index
                if random_number == count:
                    chosen_index = index
        # Return the selected index which corresponds to the target in the list
        return chosen_index
