import collections
import heapq
from collections import defaultdict


def shortestPath(graph, src, dest):
    adjList = collections.defaultdict(list)
    for u, v, w in graph:
        adjList[u].append([v, w])
    h = []
    # keep a track record of vertices with the cost
    # heappop will return vertex with least cost
    # greedy SRC -> MIN - > MIN -> MIN -> DEST

    heapq.heappush(h, (0, src))

    while len(h) != 0:
        currcost, currvtx = heapq.heappop(h)
        if currvtx == dest:
            print("Path Exisits {} to {} with cost {}".format(src, dest, currcost))
            break
        for neigh, neighcost in adjList[currvtx]:
            heapq.heappush(h, (currcost + neighcost, neigh))


# v, e = map(int, input().split())
# for i in range(e):
#     u, v, w = map(str, input().split())
#     graph[u].append((v, int(w)))
# src, dest = map(str, input().split())
graph = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
shortestPath(graph, src, dest)