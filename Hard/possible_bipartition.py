'''
 People that !like each other diff set:
 1. Union of all neighbors then

 2. If any neighbor in same set as cur:
    not good

3.

'''
from collections import defaultdict


def possiblePartition(n, dislikes):
    u = UnionFind(len(dislikes)+1)
    adj = defaultdict(list)
    for edge in dislikes:

        # sth unique to the python world ehre
        a, b = edge
        adj[a].append(b)
        adj[b].append(a)


    #
    for node in range(1, n):
        if node not in adj:
            continue
        for neigh in adj[node]:
            if u.find(node) == u.find(neigh):
                return False
    # move all its neighbors in the same list here so this is importnat
            u.union_set(adj[node][0], neigh)

#at the very end
    return True
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
