package Graph.Basics

import Graph.Islands.directions
import Graph.dfsmmatrix


fun main() {

    dfsmmatrix()
}

// O(v + e) complexity here
fun dfsMatrix() {
    // and that's it
    var grid = arrayOf(intArrayOf(0, 0, 1, 0),
            intArrayOf(0, 0, 0, 0),
            intArrayOf(0, 1, 1, 0))
    var seen = Array(grid.size) { BooleanArray(grid[0].size) }

    val nr = grid.size
    val nc = grid[0].size
    for (r in 0 until nr) {
        for (c in 0 until nc) {
            dfs(grid, r, c, seen)
        }
    }
}

fun dfs(grid: Array<IntArray>, r: Int, c: Int, seen: Array<BooleanArray>) {

    // visited already
    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]) {
        return
    }


    seen[r][c] = true
    println(grid[r][c])

    for (d in directions) {
        dfs(grid, r + d[0], c + d[1], seen)
    }

}