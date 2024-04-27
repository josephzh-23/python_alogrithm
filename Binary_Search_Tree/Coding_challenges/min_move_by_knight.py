

'''
The trick to this problem:
the left most positino is -2 and right most is x + 2

obviously use DFS,



'''
from collections import deque

# this is the same as leetcode move 1197
# each knight has 8 moves it can make
# can add the moves to a directions

# given input as said x = 2, y = 1
# and slowly deal with this

'''
Knight can move up to 8 possible moves
when using bfs here
'''

row = 300
col = 300

def minMoves( x: int, y: int) -> int:
    # the offsets in the eight directions
    offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
               (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    visited = set()
    queue = deque([(0, 0)])
    steps = 0

    while queue:

        # this gives all the neighbors at current level
        curLevelCount = len(queue)
        # iterate through the current level
        for i in range(curLevelCount):
            curRow, curCol = queue.popleft()
            if (curRow, curCol) == (x, y):
                print(steps)

            for dx, dy in offsets:
                newRow, newCol = curRow + dx, curCol + dy
                if (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    queue.append((newRow, newCol))

        # move on to the next level
        steps += 1
    print(steps)
    return steps
minMoves(5, 5)











