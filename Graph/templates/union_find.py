# used to detect cycle in graph structure as expalined in the video
from collections import defaultdict

'''
remember parent and root are 2 different htings

root: the ancestor of all parents, the parent of root is -1 as explained in the
video 
parent: just the immediate parent 

'''


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.adjList = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)

    # findParent () will eventually -> findRoot() as explained
    def findParent(s, parent, i):
        if parent[i] != -1:
            return s.findParent(parent, parent[i])

        # if -1 is the parent, that means it's a parent of itself
        else:
            return i


    # do union of 2 subsets
    def union(s, parent, x, y):
        parent[x] = y

    def isCyclic(s):

        # everything will start with -1 first at the beginning as said for the parent
        parent = [-1] * (s.V)

        # Iterate through all edges of graph, find root of both
        # vertices of every edge, if both roots are the same, then
        # there is cycle in graph.


        for i in s.adjList:
            for j in s.adjList[i]:
                x = s.findParent(parent, i)
                y = s.findParent(parent, j)

                if x == y:
                    return True
                s.union(parent, x, y)


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
