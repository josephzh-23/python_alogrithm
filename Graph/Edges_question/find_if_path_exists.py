import collections
from collections import defaultdict
from typing import List

'''
n = 3, edges = [[0, 1], [1, 2], [2, 0]]
source = 0 here 
destination = 2

There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
'''


# this is undirected here
def validPath( n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    seen = set()

    def dfs(curr_node):
        if curr_node == destination:
            return True
        if curr_node not in seen:
            seen.add(curr_node)
            for next_node in graph[curr_node]:
                if dfs(next_node):
                    return True
        return False
    return dfs(source)
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(validPath(3, edges, 0, 2))