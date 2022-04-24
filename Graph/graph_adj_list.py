"""
    graph = { "a" : ["c"],      // inside the dict is the connected nodes
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

        vertex: same as node
        edge: the line joining 2 vertices a, b
"""
import ipaddress
from collections import defaultdict


class Graph:
    def __init__(s, nodes=[], isDirected=False):
        s.nodes = nodes

        # this is basically the same as graph below, they are interchangeable
        s.adjList = {}

        if not nodes:
            s.adjList = defaultdict(list)

        s.isDirected = isDirected

        # default dictionary to store graph, this will take form of graph above
        # used for BFS


        # this is the same as the adjacency list
        s.graph = defaultdict(list)

        # initializig the dictionary here
        for node in s.nodes:
            print("node here is", node)
            s.adjList[node] = []



    def addEdge(s, u, v):
        s.adjList[u].append(v)

        if not s.isDirected:
            s.adjList[v].append(u)

    def degree(s, node):
        deg = len(s.adjList[node])
        return deg

    def printAdjList(s):
        for node in s.nodes:
            print(node, "-> ", s.adjList[node])



    # Keep track of visited to avoid cycle

        # prints all not yet visited vertices
        # reachable from s
    def DFSUtil(self, s, visited):

        # Create a stack for DFS
        stack = []

        # Push the current source node.
        stack.append(s)

        while (len(stack) != 0):

            # Pop a vertex from stack and print it
            s = stack.pop()

            # Stack may contain same vertex twice.
            # So we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                print(s, end=" ")
                visited[s] = True

            # Get all adjacent vertices of the
            # popped vertex s. If a adjacent has not
            # been visited, then push it to the stack.
            i = 0
            while i < len(self.adjList[s]):

                if (not visited[self.adjList[s][i]]):
                    stack.append(self.adjList[s][i])
                i += 1

    # prints all vertices in DFS manner
    def DFS(self):

        # Mark all the vertices as not visited
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                self.DFSUtil(i, visited)


    def bFS(s, vertex):

        # Mark all the vertices as not visited
        # print("max is " , max(s.adjList))

        visited = [False] * (max(s.adjList) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(vertex)
        visited[vertex] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            vertex = queue.pop(0)
            print(vertex, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it

            for i in s.adjList[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def countVertexes(s):
        numVertexes = 0
        if nodes:
            for node in s.nodes:
                numVertexes += len(s.adjList[node])
            print('total # of vertexes are ',numVertexes)
        else:
            numVertexes = len(s.adjList)

        return numVertexes


# Testing the graph
allEdges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")]

nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes, isDirected=True)


for u, v in allEdges:
    graph.addEdge(u, v)

graph.printAdjList()
graph.countVertexes()

print("degree of C is", graph.degree("C"))

