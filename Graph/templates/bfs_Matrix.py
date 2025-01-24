from collections import deque
from typing import List



'''
Given a grid that is filled with 0s and 1s 
Start in the top left corner and our goal 
is to find the shortest path to reach the bottom
right corner. S

'''
'''
apply a breadth first search approach to this problem, instead of a depth first search
Use a queue to store the current Row, the current column and the current distance

If  9 is reached(meaning the obstacle has been reached) or t
 then return the distance 
'''
def distanceTraversed(lot: List[List[str]]) -> int:


    n, m = len(lot), len(lot[0])

    # basically to go up, down left and right
    directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]

    q = deque()

    # So we are starting with the first one here
    q.append([0, 0, 0])
    visited= set()

    while len(q) >0:
        curRow, curCol, curDist = q.popleft()


        if curRow == n- 1 and curCol == m-1:
            print(curDist)
            return curDist

        # if lot[curRow][curCol] == 1:
        #     continue

        # directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]
        # 1st : 0, 1
        for direction in directions:
            numRow, numCol = curRow + direction[0], curCol + direction[1]
            if 0<= numRow < n and 0 <= numCol < m and (numRow, numCol) not in visited:
                q.append([numRow, numCol, curDist + 1])
                visited.add((numRow, numCol))

    return -1

lot = [[1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
distanceTraversed(lot)