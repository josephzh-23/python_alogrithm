from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Initialize a min-heap to store end times of intervals
        min_heap = []

        # Sort the intervals based on starting time
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        # Loop through each interval in the sorted list
        for start, end in sorted_intervals:

            # If the heap is not empty and the
            # smallest end time  < the current interval's start time, remove the interval from the heap
            # since it doesn't overlap with the current one. since there is no overlap here
            if min_heap and min_heap[0] < start:
                heapq.heappop(min_heap)

            # Add the current interval's end time to the heap
            heapq.heappush(min_heap, end)

        # The length of the heap gives the minimum number of overlapping groups.
        return len(min_heap)

# Example usage:
# sol = Solution()
# ans = sol.minGroups([[1,3],[2,4],[3,5]])
# print(ans)  # Expected output would be 2
