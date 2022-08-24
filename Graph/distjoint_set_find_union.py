"""

This can be used to check if a cycle exists in the graph
This is the approach 1

    TC: O(n)
    approach 2: use O log (n) using Union by Rank or Height,
    have a look at that you can

    - Medium to explain check notes
    Used in step 2 of kruskal's algo, to detect if a cycle exists
    See expalanation on union-find on GeedForGeeks

A distjoint set: is a set are 2 sets that have
no elements in common
    Ex: {1, 3, 5} and {2, 4, 6}         so both are different

    Operation to perform here
    1. We can perform union?
        - check if 2 # belong to diff sets, apply union ex (between 4 and 8)
        and then 4 and 8 an edge will be formed

        - If 2 # belong to same sets, then can't apply union

 Ex: When can we perform union and what does this have to with
 cyclic?
 take 3 numbers

                        Ex: 0  1   2    <-----
  parent array              1  2  -1
            1 is made parent of 0 (1 is now representative of subset {0, 1})
            2 is made parent of 1

            -1: means a parent of itself

            So edge 0-2 would form a cycle, since 0 is in subset 2 and 2 is
        also in subset 2. Edge forms a cycle
"""

from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''
    if a parent[i] == -1, that means it's the parent of itself
    so we just return the parent value
    
    
    '''
    def findAbsParent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.findAbsParent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        parent[x] = y

    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):

        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * (self.V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.findAbsParent(parent, i)
                y = self.findAbsParent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


# Create a graph given in the above diagram
g = Graph(9)
# g.addEdge(0, 1)
# g.addEdge(1, 2)
# g.addEdge(2, 0)

g.addEdge(4, 5)
g.addEdge(4, 7)
g.addEdge(5, 6)
g.addEdge(4, 6)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

# This code is contributed by Neelam Yadav