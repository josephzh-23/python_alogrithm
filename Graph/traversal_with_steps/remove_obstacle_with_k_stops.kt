import java.util.*

// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

/*

 Checking for the same position (if visited)won't be enough
    also need to check for # of obstacles removed

    Why do we need to store the state?
    0 -> 0          0   0
                    |   |
                    1 - 0

The reason why we need the state as above
    on left: 0 obstacle removed
    on right: 1 obstacle removed    even though both end up at (0, 1)
 */
    fun shortestPath(grid: Array<IntArray>, k: Int): Int {
        val m = grid.size
        val n = grid[0].size
        val DIR = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))

        // This is a 3d vector basically
        val v = Array(m) { Array(n) { BooleanArray(k + 1) } }

        // Our q would store sth like, this would store the obstacles left
        val q: Queue<IntArray> = LinkedList()
        var steps = 0


        // q = collections.deque([((0, 0, k) )])
        // Storing the state here as explained before
        q.offer(intArrayOf(0, 0, k))
        while (!q.isEmpty()) {
            var size = q.size
            while (size-- > 0) {

                // No need to iterate through each level in the queue since k number of steps in the queue
                val curr = q.poll()
                //If curr is the destination; return steps
                if (curr[0] == m - 1 && curr[1] == n - 1) return steps
                for (d in DIR) {
                    val newRow = curr[0] + d[0]
                    val newCol = curr[1] + d[1]
                    val obs = curr[2]

                    //Traverse through the valid cells
                    if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {

                        //If cell is empty visit the cell and add in queue
                        if (grid[newRow][newCol] == 0 && !v[newRow][newCol][obs]) {

                            // grid[r][c] could be 1 here (the grid) as shown
                            // seen[row][col] == 1 as explained before then
                            // update the o at each step
                            q.offer(intArrayOf(newRow, newCol, obs))
                            v[newRow][newCol][obs] = true

                            // Each time we run -> obstacles
                            // Run into a grid[i][j] == 1 situation
                            // Still have obstacles left with us and that position not visited
                        } else if (grid[newRow][newCol] == 1 && obs > 0 && !v[newRow][newCol][obs - 1]) {

                            q.offer(intArrayOf(newRow, newCol, obs - 1))
                            v[newRow][newCol][obs - 1] = true
                        }
                    }
                }
            }
            ++steps
        }
        return -1
    }