package Util

fun main() {
    var grid = arrayOf(intArrayOf(0,0,1,0),
            intArrayOf(0,0,0,0),
            intArrayOf(0,1,1,0))


    var seen =   Array(grid.size) { BooleanArray(grid[0].size) }

    // how to call this @ beginning here
    seen[0][0] = true
}