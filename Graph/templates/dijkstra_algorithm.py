graph ={
    'a': {'b': 3, 'c': 4, 'd': 7},
    'b': {'c':1, 'f':5},
    'c': {'f':6, 'd':2},
    'd': {'e': 3, 'g': 6},
    'e': {'g': 3, 'h': 4},
    'f': {'e':1, 'h':8},
    'g': {'h': 2},
    'h': {'g':2}
}
def dijkstra(graph, start, goal):

    shortestDist = {} #record cost to reach that node. Updated as we move along the graph
    trackPredecessor = {}  # keep track of the path that has let us to this node

    unvisitedNodes = graph     #iterate thru entire graph
    infinity = 99999        # can be a very large number

    trackPath = [] #ongoing to trace our journey back to the source node - optimal route

    for node in unvisitedNodes:
        shortestDist[node] = infinity
    shortestDist[start] = 0

    while unvisitedNodes:
        minDistanceNode = None

        for node in unvisitedNodes:
            if minDistanceNode is None:
                minDistanceNode = node
            elif shortestDist[node] < shortestDist[minDistanceNode]:
                minDistanceNode = node

        pathOptionsCool = graph[minDistanceNode].items()

        for childNode, weight in pathOptionsCool:
            if weight + shortestDist[minDistanceNode] < shortestDist[childNode]:
                shortestDist[childNode] = weight + shortestDist[minDistanceNode]
                trackPredecessor[childNode] = minDistanceNode

        unvisitedNodes.pop(minDistanceNode)
    currentNode = goal

    while currentNode != start:
        try:
            trackPath.insert(0, currentNode)
            currentNode = trackPredecessor[currentNode]

        except KeyError:
            print("Path is not reachable")
            break

    trackPath.insert(0, start)
    if shortestDist[goal] != infinity:
        print("shortest distance is " + str(shortestDist[goal]))
        print("Optimal path is " + str(trackPath))

# print(graph['a'].items())
dijkstra(graph, 'a', 'h' )