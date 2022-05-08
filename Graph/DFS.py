

# An iterative approach, done using stack and visited array (2 structures) needed

"""
    TC: O (V + E)
    SC: O (V)
"""

class Graph:
    def __init__(self, V):  # Constructor
        self.V = V  # No. of vertices
        self.adj = [[] for i in range(V)]  # adjacency lists

    def addEdge(self, v, w):  # to add an edge to graph
        self.adj[v].append(w)  # Add w to v’s list.

    # prints all not yet visited vertices reachable from s
    def DFS(self, s):  # prints all vertices in DFS manner from a given source.

        visited = [False for i in range(self.V)]

        stack = []

        stack.append(s)

        while (len(stack)):

            s = stack.pop()

            if (not visited[s]):
                print(s, end=' ')

                # Only mark the visited here
                visited[s] = True

             # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.

            for neighbor in self.adj[s]:
                if (not visited[neighbor]):
                    stack.append(neighbor)


# Driver program to test methods of graph class

g = Graph(5)  # Total 5 vertices in graph
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)

print("Following is Depth First Traversal")
g.DFS(0)