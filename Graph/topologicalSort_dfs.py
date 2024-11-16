# Python program to print topological sorting of a DAG
from collections import defaultdict


'''
Suppose you are a student at Unverisity and you must take A, B, D and E as prereq if you want to take H. 

A -> C -> J
A -> D- > H
B-> D -> H
B -> F -> I 
Using toppological sorting you would be able to know the order in which
 you should enroll such that you 
don’t enroll in a class you don’t have credits for 

Topological ordering is not unique, so there could be > 1 ordering. 
Ex2: 

Building dependencies for android 

Some basic rules

1. Not every graph can have a toplogical ordeirng, cyclic graph doesn’t have ordering
2. Directed acyclic graph has topological ordering. 

Topological Sort Algorithm
1. Pick an unvisited node, 
2. Begin with selected node, do a DFS, exploring only unvisited node. 

3. On the recursive callback of DFS, add current node to toplogical ordering in reverse order 

4. Notice that different from DFS,  We don’t print the vertex immediately, 
we first recursively call topological sorting for all its adjacent vertices, then push it to a stack. Finally, print contents of the stack.
Ex: 

A - > B -> C -> D
			 
When you go from C to D, no more places to go. Backtrack, add D to sorting.
When back to C, check if anothe node you can visit, then visit it.


And the algorithm for this 
'''

# Class to represent a graph


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topologicalSortUtil(neighbor, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack[::-1])  # return list in reverse order


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")

# Function Call
g.topologicalSort()

# This code is contributed by Neelam Yadav