package Graph

import java.util.*


//https://www.youtube.com/watch?v=ID9YJXy3OJk
fun main() {
    // using the Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main functino here
    var grid = arrayOf(
        intArrayOf(0, 0, 0),
        intArrayOf(1, 1, 0),
        intArrayOf(0, 0, 0),
        intArrayOf(0, 1, 1),
        intArrayOf(0, 0, 0)
    )
    println(shortestPathObstacle(grid, 1))
}

private val dirs = intArrayOf(-1, 0, 1, 0, -1)
fun shortestPathObstacle(grid: Array<IntArray>, k: Int): Int {
    val m = grid.size
    val n = grid[0].size
    val DIR = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
    val v = Array(m) {
        Array(n) {
            BooleanArray(
                k + 1
            )
        }
    }
    val q: Queue<IntArray> = LinkedList()
    var steps = 0
    q.offer(intArrayOf(0, 0, k))
    while (!q.isEmpty()) {
        var size = q.size
        while (size-- > 0) {
            val curr = q.poll()
            //If curr is the destination; return steps
            if (curr[0] == m - 1 && curr[1] == n - 1) return steps
            //Else go in all valid directions
            for (d in DIR) {
                val i = curr[0] + d[0]
                val j = curr[1] + d[1]
                val obs = curr[2]

                //Traverse through the valid cells
                if (i >= 0 && i < m && j >= 0 && j < n) {
                    //If cell is empty visit the cell and add in queue
                    if (grid[i][j] == 0 && !v[i][j][obs]) {
                        q.offer(intArrayOf(i, j, obs))
                        v[i][j][obs] = true
                    } else if (grid[i][j] == 1 && obs > 0 && !v[i][j][obs - 1]) {
                        q.offer(intArrayOf(i, j, obs - 1))
                        v[i][j][obs - 1] = true
                    }
                }
            }
        }
        ++steps
    }
    return -1
}