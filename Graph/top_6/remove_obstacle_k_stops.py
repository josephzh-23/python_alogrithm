from collections import deque
from typing import List

grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
''' 
So when you run into 1 then, then stop traversing and have to change direction 

In other words if we run into 1 then we are done, 

So the most obstacle you can eliminate is 1 

'''

def obstacleRemoved(lot: List[List[str]]) -> int:


    n, m = len(lot), len(lot[0])

    # basically to go up, down left and right
    directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]

    q = deque()


    # so when you encounter an obstacle here, can not add to matrix

    # each of these represent the row, the column and the distance
    q.append([0, 0, 0])
    visited= set()

    while len(q) >0:
        curRow, curCol, curDist = q.popleft()


        if curRow == n- 1 and curCol == m-1:
            print(curDist)
            return curDist

        # if it's an obstacle we will not do the bfs
        if lot[curRow][curCol] == 1:
            continue

        # directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]
        # 1st : 0, 1
        for direction in directions:
            newRow, newCol = curRow + direction[0], curCol + direction[1]
            if 0<= newRow < n and 0 <= newCol < m and (newRow, newCol) not in visited:
                q.append([newRow, newCol, curDist + 1])
                visited.add((newRow, newCol))

    return -1

obstacleRemoved()