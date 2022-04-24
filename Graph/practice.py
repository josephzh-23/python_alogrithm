
# Add between the 2
def addEdge(v, w):
    global adjList
    adjList[v].append(w)
    adjList[w].append(v)


def checkPath_undirected_practice(start, end, V):

    # If undirected, use BFS approach
    """
    between u and v, add u, check its adjList
    """
    queue = []
    queue.append(start)

    visited =[False] * V

    while queue:

        # If 4 popped, check its neighbor, if
        start = queue.pop(0)

        for neighbor in adjList[start]:

            if neighbor == end:
                return True
            else:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    # Add it to queue
                    queue.append(neighbor)

        return False


# Do this using DFS,
def checkPath_directed_practice(start, end):
    # [1, 2,3 4 5]
    # using stack
    stack = []

    stack.append(start)
    visited = [False] * (V+1)
    while stack:
        node = stack.pop()

        # print the, in this case 5
        print("popped is", node)

        # check adjList
        for neighbor in adjList[node]:
            print("neighbor is", neighbor)
            if not visited[neighbor]:
                if neighbor== end:
                    return True
                else:
                    visited[neighbor] = True
                    stack.append(neighbor)







V=5
adjList = [[] for i in range(V+1)]
addEdge(3, 4)
addEdge(3, 5)

u = 3
v= 5


checkPath_directed_practice(3, 5)

if (checkPath_directed_practice(u, v)):
    print("There is a path from", u, "to", v)
else:
    print("There is no path from", u, "to", v)








