from collections import defaultdict, deque
'''

Another elegant approach: If topological sort is not possible, the graph has a cycle.

Steps:
	•	Count in-degrees for all nodes
	•	Start removing nodes with 0 in-degree
	•	If you can’t remove all nodes → there’s a cycle
'''
def has_cycle_kahn(graph):
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited_count != len(graph)