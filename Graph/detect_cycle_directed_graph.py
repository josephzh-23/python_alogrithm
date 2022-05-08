
"""

2 Approaches both would work
1. Approach 1 using a simple DFS
2. This is used in step 2 of Kruskal's algo
 for checking cycle

Expand on approach 1:

TC: O (V + E)

    1. A cycle only if a back-edge ( an self inner loop)

    2. To detect back edge
        - keep track of vertices currently in the
        recursion stack of DFS

    3.f a vertex is reached that is already in the recursion stack,
    then there is a cycle in the tree.
"""
from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    """
        Visited : the set you pass in containing visited
         recStack : vertxes that are in our recursion for the node 
            v we are visiting 
            
         
            if we reach a vertex already in recStack, then -> a cycle
    """
    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True

        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True

            elif recStack[neighbour] == True:
                return True

            # The node needs to be popped from
            # recursion stack before function ends
            recStack[v] = False
            return False


    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)


        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False