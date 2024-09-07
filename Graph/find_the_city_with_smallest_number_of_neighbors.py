'''
We can work here on this problem adn then do a bit more as said


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],

WHich means from 0 -> 1 the distance is 3 here


n is the number of edges here
'''
import collections
from typing import List

'''
The process

1. Create a 2D matrix g that acts as the adjacency matrix for the graph.
g[f][t] = g[t][f] = w       the one below defiitely makes sense 


2) Perform dijkstra on every src to figure out its distance to all the other nodes
and see how many cities are within reachable distance based on the given threshold limit 

3) Finding the optimal city out of a ll of this here 


'''

def findTheCity(n: int, edges: List[List[int]], distance_threshold: int) -> int:

    '''
    We perform dijkstra's below for every node in this graph here
    '''

    # Function to perform Dijkstra's algorithm to find the shortest
    # paths from node `u` to all other nodes in the graph.
    # and then return the nodes with distances <= thresholdDistance for the starting node
    def dijkstra(u: int) -> int:
        '''
        Will hold the shortest dist frmo src u to every other city
        '''
        distances = [float('inf')] * n

        # Distance_dijkstra to the source node itself is 0.
        distances[u] = 0
        # Keep a visited array to track nodes that have been processed.
        visited = [False] * n

        # Repeat the process for all nodes.
        for _ in range(n):
            # `k` is going to be the unvisited node with the smallest distance.
            k = -1
            for j in range(n):
                # Select the unvisited node with the smallest distance.
                if not visited[j] and (k == -1 or distances[k] > distances[j]):
                    k = j

            # Mark the selected node as visited.
            visited[k] = True
            # Update the distances to all nodes from `k`.
            for j in range(n):
                distances[j] = min(distances[j], distances[k] + graph[k][j])

        # Return the number of nodes within the distance_threshold from `u`.
        total = 0
        for d in distances:
            if d <= distance_threshold:
                total+=1
        return total

    # Create a graph representation (adjacency matrix) with distances set to infinity.
    graph = [[float('inf')] * n for _ in range(n)]

    # Set the distance for all the edges provided in the input.
    for start, end, weight in edges:
        graph[start][end] = weight
        graph[end][start] = weight

    # `res_city` is going to be the resultant city with the smallest number
    # of reachable cities (within threshold) when tied with another city.
    res_city = n
    # `min_reachable_cities` keeps track of the smallest number of reachable cities found.
    min_reachable_cities = float('inf')

    # Iterate over all cities in reverse order to account for the smallest numbered city in a tie.
    for i in range(n - 1, -1, -1):


        # Get the number of cities reachable from city `i` within the distance threshold.
        reachable_cities = dijkstra(i)
        # If the number of reachable cities is less than the current minimum,
        # update `min_reachable_cities` and `res_city`.
        if reachable_cities < min_reachable_cities:
            min_reachable_cities = reachable_cities
            res_city = i

    # Return the city with the smallest number of reachable cities or the smallest
    # numbered city in case of a tie.
    return res_city