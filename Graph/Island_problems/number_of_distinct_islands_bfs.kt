package Graph.Island_problems

import java.util.*


internal class Solution33 {
    val WATER = 0
    val LAND = 1
    var m = 0
    var n = 0
    var baseRow = 0
    var baseCol = 0
    lateinit var grid: Array<IntArray>
    val DIRECTIONS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    fun numDistinctIslands(grid: Array<IntArray>): Int {
        m = grid.size
        n = grid[0].size
        val shapes: MutableSet<String> = HashSet()
        this.grid = grid

        //Find each islands
        for (row in 0 until m) {
            for (col in 0 until n) {
                if (grid[row][col] == WATER) continue
                baseRow = row
                baseCol = col
                val sb = StringBuilder()
                bfs(row, col, sb)
                shapes.add(sb.toString())
            }
        }

        //return unique islands
        return shapes.size
    }

    private fun bfs(row: Int, col: Int, sb: StringBuilder) {
        val queue: Queue<IntArray> = LinkedList()
        queue.add(intArrayOf(row, col))
        grid[row][col] = WATER

        //Perform BFS
        while (!queue.isEmpty()) {
            //Get first position
            val curPos = queue.poll()
            sb.append(curPos[0] - baseRow)
            sb.append(curPos[1] - baseCol)
            //Add all its neighbors (all 4 directions)
            for (direction in DIRECTIONS) {
                val curRow = curPos[0] + direction[0]
                val curCol = curPos[1] + direction[1]
                if (validPosition(curRow, curCol)) {
                    queue.add(intArrayOf(curRow, curCol))
                    grid[curRow][curCol] = WATER
                }
            }
        }
    }

    private fun validPosition(row: Int, col: Int): Boolean {
        if (row < 0 || col < 0 || row == m || col == n) return false
        return if (grid[row][col] == WATER) false else true
    }
}