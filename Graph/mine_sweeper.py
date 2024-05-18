'''

This the given problem here
M : game over here
M : revealed    E: unrevealed
click = [click, click ]

Case 1 here:
IF an empty sque E -> we check its adjacent neighbor(u, d, l and r)
if neighbors area all Es then turn the cur cell into B


If an empty q -> but if its neighbor is M, then it becomes 1, once it becomes 1 recursion stops
  1  1  1
  1  M  1
  1  1  1

else:
    if board[x][y] has adjcent mines:
        -change board[x][y] to # of mines adjacent
    if board[x][y] has no adjacent mines:
        -change board[x][y] to 'b'



Using E, M and
'''
from collections import deque


# and then here we have the code
def solution(board, click):

    def getAdjacentMines(board, x, y):
        numMines = 0
        # the reason x + 2 b/c it stops at x + 1,

        '''
        Here is what we need to check here 
        [x-1, y-1]   [x-1, y ]   [x-1,y + 1]
                        [x,y]      [x, y + 1]
                     [x +1, y]    
        
        '''
        for r in range(x-1, x+ 2):
            for c in range(y -1, y + 2):
                if 0 <= r < len(board) and 0 <= c < len(board[c]) and board[r][c] =='m':
                    numMines +=1
        return numMines

    def updateBoard(board, click):
        if not board:
            return board
        x, y = click
        if board[x][y] == 'm':
            board[x][y] = 'x'
        else:
            numMines = getAdjacentMines(board,x, y)
            if numMines:
                board[x][y] = str(numMines)
            # no more mines in the adjacent here
            else:
                board[x][y] = 'b'

                for r in range(x-1, x + 2):
                    for c in range(y-1, y +2):
                        # in the case of empty it will keep updating here
                        if 0<= r< len(board) and 0<=c < len(board[r]) and board[r][c] !='b':
                            updateBoard(board, [r, c])

        return board












