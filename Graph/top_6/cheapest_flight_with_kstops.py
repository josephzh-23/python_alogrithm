

# so we can do a BFS here first
import collections
import heapq
from typing import List


h= heapq
def findCheapestPrice( n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

    # the priority queue this is diff from dijsksta's algo

    # 0 : weight, k+1: the stops
    pq = [(0, src, k+1)]
    graph = collections.defaultdict(dict)
    for source, des, weight in flights:
        graph[source][des] = weight

    print(graph)

    while pq:
        nextItem = h.heappop()

        weight, source, stops = nextItem

        # say we are given
        if source == dst:
            return weight

        '''
        this will iterate over the neighbor
        if 0, neighbor 1 and 2 
        {0: {1: 100, 2: 500}, 1: {2, 100}}
        '''
        if stops >0:
            for neighbor in graph[source]:
                # change the source to the neighbor
                h.heappush(pq, (weight + graph[source][neighbor], neighbor, stops-1))
        return -1



  #  O(E * logV)
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
# src = 0
# dst = 3
# k = 1
findCheapestPrice(4, flights, 0, 3, 1)

