# from collections import deque
#
#
#
from typing import List


def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    # Check if the starting cell is blocked
    if grid[0][0] != 0:
        return -1

    # Initialize the size of the grid
    n = len(grid)
    # Set starting point as visited by marking it with a 1 (path length from the origin)
    grid[0][0] = 1
    # Initialize a queue with the starting coordinate
    queue = deque([(0, 0)])
    # Initialize path length
    path_length = 1

    # Process nodes until the queue is empty
    while queue:
        # Loop through all nodes at the current level of breadth
        for _ in range(len(queue)):
            i, j = queue.popleft()  # Get next node coordinates

            # Check if we've reached the target cell
            if i == j == n - 1:
                return path_length

            # Check all 8 adjacent cells
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    # Boundary check and cell is not blocked
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        # Mark cell as visited and add its coordinates to the queue
                        grid[x][y] = 1
                        queue.append((x, y))
        # Increment path length at the conclusion of the level
        path_length += 1

    # If we exit the loop without returning, no path has been found
    return -1
