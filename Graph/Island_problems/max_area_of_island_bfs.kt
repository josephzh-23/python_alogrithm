package Graph.Island_problems

import Graph.Islands.directions
import Graph.Islands.isInBoundsInt
import Graph.isInBoundsChar
import January_3rd.print
import java.util.*

/*
With the BFS approach, if a node= 1, put into a queue and
and set as 0 to mark visited.

Every time we poll from the queue
2. we check it and move in all 4 directions

3. Only add to the queue when it ==1 as said
4. Move in all 4 direciotns and then check and then see what's
going on
5. Move in all 4 direcitons as said and then ssee what's goin
g on

https://leetcode.com/problems/number-of-islands/description/
 */

// Using the bfs here and then


fun main() {

    var grid = arrayOf(intArrayOf(0,0,1,0,0,0,0,1,0,0,0,0,0),
        intArrayOf(0,0,0,0,0,0,0,1,1,1,0,0,0),
        intArrayOf(0,1,1,0,1,0,0,0,0,0,0,0,0),
        intArrayOf(0,1,0,0,1,1,0,0,1,0,1,0,0),
        intArrayOf(0,1,0,0,1,1,0,0,1,1,1,0,0),
        intArrayOf(0,0,0,0,0,0,0,0,0,0,1,0,0),
        intArrayOf(0,0,0,0,0,0,0,1,1,1,0,0,0),
        intArrayOf(0,0,0,0,0,0,0,1,1,0,0,0,0))

    maxAreaIsland2(grid).print()
}


fun maxAreaIsland2(grid: Array<IntArray>?): Int {
    if (grid == null || grid.size == 0) {
        return 0
    }
    var visited = Array(grid.size) { BooleanArray(grid[0].size) }

    var res = 0
    val row = grid.size
    val col = grid[0].size
    val q: Queue<IntArray> = LinkedList()
    for (i in 0 until row) {
        for (j in 0 until col) {
            if (grid[i][j] == 1) {

                // Whenever you see a 1 then you do a bfs and then
                // you get the max from that
                res = Math.max(res, bfs(grid, i, j, q, visited))

            }
        }
    }
    return res
}

// Will then pass a in a bfs here
fun bfs(grid: Array<IntArray>, i: Int, j: Int, q: Queue<IntArray>,
visited: Array<BooleanArray>): Int {
    var count = 0

    q.offer(intArrayOf(i, j))
    while (!q.isEmpty()) {
        val curr = q.poll()
        for (dir in directions) {
            val newRow = curr[0] + dir[0]
            val newCol = curr[1] + dir[1]
            if (isInBoundsInt(grid, newRow, newCol)
                && grid[newRow][newCol] == 1 && !visited[newRow][newCol]) {
                q.add(intArrayOf(newRow, newCol))
                count++
                // Mark as visited down here then
                visited[newRow][newCol] = true
            }
        }
    }
    return count
}
