from collections import deque



'''
remember 1 means that it's blocked 
'''

def minMoves(grid) -> int:
    # part 1 here and then
    offsets = [(0, 1), (1, 0), (1, 1)]
    visited = set()
    queue = deque([(0, 0)])
    steps = 0

    n, m = len(grid), len(grid[0])

    while queue:

        # this gives all the neighbors at current level
        curLevelCount = len(queue)
        # iterate through the current level
        for i in range(curLevelCount):
            curRow, curCol = queue.popleft()
            if (curRow, curCol) == (n, m):
                print(steps)

            for dx, dy in offsets:
                newRow, newCol = curRow + dx, curCol + dy


                if (newRow, newCol) not in visited and 0<= newRow < n and 0 <= newCol < m:
                    if grid[newRow][newCol] == 1:
                        continue
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))

        # move on to the next level
        steps += 1
    print(steps)
    return steps

minMoves([[0, 1], [1,0]])
