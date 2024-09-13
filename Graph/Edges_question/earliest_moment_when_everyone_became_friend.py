from typing import List

logs = [[20190101,0,1],
        [20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6
def countComponents(self, n: int, logs: List[List[int]]) -> int:
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    components= n
    # first sort this
    logs.sort(keys = lambda x: x[0])
    for friendship in logs:
        timestamp, x, y= friendship

        if find(x) != find(y):
            union(x, y)
            components -=1

        if components == 1: # reached connected components
            return timestamp
    return -1
