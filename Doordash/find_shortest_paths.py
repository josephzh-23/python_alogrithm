import heapq
from collections import defaultdict
'''
Road from/to/weight
1 (1, 2, 1)
2 (2, 3, 1)
3 (3, 4, 1)
4 (4, 5, 1)
5 (5, 1, 3)
6 (1, 3, 2)
7 (5, 3, 1)

Example Input: (5, [1, 2, 3, 4, 5, 1, 5], [
2, 3, 4, 5, 1, 3, 3], [1, 1, 1, 1, 3, 2, 1])
The traveller must travel from city 1 to city g_nodes, so from node 1 to node 5 in this case.
The shortest path is 3 units long and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5.
Return an array of strings, one for each road in order, where the value is YES if a road is along a shortest path or NO if it is not. In this case, the resulting array is ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES']. The third and fourth roads connect nodes (3, 4) and (4, 5) respectively. They are not on a shortest path, i.e. one with a length of 3 in this case

'''

def find_shortest_paths(g_nodes, g_from, g_to, g_weight):
    # Build graph as adjacency list
    graph = defaultdict(list)
    edges = {}

    for i, (u, v, w) in enumerate(zip(g_from, g_to, g_weight)):
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))  # Since it's bidirectional

        edges[(u, v, w)] = i  # Store edge index
        edges[(v, u, w)] = i  # Store for reverse direction

    # Dijkstra's Algorithm to find shortest path from node 1
    def dijkstra(start):
        dist = {i: float('inf') for i in range(1, g_nodes + 1)}
        dist[start] = 0
        pq = [(0, start)]  # (distance, node)
        paths = defaultdict(set)  # Stores predecessors

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight, idx in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

                    paths[neighbor] = {node}  # New shortest path
                elif new_dist == dist[neighbor]:  # Multiple shortest paths
                    print("the node is", node)
                    paths[neighbor].add(node)

        return dist, paths

    # Run Dijkstra from node 1


    '''
    What does this return 
    {1: 0, 2: 1, 3: 2, 4: 3, 5: 3}
    Print the shortest distance from [1] to each node 
    
    Shortest paths here would be 
    {2: {1},
     5: {1, 3},
      3: {1, 2},
       4: {3}})
       
       Because based on the input 
       1 (1, 2, 1)
        2 (2, 3, 1)
        3 (3, 4, 1)
        4 (4, 5, 1)
        5 (5, 1, 3)
        6 (1, 3, 2)
        7 (5, 3, 1)
    From  1-> 3 : the path can be [1-> 2 -> 3] gives 2 as well here 
        or [1-> 3] which gives 2 
    '''
    shortest_dist, paths = dijkstra(1)


    print("shortest dist and paths are ", shortest_dist, paths)
    # Find all edges used in shortest paths

    shortest_path_edges = set()
    queue = [g_nodes]

    while queue:
        node = queue.pop()
        '''
        For each path here then we check 
        We get the edge_index here 
        '''
        for prev in paths[node]:  # Check all predecessors
            edge_weight = shortest_dist[node] - shortest_dist[prev]
            edge_index = edges.get((prev, node, edge_weight), None)
            if edge_index is not None:
                shortest_path_edges.add(edge_index)
            queue.append(prev)

    # Prepare output
    result = ["YES" if i in shortest_path_edges else "NO" for i in range(len(g_from))]

    return result


# Example test case
g_nodes = 5
g_from = [1, 2, 3, 4, 5, 1, 5]
g_to = [2, 3, 4, 5, 1, 3, 3]
g_weight = [1, 1, 1, 1, 3, 2, 1]

print(find_shortest_paths(g_nodes, g_from, g_to, g_weight))