# nuber of islands

'''
When we see a 1, turn a 1 into 0 so this way we know it has been visited

    - this is important for checking the 0 around it

    - we perform a dfs on this
'''
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:

    maxArea = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def findArea(grid, curRow, curCol):

        if (0 <= curRow < len(grid)) and (0 <= curCol < len(grid[0])) and grid[curRow][curCol] == 1:

            grid[curRow][curCol] = 0
            area = 1
            for rowInc, colInc in directions:
                area += findArea(grid, curRow + rowInc, curCol + colInc)

            return area
        else:
            return 0
    # area 1        number of islands
    # maxArea
    area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            area = findArea(grid, row, col)

            maxArea = max(maxArea, area)

    return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

maxAreaOfIsland(grid)