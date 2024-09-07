from collections import deque

'''
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

'''

class Solution:
    def minimumObstacles(self, grid):
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Initialize a queue with the starting point and 0 obstacles encountered
        queue = deque([(0, 0, 0)])

        # Create a set to keep track of visited cells
        visited = set()

        # Define the directions to move in the grid, pairwise will use this

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Loop until we find the exit or run out of cells to explore
        while queue:
            # Pop the cell from the queue and count of obstacles encountered so far
            i, j, obstacle_count = queue.popleft()

            # If we've reached the bottom right corner, return the obstacle count
            if i == rows - 1 and j == cols - 1:
                return obstacle_count

            # If this cell has been visited before, skip to the next iteration
            if (i, j) in visited:
                continue

            # Mark the current cell as visited
            visited.add((i, j))

            # Iterate over all possible moves (up, down, left, right)
            for dx, dy in directions:
                x, y = i + dx, j + dy

                # Check if the new position is within bounds
                if 0 <= x < rows and 0 <= y < cols:
                    # If there is no obstacle, add the cell to the front of the queue to explore it next
                    if grid[x][y] == 0:
                        queue.appendleft((x, y, obstacle_count))
                    # If there is an obstacle, add the cell to the back of the queue with the obstacle count incremented
                    else:
                        queue.append((x, y, obstacle_count + 1))

# If running Python version earlier than 3.10, define your pairwise function like this:
# def pairwise(iterable):
#     "s -> (s0,s1), (s1,s2), (s2, s3), ..."
#     a, b = tee(iterable)
#     next(b, None)
#     return zip(a, b)

# Note: The pairwise function returns consecutive pairs of elements from the input.
# For the directions in this code, it's used to generate the pairs (up, right), (right, down),
# (down, left), and (left, up) to traverse the grid in a clockwise manner.