package Graph.Basics

import Graph.Islands.directions
import January_3rd.print
import java.util.*

// See if we can do this with bfs approach as said before
// Empty space = 0 and obstacle = 1
var matrix = arrayOf(
    intArrayOf(0, 0, 1, 0, 0),
    intArrayOf(0, 0, 0, 0, 0),
    intArrayOf(0, 0, 0, 1, 0),
    intArrayOf(1, 1, 0, 1, 1),
    intArrayOf(0, 0, 0, 0, 0)
);

fun main() {

    // The maze here
    var start = intArrayOf(0, 4)
    var dest = intArrayOf(3, 2)

    searchMatrix(matrix, start, dest).print()
}


// Using the bfs adjacency matrix here
// THis one will work for sure 100% as said
fun searchMatrix(matrix: Array<IntArray>, start: IntArray, end: IntArray): Boolean {

    //
    var visited = Array(matrix.size) { BooleanArray(matrix[0].size) }
    var q: Queue<IntArray> = LinkedList()
    q.add(start)

    // We know the starting pt right here


    visited[start[0]][start[1]] = true
    while (!q.isEmpty()) {
        var node = q.poll()
        var x = node[0];
        var y = node[1]
        // YOu need to print the node at that point

        if (x == end[0] && y == end[1]) {
            return true
        }

        directions.forEach { dir ->
            var dx = x + dir[0]
            var dy = y + dir[1]
            while (isInBoundsInt(matrix, dx, dy) && matrix[dx][dy] == 0) {

                // This allows you to keep going in that direction
                // until you hit a wall as said
                dx += dir[0]
                dy += dir[1]
            }

            // So when it hits the wall take a step back and then add it to the path
            dx -= dir[0]
            dy -= dir[1]
            if (!visited[dx][dy]) {
                visited[dx][dy] = true
                q.offer(intArrayOf(dx, dy))
            }
        }
    }
    return false
}


// This makes sure no array out of bound exception here
fun isInBoundsInt(board: Array<IntArray>, x: Int, y: Int): Boolean {
    if (x < 0 || y < 0 || x >= board.size || y >= board[0].size) {
        return false
    } else return true
}



