import collections
from typing import List

'''
    * is your location
    # is food cell, 
    'o' free space 
    'x' is an obstacle, and you can't traverse thru 
    here when you see this, 
'''
def getFood(grid: List[List[str]])->int:

    rows = len(grid)
    cols = len(grid[0])

    queue = collections.deque()
    visited = set()

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == "*":
                # the row, the column and the steps
                queue.append((row, col, 0))
                visited.add((row, col))

                break
        directions =[(1,0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            curRow, curCol, steps = queue.popleft()

            if grid[curRow][curCol] == "#":
                print(steps)
                return steps
            else:
                for rowInc, colInc in directions:
                    newRow = curRow + rowInc
                    newCol = curCol + colInc

                    # this means if we run into obstacle we will return

                    #each traversal counts as a step
                    if (0 <= newRow < rows) and (0 <=newRow < cols) and grid[newRow][newCol]!="X":
                        if (newRow, newCol) not in visited:
                            visited.add((newRow, newCol))

                            # each time we add 1 to the step
                            queue.append((newRow, newCol, steps +1))

    return -1

#: O(m*n) + O(m * n) -> 2* O (m *n ) -> O (m * n)

grid = [["X","X","X","X","X","X"],
        ["X","*","O","O","O","X"],
        ["X","O","O","#","O","X"],
        ["X","X","X","X","X","X"]]
getFood(grid)