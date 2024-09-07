package Graph.dijkstra

import Graph.matrix
import java.util.*


var EightDirections =
    arrayOf(
        intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1),
        intArrayOf(1, 1),
        intArrayOf(-1, 1),
        intArrayOf(1, -1),
        intArrayOf(-1, -1)
    )


// Runs int he o(n) time complexity here
fun shortestPathBinaryMatrix(matrix: Array<IntArray>): Boolean {

    // given a start point here
//    var start = intArrayOf(1,1)
    // 1 and 1 are the starting point for this
    var visited = Array(matrix.size) { BooleanArray(matrix[0].size) }
    var start = intArrayOf(0, 0)
    var q: Queue<IntArray> = LinkedList()
    q.add(start)

    // We know the starting pt right here

    var count = 0

    visited[start[0]][start[1]] = true
    while (!q.isEmpty()) {

        // YOu need to print the node at that point
        count++
        for (i in 0 until q.size) {



            var node = q.poll()
            var x = node[0];
            var y = node[1]

            // When to return here
            if(x == matrix.size -1 && y == matrix[0].size -1){
                println("The count is " +count)
            }
            EightDirections.forEach { dir ->
                var dx = x + dir[0]
                var dy = y + dir[1]
                // Only add it if it's 1 then
                if (isInBoundsInt(matrix, dx, dy) && matrix[x][y] == 0) {
                    if (!visited[dx][dy]) {
                        println("removed node is ${matrix[dx][dy]} ")
                        visited[dx][dy] = true
                        q.offer(intArrayOf(dx, dy))
                    }
                }
            }
        }
    }
    println(count)
    return true
}

fun main() {

//    var binaryMatrix = arrayOf(
//        intArrayOf(0, 0, 0),
//        intArrayOf(1, 1, 0), intArrayOf(1, 1, 0)
//    )

    var binaryMatrix = arrayOf(
        intArrayOf(0, 1), intArrayOf(1, 0)
    )
    var binaryMatrix2 = arrayOf(
        intArrayOf(1, 0, 0),
        intArrayOf(1, 1, 0),
        intArrayOf(1, 1, 0)
    )
    shortestPathBinaryMatrix(binaryMatrix2)
    println("$")
}

// This makes sure no array out of bound exception here
fun isInBoundsInt(board: Array<IntArray>, x: Int, y: Int): Boolean {
    if (x < 0 || y < 0 || x >= board.size || y >= board[0].size) {
        return false
    } else return true
}
