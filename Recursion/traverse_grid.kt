package Recursion

// Use recursion to build a grid usign the 2d library
//
fun traverse2DGrid(grid: Array<IntArray>, row: Int, col: Int) {
    // this is if at the last col of each row
    var row = row
    var col = col
    if (col == grid[0].size) {
        col = 0
        row++
    }
    // case: row out of bound here
    if (row == grid.size) {
        return
    }
    println("grid is ${grid[row][col]}")
    traverse2DGrid(grid, row, col + 1)
}

fun main() {
    var arr = arrayOf(intArrayOf(1, 0, 0), intArrayOf(1, 0, 0),
            intArrayOf(1, 0, 0))
    traverse2DGrid(arr, 0, 0)
}