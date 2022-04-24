"""
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
"""

# Takes in a list of pairs of edge and then build a graph from it
from collections import defaultdict


def buildGraph(list):
    graph = {}

    # take out the pair
    for pair in list:
        node1 = pair[0]
        node2 = pair[1]

        if node1 not in graph.keys():

            # Can't use append() here
            graph[node1] = []
        if node2 not in graph.keys():
            graph[node2] = []

        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


list = [[1, 2],[3, 4], [1, 3], [1, 5] ]
graph = buildGraph(list)
print(graph)


# Wow look at the following
{1: [2, 3, 5], 2: [1], 3: [4, 1], 4: [3], 5: [1]}