import collections
from typing import List

g= [[1,2,5],[1,3,6],[2,3,1]]


par = []
rank = []
def findMinSpanTree(numCity: int, graph):

    res = []
    # now sorted by weight
    graph = sorted(graph,key=lambda item: item[2])

    print(graph)

    # need to get the largest value in the edges


    i= 0

    # to keep track of the sorted edges here
    e = 0
    for node in range(numCity+1):
        par.append(node)
        rank.append(0)
    while e < numCity-1:
        u, v, w = graph[i]
        i+=1
        x = find(par, u)
        y = find(par, v)

        # not connected so do a union
        if x != y:
            e = e+1
           # that means connected
            res.append([u, v, w])
            union(par, rank, x, y)

    minimumCost = 0
    print("Edges in the constructed MST")

    for u, v, weight in res:
        minimumCost += weight
        print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree", minimumCost)
def find(parent, i):

    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

findMinSpanTree(3,g)

