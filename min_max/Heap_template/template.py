'''

Below is based on min cost to hire k workers

'''
'''

The quality
n workers;


quality and wages here

quality[i]

wages[i]


'''
import heapq
from typing import List

from Queue_heap.max_heap import MinHeap, MaxHeap

'''

quality =  [10, 20, 5] and wage = [70, 50, 30];     k = 2

Hire exactly k workers from a paid group 

1.  
Workers:    1   2   3   4
Quality:    10  20  15  30
Wage:       60  120 90  180


Suppose we hire k =2 workers while meeting the following problems here 

1.  wage[i] / quality[i]
Efficiency: 6   6   6   6

Worker 1: 
quality = 10    add to total quality here 

Worker 2:
so we calculate the total payment for these k workers using the current efficiency, which is 6 * tot = 180.

6 * total = 180 

'''


def mincostToHireWorkers(
     quality: List[int], wage: List[int], k: int
) -> float:
    # Pair each worker's quality with their minimum wage
    # and sort the workers based on their wage-to-quality ratio.
    workers = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])

    # Initialize the answer as infinity to be later minimized
    # Initialize the total quality of workers hired so far as zero
    min_cost = float('inf')
    total_quality = 0

    # Max heap to store the negative of qualities,
    # this is a max heap basically
    max_heap = []

    # Iterate over each worker
    for q, w in workers:
        # Add the current worker's quality to the total quality
        total_quality += q
        # Push the negative quality to the heap
        heapq.heappush(max_heap, -q)

        # If we have more than k workers, remove the one with the highest quality
        if len(max_heap) > k:
            # Since we stored negative qualities, popping from heap retrieves
            # and removes the biggest quality from the total
            top = heapq.heappop(max_heap)
            print('top is', top)
            total_quality += top

        # If we've collected a group of k workers
        if len(max_heap) == k:
            # Calculate the current cost for this group of workers, which is
            # the wage-to-quality ratio of the current worker times total quality
            # and update the minimum cost if it's less than the previous minimum
            min_cost = min(min_cost, w / q * total_quality)

    # Return the minimum cost found to hire k workers
    print(min_cost)
    return min_cost

mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2)
