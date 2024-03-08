package Graph.Island_problems

/*

DFS
If node =1 trigger the Graph.Edges_question.dfs search
set all node as 0 to mark visited, then counter the
# of 1s
 */

internal class Solution14 {
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
                // that's your starting point here
                if (grid[r][c] == '1') {
                    ++num_islands
                    dfs(grid, r, c)
                }
            }
        }
        return num_islands
    }
}