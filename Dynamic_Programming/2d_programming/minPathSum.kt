package Dynamic_programming.`2d_programming`

//  https://leetcode.com/problems/minimum-path-sum/
fun main() {
    var g = arrayOf(intArrayOf(1, 3, 1),
    intArrayOf(1, 5, 1), intArrayOf(4, 2,1))
    println(minPathSum(g))
}
fun minPathSum(grid: Array<IntArray>?): Int {
    val rows = grid!!.size
    val cols = grid[0].size
    if (grid == null || grid.size == 0) {
        return 0
    }
    val dp = Array(grid.size) { IntArray(grid[0].size) }
    // 1st elem starting pt
    dp[0][0] = grid[0][0]

    // Fill the first row here
    for (i in 1 until cols) {
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    }
    // Fill first col
    for (i in 1 until rows) {
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    }
    // Now fill the rest of the cell
    for (i in 1 until rows) {
        for (j in 1 until cols) {
            dp[i][j] = grid[i][j] + Math.min(dp[i - 1][j],
                    dp[i][j - 1])
        }
    }
    return dp[rows - 1][cols - 1]
}