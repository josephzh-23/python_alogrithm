'''


Here is where we dela with the code here
'''
from collections import deque




'''
adj is basically a list of lists here 
- and then we will have the next thing here 
If adj[1] = [2, 3, 4]
indegree[2] = 1
inDegree[3] = 1
inDegree[4] = 1         because all 3 will have an indegree here 

And then you add things one by one here and then you keep going here 
'''
def topological_sort(adj, V):
    # Vector to store indegree of each vertex
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1

    # Queue to store vertices with indegree 0
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, push it to the queue
            if indegree[adjacent] == 0:
                q.append(adjacent)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result


if __name__ == "__main__":
    n = 6  # Number of nodes

    # Edges
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(n)]

    # Constructing adjacency list
    for edge in edges:
        adj[edge[0]].append(edge[1])

    # Performing topological sort
    print("Topological Sort of the graph:", end=" ")
    result = topological_sort(adj, n)

    # Displaying result
    for vertex in result:
        print(vertex, end=" ")













