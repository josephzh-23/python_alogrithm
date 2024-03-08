package Graph.Island_problems

// Check out this solutino right here
// O (m *n )
// Treat this as if there is an edge between 2 horizontally adjacent nodes of
// value of 1
/*
Since when we see 1, when we visit it becomes 0, this is how we know it has
been visited
Every visited node set as 0, it's the same as visited set basically
 */
internal class Solution8 {
    fun dfs(grid: Array<CharArray>, r: Int, c: Int) {
        val nr = grid.size
        val nc = grid[0].size
        if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
            return
        }
        grid[r][c] = '0'
        dfs(grid, r - 1, c)
        dfs(grid, r + 1, c)
        dfs(grid, r, c - 1)
        dfs(grid, r, c + 1)
    }

    fun numIslands(grid: Array<CharArray>?): Int {
        if (grid == null || grid.size == 0) {
            return 0
        }
        val nr = grid.size
        val nc = grid[0].size
        var num_islands = 0
        for (r in 0 until nr) {
            for (c in 0 until nc) {
                if (grid[r][c] == '1') {
                    ++num_islands
                    dfs(grid, r, c)
                }
            }
        }
        return num_islands
    }
}