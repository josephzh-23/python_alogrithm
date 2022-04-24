"""
 Need to watch out for undircted graph,
 since it may contain cycle,
  To avoid processing a node more than once, we use a boolean visited array.

- we have put this in the Graph class
"""

# Create a graph given in
# the above diagram
from Graph.graph_adj_list import Graph

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# print("Following is Breadth First Traversal"
#       " (starting from vertex 2)")
g.bFS(2)
