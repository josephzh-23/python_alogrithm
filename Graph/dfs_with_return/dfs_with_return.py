def numberIslands( grid: List[List[str]]) -> int:

    numIslands = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def setIslandsZeros(grid, r, c):

        if( 0<= r < len(grid)) and (0<= c < len(grid[0])) and grid[r][c] == "1":
            grid[r][c] = "0"

            for rowInc, colInc in directions:
                setIslandsZeros(grid, r+ rowInc, c+ colInc)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                numIslands +=1

                setIslandsZeros(grid, row, col)
