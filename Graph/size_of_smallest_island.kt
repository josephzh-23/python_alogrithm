package Graph

import Graph.Islands.directions

//https://structy.net/problems/minimum-island
fun main() {
    // Size of the smallest here
    var grid = arrayOf(
        charArrayOf('w', 'l', 'w', 'w', 'w'),
        charArrayOf('w', 'l', 'w', 'w', 'w'),
        charArrayOf('w', 'w', 'w', 'l', 'w'),
        charArrayOf('w', 'w', 'l', 'l', 'w'),
        charArrayOf('l', 'w', 'w', 'l', 'l'),
        charArrayOf('l', 'l', 'w', 'w', 'w')
    )

    //Using this quesiton here then we have

    numIslands(grid)
}

fun dfs(grid: Array<CharArray>, r: Int, c: Int): Int {
    val nr = grid.size
    val nc = grid[0].size
    // see water then go back
    if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == 'w') {
        return 0
    }

    // We know this will be a land here since it made it this far
    grid[r][c] = 'w'
    var count = 1
    for (d in directions) {
        count += dfs(grid, r + d[0], c + d[1])
    }
    println(count)
    return count
}

fun numIslands(grid: Array<CharArray>?): Int {
    if (grid == null || grid.size == 0) {
        return 0
    }

    // Keep track of all the sums here
    var list = mutableListOf<Int>()
    val nr = grid.size
    val nc = grid[0].size
    var num_islands = 0
    for (r in 0 until nr) {
        for (c in 0 until nc) {
            // that's your starting point here
            if (grid[r][c] == 'l') {
                ++num_islands
                list.add(dfs(grid, r, c))
            }
        }
    }
    println(list)
    return list.min() ?: 0
//    return num_islands
}