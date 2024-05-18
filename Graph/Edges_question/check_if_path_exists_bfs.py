# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
from typing import List


# This class represents a directed graph
# using adjacency list representation

def validPath(edges: List[List[int]], source, destination):

    graph = defaultdict(list)
    visited = set()
    for e in edges:
        u, v = e
        # since it is bidrectional here
        graph[u].append(v)
        graph[v].append(u)

    # Create a queue for BFS
    q = []
    q.append(source)

    while q:

        # Dequeue a vertex from
        # queue and print it
        cur = q.pop(0)
        print (cur, end = " ")
        if cur == destination:
            return True
        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then add it
        # in visited and enqueue it
        for i in graph[cur]:
            if i not in visited:
                q.append(i)
                visited.add(cur)

                # Driver code
        return False
# Create a graph given in
# the above diagram

print ("Following is Breadth First Traversal"
       " (starting from vertex 2)")

# This code is contributed by Neelam Yadav
