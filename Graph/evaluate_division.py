'''


equaionts =


Using this interpretation, the problem of finding the ratio of two variables becomes a problem of finding a path
between two nodes in the graph.
If direct calculate , otherwise don't calculate
Use union find here


Iterate over the queries, for each:
1.
If both variables are in the graph and belong to the same connected component,
 calculate the ratio using the weights along the path that connects the variables.

 2.
If the variables are not in the same connected component or
 at least one is not in the graph, return -1.0 for that query.
'''


import collections
from typing import List


def calcEquation(equations, values, queries):
    adj = collections.defaultdict(list)
    #map a -> list of [b, a/b]
    for i, eq in enumerate(equations):
        a, b = eq
        adj[a].append([b, values[i]])
        adj[b].append([a,1/ values[i]])

    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1
        q, visit = collections.deque(), set()

        # this is the tricky part here, when you add source,
        # 1/1 will be for itself here
        q.append([src, 1])
        visit.add(src)
        while q:
            n,w = q.popleft()
            if n == target:
                return w
            for nei, weight in adj[n]:
                if nei not in visit:
                    q.append([nei, w * weight])
                    visit.add(nei)
        return -1




