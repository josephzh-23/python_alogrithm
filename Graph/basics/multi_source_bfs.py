from collections import deque
from typing import List



'''
When do we use this?

1. Find the shortest path from multiple source nodes to a target node in a graph. 

Multi source BFS is particularly useful in scenarios where you need to find the 
shortest paths from multiple starting points to a common destination efficiently


2. 
'''
def orangesRotting(self, grid: List[List[int]]) -> int:
    rotten_orange = deque()
    minutes = 0
    fresh_orange = 0

    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            orange = grid[r][c]
            if orange == 2:
                rotten_orange.append((r, c))
            elif orange == 1:
                fresh_orange += 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while rotten_orange and fresh_orange > 0:
        minutes += 1

        for _ in range(len(rotten_orange)):
            r, c = rotten_orange.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if 0 <=  row < rows and 0 <= col < cols and grid[row][col] == 1:
                    fresh_orange -= 1
                    grid[row][col] = 2
                    rotten_orange.append((row, col))

    return minutes if fresh_orange == 0 else -1