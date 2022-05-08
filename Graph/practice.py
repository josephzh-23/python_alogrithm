from collections import defaultdict


# Using DFS recursive approach here

# Using DFS appproach

class Graph:

    # Constructor
    def __init__(self, vertices):
        self.v = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def DFS(s, v):

        visited = set()

        # Want to perform DFS
        s.DFSUtil(v, visited)

    # find the parent here
    def findParent(s, parent, node):

        if parent[node] == -1:
            return node
        if parent[node] !=-1:
            s.findParent(parent, parent[node])

    # take 2 num, check the rank ->
    # make 1 parent of the other with parent set
    def union(s, parent, u, v ):
        parent[u] = v


    #Using the native union here
    def isCyclic(s):

        parent = [-1] *(s.v)

        for i in s.graph:
            for j in s.graph[i]:
                print("i and j are and size is ", i, j, s.v)
                x= s.findParent(parent, i)
                y = s.findParent(parent, j)

                if x==y:
                    print("this graph contains a cycle")
                    return True
                s.union(parent, x, y)






g= Graph(10)
g.addEdge(4, 5)
g.addEdge(4, 7)
g.addEdge(5, 6)
g.addEdge(4, 6)

g.isCyclic()









