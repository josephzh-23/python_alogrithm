"""
    Write a function largest component that takes in adjancecy list
of an undirected graph (in adj list).
 Function should return size of largest connected
component in the graph

    - same as finding the largest island almost

"""





def largestComponent(graph):

    # Use set so faster look up and insertion
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size> longest:
            longest = size

    return longest

def exploreSize(graph, node, visited):

    if node in visited:
        return

    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)
    return size

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict = [
    [1, 2, 3],
    [3, 4, 5],
    [1, 2, 3]
]

# We are testing this now
largestComponent(thisDict)

for node in thisDict.values():
    for connectedComp in node:
        print("connected node is", connectedComp)