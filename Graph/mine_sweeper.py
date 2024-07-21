'''


It should have been good over here and then lets keep it going?
So what happens next is there we have the code


Case 1:
- Revealing Blank Spaces: If the clicked cell has no adjacent mines,
 you trigger a recursive process similar to flood fill.
 It reveals all connected empty cells and keeps expanding
 until it hits the boundaries or cells with adjacent mines.

 Case 2:
If an empty square 'E' with at least one adjacent mine is revealed,
 then change it to a digit ('1' to '8') representing the number of adjacent mines.

'''
from collections import deque


def updateBoard(self, board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board
    m = len(board)
    n = len(board[0])
    q = deque()
    q.append(click)
    visited = set()
    visited.add(tuple(click))
    while q:
        # print(q)
        for _ in range(len(q)):
            curr = q.popleft()
            x, y = curr[0], curr[1]

            count_mine = 0

            # this is then traversing in all 8 directions here,
            # very important,
            for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                nx, ny = x + a, y + b

                # check if there is mine
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] == 'M':
                        count_mine += 1


            '''
            
            So if a mine does exist then we need to show it on the mine here 
            
            '''
            if count_mine > 0:
                board[x][y] = str(count_mine)
            else:

                '''
                No mine? Start bfsing in all 8 directions
                
                '''
                board[x][y] = 'B'
                for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    nx, ny = x + a, y + b

                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        q.append([nx, ny])
                        visited.add((nx, ny))
    return board