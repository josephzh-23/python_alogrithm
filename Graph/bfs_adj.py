# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
import collections
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if n == 1:
        return True
    graph = collections.defaultdict(list)
    for e in edges:
        src, dst = e
        graph[src].append(dst)
        graph[dst].append(src)
    queue = [source]
    seen = set()
    while queue:
        cur = queue.pop(0)
        seen.add(cur)
        for neighbour in graph[cur]:
            if neighbour == destination:
                return True
            if neighbour not in seen:
                queue.append(neighbour)
    return False
# Create a graph given in
# the above diagram

print ("Following is Breadth First Traversal"
       " (starting from vertex 2)")
g.BFS(2)

# This code is contributed by Neelam Yadav