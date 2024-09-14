'''

This quesitno consists of the answer that
we just need to find out the min distance between start node and final target node "123450".

Every time we swap 0 position in the String to find the next state.
Use a hashTable to store the visited states.

Use a hashtable to store the state here
'''
from collections import deque
from typing import List


def distanceTraversed(lot: List[List[int]]) -> int:


    n, m = len(lot), len(lot[0])

    # basically to go up, down left and right
    # this is the basic direction right here
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

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
                q.append([numRow, numCol, curDist + 1])
                visited.add((numRow, numCol))

    return -1
lot = [[1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1]]