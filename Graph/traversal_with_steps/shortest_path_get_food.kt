package Graph.traversal_with_steps

import Graph.Islands.directions
import java.util.*
//https://leetcode.com/problems/shortest-path-to-get-food/description/
// Need to add both i, j and the # of step for the q here
fun getFood(grid: Array<CharArray>): Int {
    var count = 0
    var rowSize = grid.size
    var colSize = grid[0].size
    var startRow = -1
    var startCol = -1
    // This needs to take in 3 values here
    val q = LinkedList<IntArray>()
    for (i in 0 until rowSize) {
        for (j in 0 until colSize) {
            if (grid[i][j] == '*') {
                println("$i and $j")
                q.add(intArrayOf(
                        i, j,0
                ))
                startRow = i
                startCol =j
                break

            }
        }
    }
    val visited = Array(rowSize) { BooleanArray(colSize) }
    visited[startRow][startCol] = true
    while (!q.isEmpty()) {
        var size = q.size
            var node = q.poll()
            var row = node[0];
            var col = node[1]
            var steps = node[2]
            if (grid[row][col] == '#') {
                return steps
            }

            directions.forEach { dir ->
                var newRow = row + dir[0]
                var newCol = col + dir[1]
                if(!isOutofBounds(grid, newRow, newCol) &&
                        grid[newRow][newCol] != 'X' ){
                    if( !visited[newRow][newCol]) {
                        visited[newRow][newCol] == true
                        q.add(intArrayOf(
                                newRow, newCol, steps+1
                        ))
                    }
                }
            }

    }
    // That means nothing is found
    return -1
}

fun isOutofBounds(board: Array<CharArray>, x: Int, y:Int): Boolean {
    return (x< 0 || x> board.size-1 || y< 0 || y> board[0].size -1)
}

fun main() {
    // using the Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main functino here
    var grid = arrayOf(charArrayOf('x', 'x', 'x','x', 'x', 'x'),
            charArrayOf('x', '*', 'o','o', 'o', 'x') ,
            charArrayOf('x', 'o', 'o','#', 'o', 'x'),
            charArrayOf('x', 'x', 'x','x', 'x', 'x'))
    println(getFood(grid))
}