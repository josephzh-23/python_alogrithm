'''


Here we are adding incrementing each distance after we traverse each level in the q

'''
from collections import deque
from typing import List


def distanceTraversed(lot: List[List[str]]) -> int:


    n, m = len(lot), len(lot[0])

    # basically to go up, down left and right
    directions = [[0,1 ], [1, 0], [0, -1], [-1, 0]]

    q = deque()

    # So we are starting with the first one here
    q.append([0, 0])
    visited= set()

    curDist = 0
    while len(q) >0:

        for _ in range(len(q)):
            curRow, curCol = q.popleft()


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
                    q.append([numRow, numCol])
                    visited.add((numRow, numCol))
        curDist += 1
    return -1

lot = [[1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
distanceTraversed(lot)