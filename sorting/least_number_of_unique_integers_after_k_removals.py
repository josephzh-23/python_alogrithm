"""

Using k digits here wouldb e a lot better
Using a monotonic stack here

When we see an element x, if x > the last one in stack, stack.pop()
and then we add this element

if the string is "1432219"   k = 3
then remove string is "1219" as shown above here

remove the string 4,3, 2
"""
import heapq
from collections import Counter
from typing import List

stack = [1, 2, 3, 4, 5]
print(stack[:-2])       # the above is for truncating elements as said


def findLeastNumOfUniqueInts( arr: List[int], k: int) -> int:
    # Dictionary to track the frequencies of elements
    freq_map = Counter(arr)
    print(freq_map)

    # Min heap to track all the frequencies
    frequencies = list(freq_map.values())
    heapq.heapify(frequencies)

    # print("frequencies are ", frequencies)
    # Tracking the number of elements removed
    elements_removed = 0

    # Traversing all frequencies
    while frequencies:
        # Removing the least frequent element
        elements_removed += heapq.heappop(frequencies)

        print("frequencies are ", frequencies, elements_removed)

        # If the number of elements removed exceeds k, return
        # the remaining number of unique elements
        if elements_removed > k:

            # Add 1 for the remaining element
            return len(frequencies) + 1

    # We have removed all elements, so no unique integers remain
    # Return 0 in this case
    return 0
arr = [5, 5, 4]
k = 1
findLeastNumOfUniqueInts(arr, k)

'''
Output: 1
Explanation: Remove the single 4, only 5 is left.
'''