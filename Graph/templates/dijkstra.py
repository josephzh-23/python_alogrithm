from queue import PriorityQueue


'''
From stackabuse website 
'''

'''
This uses adjacency matrix as said 
'''
class Graph:
    def __init__(self, num_of_vertices):
        self.vertices = num_of_vertices

        #edges are also needed for this since we need to know
        # the connections
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, startVertex):
    '''
       This is going to be a list where we keep
       the shortest paths from start_vertex to all of the other nodes.
       '''
    D = {v: float('inf') for v in range(graph.vertices)}

# and then using this we have some intesting property

    '''
    We set the value of the start vertex to 0, since that is its distance from itself
    '''
    D[startVertex] = 0

    pq = PriorityQueue()
    pq.put((0, startVertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)


        for neighbor in range(graph.vertices):
            if graph.edges[current_vertex][neighbor] != -1:

                # this will be the distance updated each time
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:

                    '''
                    oldCost = cur value (shortest path) from start vertext to neighbor 
                    newCost = shortest path from start vertex to cur vertex 
                        + distance between cur vertext to neighbor
                    '''
                    oldCost = D[neighbor]
                    newCost = D[current_vertex] + distance

                    # can also use a min function here
                    if newCost < oldCost:
                        pq.put((newCost, neighbor))
                        D[neighbor] = newCost
    return D

g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)

# return the list as well
D = dijkstra(g, 0)

print(D)

for vertex in range(len(D)):
    print("Distance_dijkstra from vertex 0 to vertex", vertex, "is", D[vertex])