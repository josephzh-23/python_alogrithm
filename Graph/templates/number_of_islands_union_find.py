from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        uf = UnionFind(n * m)
        count = 0
        for i in range(n):
            for j in range(m):

                '''
                We need the unique identifier here which is important 
                
                '''
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0';
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        if uf.union(i * m + j, (i - 1) * m + j):
                            count -= 1

                    if i + 1 < n and grid[i + 1][j] == '1':
                        if uf.union(i * m + j, (i + 1) * m + j):
                            count -= 1

                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        if uf.union(i * m + j, i * m + j - 1):
                            count -= 1

                    if j + 1 < m and grid[i][j + 1] == '1':
                        if uf.union(i * m + j, i * m + j + 1):
                            count -= 1

        return count


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False