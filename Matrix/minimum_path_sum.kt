package Matrix

// Bottom to top dynamic programming questino here
// Another one of these
fun minPathSum(grid: Array<IntArray>): Int {
    for (i in grid.indices.reversed()) {
        for (j in grid[0].indices.reversed()) {

            // We start with the last row first for each column
            if (i == grid.size - 1 && j != grid[0].size - 1) grid[i][j] = grid[i][j] + grid[i][j + 1]

            // start with the last column first for each row
            else if (j == grid[0].size - 1 && i != grid.size - 1) grid[i][j] = grid[i][j] + grid[i + 1][j]

            // The below is the actual diagram that we have found
            else if (j != grid[0].size - 1 && i != grid.size - 1)
                grid[i][j] =
                grid[i][j] + Math.min(grid[i + 1][j], grid[i][j + 1])
        }
    }
    return grid[0][0]
}