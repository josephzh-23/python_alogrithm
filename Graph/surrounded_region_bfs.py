'''
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]


The solution is based on the idea that an 'O' region would not be captured
if it's connected directly or indirectly to an 'O' on the boundary of the board
 since it cannot be surrounded entirely by 'X's.

 To implement this, we apply depth-first search (DFS) to mark all 'O's
 that are connected to the boundary 'O's with a temporary marker (in this case, '.').
 This multi-step approach ensures we only flip those 'O's into 'X's that are truly surrounded:


Step 1:
Identify Boundary-Connected 'O's:

1) Iterate over the border rows and columns. For any 'O' found on the boundary,
perform a DFS search to mark not only this 'O' but also any other 'O' connected to this one, directly or indirectly.
 We replace these 'O's temporarily with '.' to indicate they're safe from flipping.


Step 2:
Capture Surrounded Regions:
After the DFS marking step, we go through the entire board to flip the remaining 'O's (those that are not marked with 'E')
into 'X's as they are surrounded by 'X's.

Step 3: reverse it
Restore Boundary-Connected Regions: Finally, we make another pass to convert all temporary markers 'E' back into 'O's to restore the initial state for all the 'O's that were connected to the board boundary.

By taking this approach, we ensure to flip only those 'O's that are truly surrounded by 'X's,
while preserving the boundary-connected 'O's.

And that's it here not too bad as said

'''
from typing import List

from Graph.number_of_battleships import directions, isValid


# and then the code here, then next
def solve( board: List[List[str]]) -> None:
    rows, cols = len(board), len(board[0])

    def dfs(row, col):
        board[row][col] = 'e'

        for direction in directions:
            x, y = row + direction[0], col + direction[1]

            # keep the traversing if it's connected to the outside here
            if (isValid(x, y, rows, cols)) and board[x][y] == 'o':
                dfs(x, y)




    # First, traverse the border cells to find 'O's connected to borders
    for i in range(rows):
        for j in range(cols):
            is_border_cell = i in (0, rows - 1) or j in (0, cols - 1)
            if board[i][j] == 'O' and is_border_cell:
                dfs(i, j)

    # and then next we have the code

    # Then, flip all the 'O' regions that are not on the border to 'X'
    # and convert the previously marked border-connected 'O's back to 'O'
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '.':
                board[i][j] = 'O'


