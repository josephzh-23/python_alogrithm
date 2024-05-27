'''
Then using htis

Breath over depth (level by level) here

'''
from collections import deque
from typing import List


def orangeRotting(grid: List[List[int]])-> int:
    q = deque()

    time, fresh = 0, 0

    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh+=1
            if grid[r][c] == 2:
                q.append([r, c])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()

            for dr, dc in directions:

                row, col = dr + r, dc + c

                # if in bounds and fresh make rotten
                if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                    continue


                # when fresh orange grid[row][col]==1 , we make it orange by making it 2 here.
                # this becomes one so we don't touch it again for a long time
                grid[row][col] =2
                q.append([row, col])
                fresh -=1

        # at each level we increment the level 1 by 1 here 
        time +=1


    return time if fresh == 0 else -1




















