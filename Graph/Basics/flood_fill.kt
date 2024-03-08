package Graph.Basics


import Basics.printMatrix
import Graph.Islands.directions
import java.util.*


//var matrix = arrayOf(
//        intArrayOf(1, 1, 1, 1),
//        intArrayOf(1, 0, 0, 0),
//        intArrayOf(1, 0, 0, 0),
//        intArrayOf(1, 0, 0, 0),
//);

var matrix2 = arrayOf(
    intArrayOf(1, 1, 1),
    intArrayOf(1, 1, 0), intArrayOf(1, 0, 1)
)
fun main() {
    floodFill(matrix2, 2)
}

// Using the bfs adjacency matrix here
// THis one will work for sure 100% as said
fun floodFill(matrix: Array<IntArray>, color: Int): Boolean {


    // since we will be updating this matrix here
    var matrix = matrix
    // 1 and 1 are the starting point for this
    var visited = Array(matrix.size) { BooleanArray(matrix[0].size) }
    var start = intArrayOf(1, 1)
    var q: Queue<IntArray> = LinkedList()
    q.add(start)

    // We know the starting pt right here


    visited[start[0]][start[1]] = true
    // Since this is the starting pt we will hard code it here
    matrix[1][1] = 2
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

                    if (matrix[dx][dy] + 1 == color) {
                        visited[dx][dy] = true
                        matrix[dx][dy] = color
                        q.offer(intArrayOf(dx, dy))
                    }
                }
            }
        }
    }
    printMatrix(matrix)
    return true
}







