from typing import List


def countComponents(n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    for x, y in edges:
        union(x, y)


    numOfComponents = n
    print(parent)
    # method 1 here
    for x, y in edges:
        if find(x) == find(y):
            numOfComponents-=1
    return numOfComponents