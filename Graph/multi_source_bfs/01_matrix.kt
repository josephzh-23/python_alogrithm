package Graph.multi_source_bfs

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
            intArrayOf(0, 0, 0),
            intArrayOf(0, 1, 0), intArrayOf(0, 0, 0)
    )
    var s = Solution4(houseGrid)

    s.start(houseGrid)
}

class Solution4(matrix: Array<IntArray>) {

    // For this question we can start a bfs from 0 as said here
    // And then we keep going here until reaching the destinatino
    // The count will keep track of all the grid here as said
    var count = Array(matrix.size) { IntArray(matrix[0].size) }

    fun start(houseGrid: Array<IntArray>) {

        var res = 0


        val houseCoordinates = Array(houseGrid.size) { BooleanArray(houseGrid[0].size) }
        var (i , j) = listOf(0, 0)
        var k = 0
        var (m, n) = listOf(count.size, count[0].size)
        var houseCount = 0

        houseCoordinates[i][j] = true
        bfsSearch(houseGrid, i, j, k)

        for(i in 0 until m){
            for(j in 0 until n){
                println(count[i][j])
            }
        }

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


                    count[x][y] += 1
                }
                directions.forEach { dir ->
                    val dx = x + dir[0]
                    val dy = y + dir[1]
                    val newK = k +1
                    if (Graph.Basics.isInBoundsInt(matrix, dx, dy) && !visited[dx][dy]) {

                        q.offer(intArrayOf(dx, dy, newK))
                    }
                }
            }
        }
        return true
    }
}