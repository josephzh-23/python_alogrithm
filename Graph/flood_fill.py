'''
The flood fill problem that we were working on here

Flood fill problem upfront here
1. So it's basically done on the related item only but nothing else as said


'''
from collections import deque
from typing import List

from Graph.templates.dfs_matrix import directions


# so how do we work on this?
# Function to check if current
# position is valid or not
def isValid(row, col, COL, ROW, vis):
    # Check if the cell is out of bounds
    if row < 0 or col < 0 or col > COL - 1 or row > ROW - 1:
        return False

    # Check if the cell is visited or not
    if vis[row][col]:
        return False
    return True


def floodFill(lot: List[List[str]]) -> int:
    n, m = len(lot), len(lot[0])

    # basically to go up, down left and right
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = deque()

    # each of these represent the row, the column and the distance
    q.append([1, 1])
    lot[1][1] = 2
    # the starting point right here

    # and then the next thign will then come
    visited = set()
    visited.add((1, 1))
    while len(q) > 0:

        # current row nad column right here
        curRow, curCol = q.popleft()

        for direction in directions:
            numRow, numCol = curRow + direction[0], curCol + direction[1]
            if 0 <= numRow < n and 0 <= numCol < m and (numRow, numCol) not in visited:

                if lot[numRow][numCol] == 1 and lot[curRow][curRow] == 2:
                    lot[numRow][numCol] = 2     
                q.append([numRow, numCol])
                visited.add((numRow, numCol))
    print(lot)
    return -1


image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
floodFill(image)
