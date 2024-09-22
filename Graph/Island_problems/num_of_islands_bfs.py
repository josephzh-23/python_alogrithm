package Graph.Islands

import java.util.*

/*
With the BFS approach, if a node= 1, put into a queue and
and set as 0 to mark visited.

Every time we poll from the queue
2. we check it and move in all 4 directions

3. Only add to the queue when it ==1 as said
4. Move in all 4 direciotns and then check and then see what's
going on
5. Move in all 4 direcitons as said and then ssee what's goin
g on

https://leetcode.com/problems/number-of-islands/description/
 */

// Using the bfs here and then

fun numIslands(grid: Array<CharArray>?): Int {
    if (grid == null || grid.size == 0) {
        return 0
    }
    var count = 0
    val row = grid.size
    val col = grid[0].size

    // Move in 4 directions
    val directions = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
    val qu: Queue<IntArray> = LinkedList()
    for (i in 0 until row) {
        for (j in 0 until col) {
            if (grid[i][j] == '1') {
                count++
                qu.add(intArrayOf(i, j))

                // mark as visited
                grid[i][j] = '2'
                while (!qu.isEmpty()) {
                    val curr = qu.poll()
                    for (dir in directions) {
                        val newRow = curr[0] + dir[0]
                        val newCol = curr[1] + dir[1]
                        if (newRow >= 0 && newRow < row && newCol >= 0 && newCol < col && grid[newRow][newCol] == '1') {
                            qu.add(intArrayOf(newRow, newCol))

                            // Mark sth as 2 basically saying it hasn't
                            // been visited here essentiallly
                            grid[newRow][newCol] = '2'
                        }
                    }
                }
            }
        }
    }
    return count.also{println(it)}
}

fun main() {
    var grid = arrayOf(charArrayOf('1','1','0','0','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0', '0', '1', '0', '0'),
            charArrayOf('0', '0', '0', '1', '1'))

    numIslands(grid)
    // and using this we can have the data sent here
}