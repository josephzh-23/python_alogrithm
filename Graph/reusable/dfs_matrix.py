# Python3 program for the above approach

# Direction vectors
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# Function to check if current
# position is valid or not
def isValid(row, col, COL, ROW, vis):

    # Check if the cell is out of bounds
    if (row < 0 or col < 0 or col > COL - 1 or row > ROW - 1):
        return False

    # Check if the cell is visited or not
    if (vis[row][col] == True):
        return False
    return True


# Utility function to print matrix
# elements using DFS Traversal
def DFSUtil(row, col, grid, M, N, vis):

    # Mark the current cell visited
    vis[row][col] = True

    # Print element at the cell
    print(grid[row][col], end=" ")

    # Traverse all four adjacent
    # cells of the current element
    for direction in directions:
        x, y = row + direction[0], col + direction[1]

        # Check if x and y is
        # valid index or not
        if (isValid(x, y, M, N, vis)):
            DFSUtil(x, y, grid, M, N, vis)


# Function to print matrix elementsdef
def DFS(row, col, grid, M, N):
    vis = [[False for i in range(M)] for i in range(N)]

    # Initialize a visiting matrix

    # Function call to print matrix
    # elements by DFS traversal
    DFSUtil(0, 0, grid, M, N, vis)


# Driver Code
if __name__ == '__main__':
    # Given matrix
    grid = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

    # Row of the matrix
    M = len(grid)

    # Column of the matrix
    N = len(grid[0])
    DFS(0, 0, grid, M, N)