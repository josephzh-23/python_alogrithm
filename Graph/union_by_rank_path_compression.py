
"""
Some extra notes:
1.
This is union and find approach #2,
using Union By rank or height

notice rank is not the same as height, rank would only increase
, height can decrease though
-
"""

# A union by rank and path compression based
# program to detect cycle in a graph
from collections import defaultdict


# a structure to represent a graph


class Graph:

    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.adjList = defaultdict(list)

    # graph is represented as an
    # array of edges
    def addEdge(self, u, v):
        self.adjList[u].append(v)

# THis will represent a node in the tree
"""
Node     0   1   2  
Parent   0   1   2
Rank     0    0   0 
"""
class Node:
    #
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

"""
A utility function to find the absolute 
parent of a node, initially they would all be itself

Ex: 7 would be the absParent of 7

 using path compression:
 find (7)    before: take 3 steps
             after : take 1 step 
"""
def find(subsets, node):
    """
    What's subset
    Node     0   1   2
    Parent   1   1    2
    Rank     0   0   0
    """
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)

    print("the found absolute parent is", subsets[node].parent)
    return subsets[node].parent


"""
Node     0   1   2  
Parent   0   1   2
Rank     0    0   0 

After union of 0 and 1, 1 becomes parent of 0 
Node     0   1   2  
Parent   1   1   2 
Rank     0    1   0 

1's rank would increase 
"""
def union(subsets, u, v):

    # Attach smaller rank tree under root
    # of high rank tree(Union by Rank)
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u

    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v

    # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


def isCycle(graph):
    subsets = []

    for u in range(graph.num_of_v):
        print("subset is", u)
        subsets.append(Node(u, 0))


         # Iterate through all edges of graph,
    # find sets of both vertices of every
    # edge, if sets are same, then there
    # is cycle in graph.

    for u in graph.adjList:
        uAbsolutePar = find(subsets, u)

        for v in graph.adjList[u]:
            vAbsolutePare = find(subsets, v)


            # this means a cycle is found
            if uAbsolutePar == vAbsolutePare:
                print("u absParent and v absParent are", uAbsolutePar, vAbsolutePare)
                return True
            else:
                union(subsets, uAbsolutePar, vAbsolutePare)


# Driver Code
g = Graph(3)

# add edge 0-1
g.addEdge(0, 1)

# add edge 1-2
g.addEdge(1, 2)

# add edge 0-2
g.addEdge(0, 1)

if isCycle(g):
    print('Graph contains cycle')
else:
    print('Graph does not contain cycle')
