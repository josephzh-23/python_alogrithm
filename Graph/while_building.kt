package Graph

import Graph.Island_problems.numIslands
import January_3rd.print
import java.util.*

fun main() {

    var grid = arrayOf(
        charArrayOf('1', '1', '0', '0', '0'),
        charArrayOf('1', '1', '0', '0', '0'),
        charArrayOf('0', '0', '1', '0', '0'),
        charArrayOf('0', '0', '0', '1', '1')
    )

    // Much faster when yo udo things this ways here
    bfsTrial(grid).print()
}

// This is how to do it when you use it with the visited array here
// # of islands right here
fun bfsTrial(grid: Array<CharArray>): Int {
    // and now working on this much easier to type around as said before

    // And then

    // The 4 directions up here  and then
    val directions = arrayOf(
        intArrayOf(1, 0),
        intArrayOf(0, 1),
        intArrayOf(-1, 0), intArrayOf(0, -1)
    )

    var count = 0

    val q: Queue<IntArray> = LinkedList()

    var row = grid.size
    var col = grid[0].size
//    var (row, col) = arrayOf(grid.size, grid[0].size)
    val visited = Array(row) { BooleanArray(col) }


    // Add the start to this first and then add other stuff
    // The visited stuff here that's good
    for (i in 0 until row) {
        for (j in 0 until col) {

            // When you see a one start counting
            // Then here you have

            if (grid[i][j] == '1') {
                // Then start counting
                count++
                q.add(intArrayOf(i, j))


                grid[i][j] = '2'
                // Mark as visited

                // And then start adding in all directions when q!empty
                while (!q.isEmpty()) {

                    val cur = q.poll()
                    directions.forEach {
                        val newRow = cur[0] + it[0]
                        val newCol = cur[1] + it[1]


                        // Make sure withint the bound here

                        if (isInBoundsChar(grid, newRow, newCol)
                            && grid[newRow][newCol] == '1'
                        ) {
                            // And not added here mark it as true if already
                            // visited here
//                            visited[newRow][newCol] = true
                            q.add(intArrayOf(newRow, newCol))
                            grid[newCol][newCol] = '2'
                        }
                    }
                }
            }
        }

    }
    return count
}

// Make sure eveything is in bounds here
fun isInBoundsChar(board: Array<CharArray>, x: Int, y: Int): Boolean {
    if (x < 0 || y < 0 || x >= board.size || y >= board[0].size) {
        return false
    } else return true
}