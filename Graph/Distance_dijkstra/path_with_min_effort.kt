package Graph.dijkstra

import Graph.Islands.directions
import java.lang.Integer.max
import java.lang.Math.abs
import java.util.*


fun main() {
    var heights = arrayOf(intArrayOf(1, 2, 3),
    intArrayOf(3, 8, 4),
    intArrayOf(5, 3, 5))
    pathWithMinEfforts(heights)
}

/*

In this quesiton, use a minimum diffMatrix where each cell :
min effort required to reach that cell from all possible paths
 */
fun pathWithMinEfforts(heights: Array<IntArray>): Int {

    var row = heights.size
    var col = heights[0].size

    // the difference matrix here represents the min effort it takes to
    // reach that cell
    val differenceMatrix = Array(heights.size) { IntArray(heights[0].size) }
    for(row in differenceMatrix){
        Arrays.fill(row, Int.MAX_VALUE)
    }

    differenceMatrix[0][0] = 0
    var visited = Array(heights.size) { BooleanArray(heights[0].size) }
    var start = intArrayOf(0, 0)
    var q: Queue<IntArray> = LinkedList()
    q.add(start)

    // We know the starting pt right here


    // To process the edges first turn them into graph?
    val adj: MutableMap<Int, MutableList<IntArray>?> = HashMap()

    // We can add the smallest difference here
    val pq = PriorityQueue { a: IntArray, b: IntArray ->
        a[2] - b[2]
    }

    var maxDiff = 0
    // {the node, the diff between this and previous }
    pq.offer(intArrayOf(0, 0,  0))
    while (!pq.isEmpty()) {
        val temp = pq.poll()
        val x = temp[0]
        val y = temp[1]
        val diff = temp[2]


        // Need to store the number of steps for that node in particular here
        // SO no more processing if sth similar occurs here
        if (x == heights.size -1  && y == heights[0].size-1 ) return diff




        directions.forEach { dir ->
            var dx = x + dir[0]
            var dy = y + dir[1]
            if (isInBoundsInt(heights, dx, dy)) {
                if (!visited[dx][dy]) {
                    println("removed node is ${heights[dx][dy]} ")
                    visited[dx][dy] = true

                    var curDiff = abs(heights[dx][dy] - heights[x][y])
                    maxDiff = max(curDiff, differenceMatrix[x][y])

                    /*
                     Make sure the diff matirx at that point always
                     smallest here
                     */
                    if(differenceMatrix[dx][dy] > maxDiff){
                        differenceMatrix[dx][dy] = maxDiff
                        q.offer(intArrayOf(dx, dy, abs(heights[dx][dy] - heights[x][y])))

                    }
                }
            }
        }
    }
    print(maxDiff)
    return differenceMatrix[row-1][col -1]

}