'''
THis is used to solve problems such as weighted graph
such as the
'''
import collections
flights= [[0, 1, 100]]
graph = collections.defaultdict(dict)
for source, des, weight in flights:
    graph[source][des] = weight