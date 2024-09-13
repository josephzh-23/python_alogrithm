# Python3 program for the above approach


directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# Function to check if current
# position is valid or not
def isValid(row, col, COL, ROW):

    if row < 0 or col < 0 or col > COL - 1 or row > ROW - 1:
        return False
    return True

def dfs(row, col, grid, M, N, vis):

    vis[row][col] = True

    print(grid[row][col], end=" ")

    for direction in directions:
        x, y = row + direction[0], col + direction[1]

        if (isValid(x, y, M, N)) and not vis[x][y]:
            dfs(x, y, grid, M, N, vis)


if __name__ == '__main__':
    # Given matrix
    grid = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

    M = len(grid)

    N = len(grid[0])
    vis = [[False for i in range(M)] for i in range(N)]

    dfs(0, 0, grid, M, N, vis)