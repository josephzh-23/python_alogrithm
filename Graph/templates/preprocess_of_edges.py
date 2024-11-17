# Edges
edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

n = len(edges)
# Graph represented as an adjacency list
adj = [[] for _ in range(n)]

# Constructing adjacency list
for edge in edges:
    adj[edge[0]].append(edge[1])