package Graph.Island_problems

import java.util.*


/*

https://leetcode.com/problems/pacific-atlantic-water-flow/
This is the optimized approach
1. We only visit the cell that's valid
- basically the cell where height[cell] >= height[neigh]
2. Once visited we will mark it as 0

3. Have 2 sarapte arrays for this and then keep going
 */

internal class Solution15 {
    var dir = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(-1, 0))
    fun pacificAtlantic(matrix: Array<IntArray>?): List<List<Int>> {
        val res: MutableList<List<Int>> = ArrayList()
        if (matrix == null || matrix.size == 0 || matrix[0].size == 0) return res
        val row = matrix.size
        val col = matrix[0].size

        /*
        Have 2 matrixes for pacific and atlantic
        here
         */
        val pacific = Array(row) { BooleanArray(col) }
        val atlantic = Array(row) { BooleanArray(col) }

        //So basically we start from first and last row
        for (i in 0 until col) {
            dfs(matrix, 0, i, Int.MIN_VALUE, pacific)
            dfs(matrix, row - 1, i, Int.MIN_VALUE, atlantic)
        }
        //So basically we start from first and last row

        for (i in 0 until row) {
            dfs(matrix, i, 0, Int.MIN_VALUE, pacific)
            dfs(matrix, i, col - 1, Int.MIN_VALUE, atlantic)
        }

        // At the end here
        //Iterate and find the value true in both pac and alt
        //
        for (i in 0 until row) {
            for (j in 0 until col) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(Arrays.asList(i, j))
                }
            }
        }
        return res
    }

    fun dfs(matrix: Array<IntArray>, i: Int, j: Int, prev: Int, ocean: Array<BooleanArray>) {

        // Check for boundary condi
        if (i < 0 || i >= ocean.size || j < 0 || j >= ocean[0].size) return


        /*
          Check if we can go to the location
          ocean[i][j] == true if already visited
         */
        if (matrix[i][j] < prev || ocean[i][j]) return
        ocean[i][j] = true
        // call Graph.Edges_question.dfs on all 4 direcions this is amazing wow really fast

        for (d in dir) {
            dfs(matrix, i + d[0], j + d[1], matrix[i][j], ocean)
        }
    }
}