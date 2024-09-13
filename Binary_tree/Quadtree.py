class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

'''

Quad tree problem here how to implement in a good way 

True here

isLeaf: check if the node leaf here
From a 2d here

We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's)
set isLeaf True and set val to the value of the grid and set the four children to Null and stop.

If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.


 grid = [[0,1],[1,0]]
'''

class Solution:
    # Returns true if all the values in the matrix are the same; otherwise, false.
    def sameValue(s, grid, x1, y1, length):
        for i in range(x1 + length):
            for j in range(y1 + length):
                if grid[i][j] != grid[x1][y1]:
                    return False
        return True

    def solve(s, grid, x1, y1, length):
        # Return a leaf node if all values are the same.
        if s.sameValue(grid, x1, y1, length):
            return Node(grid[x1][y1] == 1, True)
        else:
            root = Node(False, False)

            # Recursive call for the four sub-matrices.
            root.topLeft = s.solve(grid, x1, y1, length // 2);
            root.topRight = s.solve(grid, x1, y1 + length // 2, length // 2);
            root.bottomLeft = s.solve(grid, x1 + length // 2, y1, length // 2);
            root.bottomRight = s.solve(grid, x1 + length // 2, y1 + length // 2, length // 2);

            return root;

    def construct(s, grid):
        return s.solve(grid, 0, 0, len(grid))


'''
Input and output here 
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
'''
c = Solution()
grid = [[0, 1], [1, 0]]
answer = c.construct(grid)

print(answer.topRight)