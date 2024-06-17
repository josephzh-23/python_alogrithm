from typing import List

from Heap.max_heap import MinHeap


def minimumObstacles(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    visited = [[False] * m for _ in range(n)]

    paths = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    q = MinHeap()
    q = q.push([0, 0, 0]) # val, x,y will be pushed

    while q:
        obstacle, i, j = q.pop()
        if i == n - 1 and j == m - 1:
            print('step is', obstacle + grid[i][j])

            return obstacle + grid[i][j]

        for x, y in paths:
            x1 = i + x
            y1 = j + y

            if (x1 >= 0 and x1 < n and y1 >= 0 and y1 < m and not visited[x1][y1]):
                visited[x1][y1] = True
                q.push(obstacle + grid[x1][y1], x1, y1)

    return -1


# now to test thsi soultino here

grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
minimumObstacles(grid)