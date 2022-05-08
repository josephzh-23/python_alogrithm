# """
# Time Complexity: O(V + E)
# Auxiliary Space: O(V)
#
# Given 2 nodes, in an undirceted graph, check it should return a boolean
# indicating whether a path exists between nodeA and nodeB
# """
#
# # Python3 program to check if there is exist a path between
# # two vertices of an undirected graph.
# from collections import deque
#
#
# def addEdge(v, w):
#     global adjList
#     adjList[v].append(w)
#     adjList[w].append(v)
#
#
# # A BFS based function to check whether d is reachable from s.
# def isReachable(start, dest):
#     # Base case
#     if (start == dest):
#         return True
#
#     visited = [False] *V
#
#     queue = deque()
#
#     visited[start] = True
#     queue.append(start)
#
#     while (len(queue) > 0):
#
#         # Dequeue a vertex from queue and print
#         start = queue.pop()
#
#
#         for neighbor in adjList[start]:
#
#             if (neighbor == dest):
#                 return True
#
#             if (not visited[neighbor]):
#                 visited[neighbor] = True
#                 queue.append(neighbor)
#
#     return False
#
#
# # Driver program to test methods of graph class
# if __name__ == '__main__':
#
#     # Create a graph given in the above diagram
#     V = 4
#
#     # a 2d list
#     adjList = [[] for i in range(V + 1)]
#     addEdge(0, 1)
#     addEdge(0, 2)
#     addEdge(1, 2)
#     addEdge(2, 0)
#     addEdge(2, 3)
#     addEdge(3, 3)
#     u, v = 1, 3
#     if (isReachable(u, v)):
#         print("There is a path from", u, "to", v)
#     else:
#         print("There is no path from", u, "to", v)
#
#         # This code is contributed by mohit kumar 29.