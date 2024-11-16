'''You are given an array called nums that has a certain number of elements, denoted as n. You have to find the
majority element in this array. The majority element is defined as the one that

 appears more than n / 2 times. It's
guaranteed that there is always a majority element in the array you're given.

The Moore Voting Algorithm works by keeping a current candidate for majority element and a counter.
As it goes through the array, the algorithm either increases the count if the current number matches the
candidate or decreases the count otherwise.

        When the count reaches zero, it means that up to that point, there is no majority element, and the algorithm selects the
  current number as the new candidate. The key insight is that the majority element's surplus
 count will withstand the count decrements due to non-majority elements.

 This is done using moore voting algorithm here

 Majority element ii

 what if we use dictionary here

'''
from typing import List


def majorityElement(self, nums: List[int]) -> int:
    # Initialize the count and the candidate for majority element
    count = 0
    majority_candidate = None

    # Process each number in the list
    for num in nums:
        # If the current count is 0, we choose a new number as the potential majority candidate
        if count == 0:
            majority_candidate = num
            count = 1
        # If the current number is the same as the majority candidate, increase the count
        elif majority_candidate == num:
            count += 1
        # Otherwise, decrease the count
        else:
            count -= 1

    # The majority candidate is the number that remains after pairing off different elements
    return majority_candidate