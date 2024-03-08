package Graph.Island_problems



fun main() {
    var sol = Solution17()

    var s = arrayOf(intArrayOf(1,1, 0,1, 1),
    intArrayOf(1, 0, 0,0,0),
    intArrayOf(0, 0,0, 0,1), intArrayOf(1,1,0,1,1))
    print(sol.numIslands(s))
//    s.
//    s.numIslands()
}
internal class Solution17 {

    var set: MutableSet<String> = HashSet()

    // Now for each of these
    // And now this
    var baseRow = 0;
    var baseCol = 0
    fun numIslands(grid: Array<IntArray>?): Int {
        if (grid == null || grid.size == 0) {
            return 0
        }
        val nr = grid.size
        val nc = grid[0].size
        for (r in 0 until nr) {
            for (c in 0 until nc) {
                // that's your starting point here
                if (grid[r][c] == 1) {


                    // pass in a base case, always the
                    // starting grid
                    baseRow = r
                    baseCol = c
                    // Start sth new each time here
                    var sb = StringBuilder()

                    // Pass in a base case
                    dfs(grid, r, c, sb)

                    // This make sure unique
                    set.add(sb.toString())
                }
            }
        }
        return set.size
    }

    fun dfs(grid: Array<IntArray>, r: Int, c: Int, sb: StringBuilder) {
        val nr = grid.size
        val nc = grid[0].size
        if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == 0) {
            return
        }
        // If this is the first time looking at it then put this here
        grid[r][c] = 0
        // Add coords to the string
        // [1011
        sb.append(r - baseRow)
        sb.append(c - baseCol)
        dfs(grid, r - 1, c, sb)
        dfs(grid, r + 1, c, sb)
        dfs(grid, r, c - 1, sb)
        dfs(grid, r, c + 1, sb)
//        set.add(sb.toString())
    }
}