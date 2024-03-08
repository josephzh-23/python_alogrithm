package Graph

import Graph.Islands.directions
import java.util.*


var matrix = arrayOf(
    intArrayOf(1, 1, 1, 1),
    intArrayOf(1, 0, 0, 0),
    intArrayOf(1, 0, 0, 0),
    intArrayOf(1, 0, 0, 0)

);


// Using the bfs adjacency matrix here
// THis one will work for sure 100% as said
fun searchMatrix(matrix: Array<IntArray>): Boolean {

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
        var node = q.poll()
        var x = node[0];
        var y = node[1]
        // YOu need to print the node at that point


        directions.forEach { dir ->
            var dx = x + dir[0]
            var dy = y + dir[1]
            if (isInBoundsInt(matrix, dx, dy)) {
                if (!visited[dx][dy]) {
                    println("removed node is ${matrix[dx][dy]} ")
                    visited[dx][dy] = true
                    q.offer(intArrayOf(dx, dy))
                }
            }
        }
    }
    return true
}

fun main() {
    searchMatrix(matrix)
    println("$")
}

// This makes sure no array out of bound exception here
fun isInBoundsInt(board: Array<IntArray>, x: Int, y: Int): Boolean {
    if (x < 0 || y < 0 || x >= board.size || y >= board[0].size) {
        return false
    } else return true
}








