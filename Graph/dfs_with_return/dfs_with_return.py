from typing import List


def isCaptured(grid: List[List[str]]) -> int:
    # check to see if the board is captured here
    def dfs(grid, i, j):

        if (i < 0 or i>= len(grid)) or ( j< 0 or j >= len(grid[0])) or grid[i][j] == '1':
            return True
        # Not surrounded
        if grid[i][j] == '-':
            return False

        grid[i][j] = '1'
        return dfs(grid, i - 1, j) and dfs(grid, i + 1, j) and dfs(grid, i, j - 1) and dfs(grid, i, j + 1)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '0':
                if (not dfs(grid, row, col)):
                    return False

    return True

grid = [['1', '0', '1', '0'], ['1', '0', '1', '0'], ['1', '1', '1', '0']]
print(isCaptured(grid))