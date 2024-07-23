'''
If it's 1 a thief
- empty = nobody there

-

    One approach to find the safeness factors of the cells would be to iterate over each cell in the grid and find its distance from all the thieves in the grid.
 We can then pick the smallest distance as the safeness factor for that cell.

 And then here
  Use multi-source bfs:


1. determine the minimum distance from each cell to the nearest thief. Use multi source bfs
2. Sort the distances based on safeness factor here from (0, 0) to (n-1, n-1)

3.Use union find to merge all the cells

4.  Once (0, 0) and (n - 1, n - 1) are combined into the same set, we have found a path with the maximum possible safeness factor,



'''
from collections import deque
from typing import List

from pip._internal.utils.misc import pairwise

from Hard.possible_bipartition import UnionFind



def maximumSafenessFactor(grid: List[List[int]]) -> int:
    """Calculates the maximum safeness factor in a grid avoiding unsafe cells."""
    # Initialize variables
    n = len(grid)
    # If start or end cells are unsafe, return 0
    if grid[0][0] or grid[n - 1][n - 1]:
        return 0

    # BFS to find distances from unsafe cells
    queue = deque()
    dist = [[float('inf')] * n for _ in range(n)]
    # Seed initial distances for unsafe cells
    for i in range(n):
        for j in range(n):

            # add the grid value that's not 0 here and then you have sth here
            if grid[i][j]:

                print(i , j)
                queue.append((i, j))
                dist[i][j] = 0

    # for adding to the queue

    # Directions for moving to adjacent cells
    directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]

    while queue:
        ci, cj = queue.popleft()
        for da, db in directions:
            ni, nj = ci + da, cj + db
            if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == float('inf'):
                dist[ni][nj] = dist[ci][cj] + 1
                queue.append((ni, nj))



    print(dist)
    # Sort cells based on their distance from unsafe cells in descending order
    candidates = sorted(((dist[i][j], i, j) for i in range(n) for j in range(n)), reverse=True)

    uf = UnionFind(n * n)


    for d, i, j in candidates:


        # Attempt to connect current cell with all its neighbors
        for da, db in directions:
            x, y = i + da, j + db
            if 0 <= x < n and 0 <= y < n and dist[x][y] >= d:
                uf.union_set(i * n + j, x * n + y)


        # Check if start and end cells are connected
        if uf.find(0) == uf.find(n * n - 1):
            return int(d)
    return 0

grid = [[0,0,1],[0,0,0],[0,0,0]]
maximumSafenessFactor(grid)