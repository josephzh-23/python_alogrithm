'''


input = [[1, 2], [0, 3, 2], [0, 1], [1]]
x = 3

we want to know if all nodes can be reached from the node 3 here
'''


# Function to find if
# all nodes can be visited from X
def canVisitAllNodes(arr, X, n):
    q = []
    visited = [False] * n
    q.append(X)
    visited[X] = True
    count = 0

    # Loop to implement BFS

    # this is like the bfs from rotten oranges we want to traverse each side of the q here
    while (len(q) > 0):
        size = len(q)

        for i in range(size):
            curr = q.pop(0)

            count = count + 1

            for j in arr[curr]:

                # if this hasn't been visited we add it here
                if (visited[j] == False):
                    q.append(j)
                    visited[j] = True

    # Check if all nodes are visited
    if (count == n):
        return True

    return False
