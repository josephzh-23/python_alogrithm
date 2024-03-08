package Graph.multi_source_bfs

import java.util.*

// Running mutliple source bfs
/*
Better to use the answer from leetcode more stable
Only add rotten oranges to the game
how to know when finished?      keep track of # of fresh ones initially

1. We need to add the # of fresh variables here
2.
 */
fun orangesRotting(grid: Array<IntArray>): Int {
    // will try not to modify directly here

    var time = 0

    // This has to be 0 by the end
    var countFresh = 0



    // We want to find the # of fresh oranges
    val q: Queue<IntArray> = LinkedList()
    for (i in 0 until grid.size) {
        for (j in 0 until grid[i].size) {
            // Then add to the fresh oranges
            if (grid[i][j] == 1) {

                // Add to the count fresh here
                countFresh++
            } else if (grid[i][j] == 2) {

               q.add(intArrayOf(i ,j))
            }
        }
    }

    val row = grid.size
    val col = grid[0].size

    // Move in 4 directions
    val directions = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
    while (!q.isEmpty()&& countFresh >0) {

        // Because doing this allows us to
        for(i in q.indices) {
            val curr = q.poll()

            for (dir in directions) {
                val newRow = curr[0] + dir[0]
                val newCol = curr[1] + dir[1]

                // meaning if we run into a fresh orange then make rotten
                if (newRow >= 0 && newRow < row && newCol >= 0 && newCol < col && grid[newRow][newCol] == 1) {

                    // Mark sth as 2 so now it's rotten as well here
                    grid[newRow][newCol] = 2
                    q.add(intArrayOf(newRow, newCol))
                    countFresh -= 1

                }
            }
        }
        // increase the time by 1
        time++
    }

    return if(countFresh ==0) time else -1
}


fun main() {
    var arr = arrayOf(intArrayOf(2, 1, 1),
    intArrayOf(1,1, 0),
    intArrayOf(0, 1,1))
    println(orangesRotting(arr))
}

