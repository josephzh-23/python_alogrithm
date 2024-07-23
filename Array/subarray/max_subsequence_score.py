'''
Better when using this


 Now, since our final score involves a sum from nums1 and a minimum from nums2, we wish to select the top
 k indices with respect to the product of sums and minimums.

 1. as we iterate through our sorted pairs,


 2. If the heap == full,
    - try to calculate the final score here
'''
from heapq import heappush, heappop

from Heap.max_heap import MinHeap


def maxScore(self, cards1: List[int], cards2: List[int], k: int) -> int:
    # Combine the two lists into one by creating tuples of cards from cards2 and cards1
    # and sort the combined list in descending order based on cards2 values.
    combined_cards = sorted(zip(cards2, cards1), reverse=True)

    # Initialize a min-heap to keep track of the smallest elements.
    min_heap = []
    # Initialize sum and answer
    current_sum = 0
    max_score = 0

    # Iterate over the sorted list of combined cards.
    for card2_value, card1_value in combined_cards:
        # Add the value from cards1 to the current sum.
        current_sum += card1_value
        # Push the value from cards1 to the min-heap.
        heappush(min_heap, card1_value)

        # If the heap size reaches k, update the maximum score.
        # This corresponds to choosing k cards from cards1.
        if len(min_heap) == k:
            max_score = max(max_score, current_sum * card2_value)
            # Remove the smallest element from the current sum as we want the largest k elements.
            current_sum -= heappop(min_heap)

    # Return the maximum possible score.
    return max_score







