package Graph

import Graph.Islands.directions
import January_3rd.print


// Distinct islands things
fun main() {
    // So here we will then have the code
    // So we can have a set, and then when we are done here
    var s2 = Sol()


    var s = arrayOf(intArrayOf(1,1, 0,1, 1),
        intArrayOf(1, 0, 0,0,0),
        intArrayOf(0, 0,0, 0,1), intArrayOf(1,1,0,1,1))
    s2.numIslands(s).print()
}


var list = mutableSetOf<Int>()

class Sol() {

    var set = mutableSetOf<String>()

    var baser = 0
    var basec = 0


    fun numIslands(grid: Array<IntArray>): Int {

        var seen = Array(grid.size) { BooleanArray(grid[0].size) }

        // WHen you see a 1 then start
        for (i in 0 until grid.size) {
            for (j in 0 until grid[0].size) {
                if (grid[i][j] == 1) {
                    baser = i
                    basec = j
                    var sb = StringBuilder()
                    dfs2(grid, baser, basec, seen, sb)

                    set.add(sb.toString())
                }
            }
        }
        return set.size
    }

    fun dfs2(
        grid: Array<IntArray>, r: Int, c: Int, seen: Array<BooleanArray>, sb: StringBuilder
    ) {

        // visited already
        if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c] || grid[r][c] == 0) {
            return
        }

        // Don't hcange the r and the c here so we are good here
        seen[r][c] = true
        println(grid[r][c])

        for (d in directions) {
            dfs2(grid, r + d[0], c + d[1], seen, sb.append(d))
        }

    }
}