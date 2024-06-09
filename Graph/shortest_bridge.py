'''
Step 1: (DFS) here
Identify and separet the first 2 islands here
1. Find the island with 1 here
- Find island with 1 here and then once you find it,

Once we find it, we perform a DFS starting from that cell to mark all connected
 land cells as part of the same island.
    - For clarity, we mark these cells with a 2.

For every cell marked as 2, continue the dfs here

Step 2: (BFS) step here

ans: keep track of the # of flips required here and then this is very important here

Use bfs to build bridge to 2nd island
- after making ti then we go,
During the BFS, we dequeue cells from q and explore their neighbors in all four directions. We have three cases for each neighbor:

If cell is 0 here:
If the cell is water (0),
we flip it to (2) to indicate it is now part of the bridge and add it to the queue for further exploration.

If cell is 1:
If the cell is a part of the unvisited island (1),
we have reached the second island, and we return the ans variable because
we found the minimal number of flips to connect the two islands.

If cell is 2:
If the cell is already included in the bridge or is a part of the isolated island (2),
 we ignore it and continue.
- adn then here



'''
from collections import deque


class Solution:
    def shortestBridge(self, grid):
        '''
        Step 1 here and then just add some data
        '''
        # Depth-first search function to mark the first island
        def dfs(i, j):

            queue.append((i, j))
            grid[i][j] = 2


            for k in range(4):
                x, y = i + directions[k], j + directions[k + 1]

                # if it's one then we just keep doing this
                if 0 <= x < size and 0 <= y < size and grid[x][y] == 1:
                    dfs(x, y)

        size = len(grid)
        # Directions for exploring neighboring cells (right, down, left, up)
        directions = [0, 1, 0, -1, 0]
        queue = deque()

        # Find the first 1 in the grid to start the DFS
        start_i, start_j = next((i, j) for i in range(size) for j in range(size) if grid[i][j] == 1)

        # Run DFS to find one island and mark it as 2
        dfs(start_i, start_j)

        steps = 0  # Number of steps required to connect the two islands
        # BFS to expand the first island
        while True:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k in range(4):


                    x, y = i + directions[k], j + directions[k + 1]
                    if 0 <= x < size and 0 <= y < size:

                        # When we find the second island, return the number of steps so the bridge connection is done here 
                        if grid[x][y] == 1:
                            return steps
                        # If water is found, mark it as part of the first island and add to the queue
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            queue.append((x, y))
            steps += 1
