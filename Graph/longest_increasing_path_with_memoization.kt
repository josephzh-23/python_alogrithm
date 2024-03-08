package Graph

// DFS + Memoization Solution
// Accepted and Recommended

// O (m n) the more optimized apporach as explained before
class Solutionee {
    private var m = 0
    private var n = 0
    fun longestIncreasingPath(matrix: Array<IntArray>): Int {
        if (matrix.size == 0) return 0
        m = matrix.size
        n = matrix[0].size
        val cache = Array(m) { IntArray(n) }
        var ans = 0
        for (i in 0 until m) for (j in 0 until n) ans = Math.max(ans, dfs(matrix, i, j, cache))
        return ans
    }

    private fun dfs(matrix: Array<IntArray>, i: Int, j: Int, cache: Array<IntArray>): Int {
        if (cache[i][j] != 0) return cache[i][j]
        for (d in dirs) {
            val x = i + d[0]
            val y = j + d[1]
            if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] > matrix[i][j]) cache[i][j] = Math.max(
                cache[i][j], dfs(matrix, x, y, cache)
            )
        }
        return ++cache[i][j]
    }

    companion object {
        private val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))
    }
}