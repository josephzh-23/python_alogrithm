package Graph.Island_problems

import January_3rd.print


/*
Approach 1 bad approach
1. WHenever you see a 1 then do a dfs here and then, but this is kind of
bad need to do a memoization trick when you see 1 here, since you might
end up with repeated work here
O(N^2) * O(n^2)

2. The better approach use some sort of an ids here
Say the islands is
1  1  1
1  0  0
0  1  1

{-1: 4, -2: 2}      -1 is for the one at the top
the max here  is 7 and then that's it
// And then here you have the code here a little bit better
 */

fun main() {
    var grid = arrayOf(intArrayOf(1, 0),
    intArrayOf(0, 1))
    var s = Solution16()
    s.largestIsland(grid).print()
}
internal class Solution16 {
    lateinit var grid: Array<IntArray>

    // Each islands with count will have an id here
    var id = -1
    var map: MutableMap<Int, Int> = HashMap()
    var m = 0
    var n = 0
    val DIRECTIONS = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
    fun largestIsland(grid: Array<IntArray>): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size

        // Step 1:
        //Find the size of each island and assign an id
        for (row in 0 until m) {
            for (col in 0 until n) {
                if (grid[row][col] == 1) {
                    val size = dfs(row, col)
                    map[id] = size
                    id-- //Update the id because id should be unique
                }
            }
        }

        //Find the max area by visit each 0
        var maxIsland = 0
        for (id in map.keys) maxIsland = Math.max(map[id]!!, maxIsland)

        for (row in 0 until m) {
            for (col in 0 until n) {
                if (grid[row][col] == 0) {
                    val curMaxIsland = calculateMaxIsland(row, col)
                    maxIsland = Math.max(maxIsland, curMaxIsland)
                }
            }
        }
        return maxIsland
    }

    private fun dfs(row: Int, col: Int): Int {
        //Base case
        if (row < 0 || row == m || col < 0 || col == n) return 0
        if (grid[row][col] != 1) return 0

        /*
         The grid here also got updated with teh corresponding id, making a
     grid with another id here,
         */
        grid[row][col] = id
        println("the id here is $id")

        //dfs all 4 directions
        val down = dfs(row + 1, col)
        val top = dfs(row - 1, col)
        val right = dfs(row, col + 1)
        val left = dfs(row, col - 1)
        return down + top + right + left + 1
    }

    private fun calculateMaxIsland(row: Int, col: Int): Int {
        val set: MutableSet<Int> = HashSet()
        for (direction in DIRECTIONS) {
            val curRow = direction[0] + row
            val curCol = direction[1] + col
            if (curCol < 0 || curRow == m || curRow < 0 || curCol == n) continue
            if (grid[curRow][curCol] == 0) continue
            val curId = grid[curRow][curCol]

//            println("the id here is $id")
            set.add(curId)
        }
        var sum = 0
        for (curId in set) {
            sum += map[curId]!!
        }
        return sum + 1
    }
}