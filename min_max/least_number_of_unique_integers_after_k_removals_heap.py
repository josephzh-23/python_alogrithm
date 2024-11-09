'''

How to solve this here
'''
import heapq
from collections import Counter
from typing import List

from Queue_heap.max_heap import MinHeap


def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    # Dictionary to track the frequencies of elements
    freq_map = Counter(arr)

    # Min heap to track all the frequencies
    frequencies = list(freq_map.values())
    heapq.heapify(frequencies)

    # Tracking the number of elements removed
    elements_removed = 0
    print(frequencies)
    # Traversing all frequencies
    while frequencies:
        # Removing the least frequent element
        elements_removed += heapq.heappop(frequencies)

        # If the number of elements removed exceeds k, return
        # the remaining number of unique elements
        if elements_removed > k:
            # Add 1 for the remaining element
            return len(frequencies) + 1

    # We have removed all elements, so no unique integers remain
    # Return 0 in this case
    return 0


nums = [4, 3, 1, 1, 3, 3, 2]
findLeastNumOfUniqueInts(nums, 3),
