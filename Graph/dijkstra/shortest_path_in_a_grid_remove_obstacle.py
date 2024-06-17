import collections


'''
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/


Wathc cracking fanng video at 10th minute where he 
explains why a need for the state variable
'''

def shortestPath(s, grid, k) ->int:
    rows= len(grid)
    cols = len(grid[0])

    target = (rows-1, cols-1)

    if k >= (rows -1) + (cols -1):
        return rows + cols -2
    '''
    Checking for the same position (if visited)won't be enough
    also need to check for # of obstacles removed
        
        
    0 -> 0          0   0
                    |   |
                    1 - 0
    When we are going in the above: going from 0 to 0 and 0-> 1-> 0-> 0
    is very different indeed
    
The reason why we need the state as above 
    on left: 0 obstacles removed
    on right: 1 obstacle removed    but both end up at position (1, 0)
    t
    '''
    '''
    Here using the tuple here 
    0 : total steps taken
    2nd : current state of our path
    '''
    q = collections.deque([(0,(0, 0, k) )])

    seen = set([(0, 0, k)])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    while q:
        steps, (row, col, removalLeft) = q.popleft()

        if (row, col) == target:
            return steps

        for rowInc, colInc in directions:
            newRow = row + rowInc
            newCol = col + colInc

            if (0 <= newRow < rows) and (0 <= newCol < cols):
                newRemoval = removalLeft - grid[newRow][newCol]
                newState = (newRow, newCol, newRemoval)

                # still within the k obstacles
                if newRemoval >= 0 and newState not in seen:
                    seen.add(newState)
                    q.append((steps + 1, newState))

    return -1


# T: O(n) * (k) = O (n* k)
# T  O (n) * k = O(n*k)








