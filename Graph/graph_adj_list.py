"""
    graph = { "a" : ["c"],      // inside the dict is the connected nodes
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

        vertex: same as node
        edge: the line joining 2 vertices a, b
"""
import ipaddress
from collections import defaultdict

edges=[("A","B"),("A","C"),("B","C"),("B","D"),
       ("B","E"),("C","D"),("D","E")]
class Graph:
    def __init__(self,Nodes,is_directed=False):
        self.nodes=Nodes
        self.adj_list={}
        self.is_directed=is_directed

        for node in self.nodes:
            self.adj_list[node]=[]

    def addEdge(self, v, e):
        self.adj_list[v].append(e)
        if not self.is_directed:
            self.adj_list[e].append(v)

    # of edges connected here
    def degreeVertex(self, node):
        degree=len(self.adj_list[node])
        return degree

    def print_adj(self):
        for node in self.nodes:
            print(node,":",self.adj_list[node])




nodes=["A","B","C","D","E"]
graph=Graph(nodes,is_directed=False)
for v,e in edges:
    graph.addEdge(v, e)
graph.print_adj()
# print(graph.degree_vertex("B"))