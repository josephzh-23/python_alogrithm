# nuber of islands

'''
When we see a 1, turn a 1 into 0 so this way we know it has been visited

    - this is important for checking the 0 around it

    - we perform a dfs on this
'''
from typing import List

'''
When we see a 1, we kick off a dfs search in all directions 

1. Every time we see a 1, we set it to a 0 to avoid an infinite loop 
2. This way we don't need the visited set here 

3. Max area of the island here set it equal to 0, 

'''
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


# T: O(R*C)
# S: O(R*C)
