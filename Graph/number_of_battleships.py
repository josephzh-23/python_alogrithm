'''
This part is important here with graph very important

https://algo.monster/liteproblems/419

An interesting problem indeed here

Very simliar to the # of islands but we have to solve it better here ?

Could you do it in one-pass, using only O(1) extra memory and
without modifying the values board?


'''

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def isValid(row, col, COL, ROW):
    if row < 0 or col < 0 or col > COL - 1 or row > ROW - 1:
        return False
    return True


# Utility function to print matrix
# elements using DFS Traversal
def dfs(row, col, grid, M, N, vis):
    vis[row][col] = True
    for direction in directions:
        x, y = row + direction[0], col + direction[1]

        if (isValid(x, y, M, N)) and not vis[x][y]:
            dfs(x, y, grid, M, N, vis)


# 2d matrix here
def solution(grid: list[list]):
    numOfIslands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "x":
                # we want to make sure this is a  leader node (which means it's the first
                # one that's starting here

                # and i think this one would be ok here
                if (row ==0 or grid[row - 1][col] == '.') and (col ==0 or grid[row][col - 1] == '.'):
                    numOfIslands+=1

        # the above is number 1 here

