'''


There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
 tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
Input: m = 3, n = 7
Output: 28

This is sort of the backtracking solutino here


Brute force approach solution with
O (2 ^m * 2^n) the brute force solution here
-
'''

class Solution():
    count = 0
    def uniquePath(s, m, n):
        s.backtrack(0, 0, m, n)
        return s.count

    def backtrack(s, row, col, m, n):

        if row == m -1 and col == n- 1:
            s.count+=1
            return
        if (row >= m or col >= n): return
        s.backtrack(row, col + 1, m, n)
        s.backtrack(row + 1, col, m, n)