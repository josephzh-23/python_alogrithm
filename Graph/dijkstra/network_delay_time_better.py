import collections
import heapq
from typing import List


'''
General summary: 
0. Can check out notes in leetcode this is very important 
1. Uses a BFS search, use a PQ instead of regular queue
2. 

visualization:
MinHeap
Distance    Node
0           1
1           3
4           2
            4
Here n = # of nodes 
# you are sending a signal from a given node k

- same as the shortest path theory as dijkstra theory 
. Return the minimum time it takes for all the 
n nodes to receive the signal.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

k = the starting point 
t = time to reach all the nodes 
'''
def networkDelayTime(times:List[List[int]], n: int, k: int) -> int:

    # write down the approach
    edges = collections.defaultdict(list)

    for u, v, w in times:
        edges[u].append((v,w))

    # the distance + the starting distance
    minHeap = [(0, k)]
    visited = set()
    t = 0

    while minHeap:

        # w1 is the time to reach n1
        w1, n1 = heapq.heappop(minHeap)

        if n1 not in visited:

            visited.add(n1)
            # update the time for it
            t = max(t, w1)

        # now we go thru its neighbor,
        for n2, w2 in edges[n1]:
            if n2 not in visited:

                # w1 + w2 is the total path to reach n2
                # example: if  you need to go from 2 to 4
                # need to go thru 2 -> 3 -> 4
                heapq.heappush(minHeap, (w1 + w2, n2))


    # after t is here then it would be possible here,
    #
    print(t)
    return t if len(visited)== n else -1

# O(E*logv)

times = [[2,1,1],[2,3,1],[3,4,1]]
# n = 4
# k = 2
n = 3
k = 1
# networkDelayTime(lot, n, k)






