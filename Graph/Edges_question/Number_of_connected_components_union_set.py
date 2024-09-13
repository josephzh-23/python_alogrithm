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
    # method 2 using a set
    # s = set()
    # for i in range(n):
    #     s.add(find(i))
    #     # Basically here we return the length of the set of parents (all unique indexes in there)
    #     # as said
    # return len({find(i) for i in range(n)})
edges = [[0, 1], [1, 2], [3, 4]]
print(countComponents(5, edges))


