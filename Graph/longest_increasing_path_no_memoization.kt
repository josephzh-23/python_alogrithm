package Graph

import January_3rd.print

// This is the native approach here
// These 2 will be the sizes and then assigned there
// Naive DFS Solution
// Time Limit Exceeded

fun main() {
    var s = Solution134()

    var g = arrayOf(
        intArrayOf(9, 9, 4),
        intArrayOf(6, 6, 8),
        intArrayOf(2, 2, 1)
    )
    s.longestIncreasingPath(g).print()

}

class Solution134 {
    private var m = 0
    private var n = 0
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        if (matrix.size == 0) return 0
        m = matrix.size
        n = matrix[0].size
        var ans = 0
        for (i in 0 until m)
            for (j in 0 until n)
                ans = Math.max(ans, dfs(matrix, i, j))
        return ans
    }

    private fun dfs(matrix: Array<IntArray>, i: Int, j: Int): Int {
        var ans = 0
        for (d in dirs) {
            val x = i + d[0]
            val y = j + d[1]
            if (x in 0 until m && y in 0 until n && matrix[x][y] > matrix[i][j]) {
                ans = Math.max(ans, dfs(matrix, x, y))
                println(ans)
            }

        }

        // Storing the answer in here too
        return ++ans
    }

    companion object {
        private val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
    }
}