package Graph.Island_problems


internal class Solution32 {
    // O - Water or out of bounds
    // X - start of an island
    // L - Left
    // R - Right
    // U - up
    // D - Down
    fun numDistinctIslands(grid: Array<IntArray>?): Int {
        if (grid!!.size == 0 || grid == null) {
            return 0
        }
        val m = grid.size
        val n = grid[0].size
        val set: MutableSet<String?> = HashSet()
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1) {
                    val sb = StringBuilder()
                    calculatePath(i, j, m, n, "X", grid, sb)
                    set.add(sb.toString())
                }
            }
        }
        return set.size
    }

    fun calculatePath(i: Int, j: Int, m: Int, n: Int, direction: String?, grid: Array<IntArray>, sb: StringBuilder) {
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == 0) {
            sb.append("O")
            return
        }
        sb.append(direction)
        grid[i][j] = 0
        calculatePath(i, j - 1, m, n, "L", grid, sb)
        calculatePath(i, j + 1, m, n, "R", grid, sb)
        calculatePath(i - 1, j, m, n, "U", grid, sb)
        calculatePath(i + 1, j, m, n, "D", grid, sb)
    }
}