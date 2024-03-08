package Graph

import January_3rd.print
import java.util.*


fun main() {
    // using the Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main functino here
    var grid = arrayOf(
        charArrayOf('x', 'x', 'x', 'x', 'x', 'x'),
        charArrayOf('x', '*', 'o', 'o', 'o', 'x'),
        charArrayOf('x', 'o', 'o', '#', 'o', 'x'),
        charArrayOf('x', 'x', 'x', 'x', 'x', 'x')
    )
    println(getFood(grid)).print()
}

private val dirs = intArrayOf(-1, 0, 1, 0, -1)

fun getFood(grid: Array<CharArray>): Int {
    val rows = grid.size
    val columns = grid[0].size
    val visited = Array(rows) {
        BooleanArray(
            columns
        )
    }
    var startRow = -1
    var startColumn = -1
    val total = rows * columns
    for (i in 0 until total) {
        val row = i / columns
        val column = i % columns
        if (grid[row][column] == '*') {
            startRow = row
            startColumn = column
            break
        }
    }
    visited[startRow][startColumn] = true
    val queue: Queue<IntArray> = LinkedList()
    queue.offer(intArrayOf(startRow, startColumn))
    val directions = arrayOf(intArrayOf(-1, 0), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(0, 1))
    var steps = 0
    while (!queue.isEmpty()) {
        val size = queue.size
        /*
        The reason for traversing level if you can end up at the
        same place but having taken different number of steps

         */
        for (i in 0 until size) {
            val cell = queue.poll()
            val row = cell[0]
            val column = cell[1]
            if (grid[row][column] == '#') return steps
            for (direction in directions) {
                val newRow = row + direction[0]
                val newColumn = column + direction[1]
                if (newRow >= 0 && newRow < rows && newColumn >= 0 &&
                        newColumn < columns && grid[newRow][newColumn] != 'X' && !visited[newRow][newColumn]) {
                    visited[newRow][newColumn] = true
                    queue.offer(intArrayOf(newRow, newColumn))
                }
            }
        }
        steps++
    }
    return -1
}
