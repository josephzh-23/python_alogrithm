
"""
 Using BFS or DFS, both could work

"""
"""
TC: O(E + V)
Space complexity : O (V)    # of vertixes
# of connected components, you can take a look at the video for better demonstration
but basically we increase counter:

    when we find a unconnected component, this is like finding the # of islands

The summary of steps
    Initialize all vertices as unvisited.
    For all the vertices check if a vertex has not been visited,
    then perform DFS on that vertex and increment the variable count by 1.
"""
class Graph:

    def __init__(self, V):

        # No. of vertices
        self.V = V

        # Pointer to an array containing
        # adjacency lists
        self.adj = [[] for i in range(self.V)]

    # Function to return the number of
    # connected components in an undirected graph
    def NumberOfconnectedComponents(self):

        # Mark all the vertices as not visited
        visited = [False for i in range(self.V)]

        # To store the number of connected
        # components
        count = 0

        for v in range(self.V):
            if (visited[v] == False):
                self.DFSUtil(v, visited)
                count += 1

        return count


    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        visited[v] = True

        for i in self.adj[v]:
            if (not visited[i]):
                self.DFSUtil(i, visited)

    # Add an undirected edge
    def addEdge(self, v, w):

        self.adj[v].append(w)
        self.adj[w].append(v)


# Driver code
g = Graph(6)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)

print(g.NumberOfconnectedComponents())