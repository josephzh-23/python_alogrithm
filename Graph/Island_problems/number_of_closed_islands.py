'''


'''
from collections import deque
from typing import List


def distanceTraversed(lot: List[List[str]]) -> int:


    n, m = len(lot), len(lot[0])

    # basically to go up, down left and right
    directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]

    q = deque()

    # each of these represent the row, the column and the distance
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

                if lot[numRow][numCol] == 1:
                    q.append([numRow, numCol, curDist + 1])
                    visited.add((numRow, numCol))


