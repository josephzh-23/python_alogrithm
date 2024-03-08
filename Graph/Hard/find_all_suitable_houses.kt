package Graph.Hard

import Graph.Islands.directions
import java.util.*

/*
Step 1:
Iterate over all of the coordinates to find where all the houses are located
by checking

step 2:
once a house is found, increment house count by 1 to count the # of houses
present in the grid
put that in a hashset

step 3:
1. Conduct bfs on the grid by incrrementing the count by 1 here
 */


// what exactly is k: k is the number houses that are no more than k from all the houses in
// the neigbhorhood

fun main() {
    var houseGrid = arrayOf(
        intArrayOf(0, 0, 0, 0),
        intArrayOf(0, 0, 1, 0), intArrayOf(1, 0, 0, 1)
    )
    var s = Solution4(houseGrid)

    s.start(houseGrid)
}

class Solution4(houseGrid: Array<IntArray>) {

    var count = Array(houseGrid.size) { IntArray(houseGrid[0].size) }

    fun start(houseGrid: Array<IntArray>) {

        var res = 0


        val houseCoordinates = Array(houseGrid.size) { BooleanArray(houseGrid[0].size) }
        var k = 2
        var (m, n) = listOf(houseGrid.size, houseGrid[0].size)
        var houseCount = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (houseGrid[i][j] == 1) {

                    bfsSearch(houseGrid, i, j, k)
                    houseCount += 1
                    // Means we have visited here
                    houseCoordinates[i][j] = true
                }
            }
        }

        // DId the count actually chagne?
        for (i in 0 until m) {
            for (j in 0 until n) {

                println(count[i][j])
            }
        }
        println("house count is $houseCount")
        // And then the last part of this is here
        for (i in 0 until m) {
            for (j in 0 until n) {

                // We want to make sure we haven't visited this yet
                if (count[i][j] == houseCount && !houseCoordinates[i][j]) {
                    res += 1
                }
            }
        }
        println(res)


    }

    fun bfsSearch(matrix: Array<IntArray>, i: Int, j: Int, k: Int): Boolean {

        // given a start point here
//    var start = intArrayOf(1,1)
        // 1 and 1 are the starting point for this
        var visited = Array(matrix.size) { BooleanArray(matrix[0].size) }
        // everywhere when it starts ti will start with k here
        var start = intArrayOf(i, j, k)
        var q: Queue<IntArray> = LinkedList()
        q.add(start)

        // We know the starting pt right here


//        visited[start[0]][start[1]] = true
        while (!q.isEmpty()) {
            for (l in 0 until q.size) {


                val (x, y, k) = q.poll()
                // YOu need to print the node at that point

                // Basically whatever that's added to the queue meets the condition
                // that's listed below so we are good here
                if (!visited[x][y]) {

                    visited[x][y] = true
                    println("visited size ${visited.size}" +
                            "and the other one is ${count.size}")
//                    println("come here $x and $y")
                    count[x][y] += 1
                }
                directions.forEach { dir ->
                    val dx = x + dir[0]
                    val dy = y + dir[1]
                    val newK = k - 1
                    if (Graph.Basics.isInBoundsInt(matrix, dx, dy)
                        && newK >= 0 && !visited[dx][dy]
                    ) {
                        println("come here $dx and $dy")

                        q.offer(intArrayOf(dx, dy, k - 1))
                    }
                }
            }
        }
        return true
    }
}