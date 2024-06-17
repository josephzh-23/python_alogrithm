package Backtracking

/*
1   start       2  ending square
0 empty ones we can walk over
https://leetcode.com/problems/unique-paths-iii/
kind of different from counting number of islands here
1. Try to go in all 4 directions, if obstacle then return
if already visited, then return
2. If cell is 2, but all cells are not covered return and backtrack
    if cell is 2, and all empty cell is covered then found 1
        path++
 */
fun uniquePathsIII(grid: Array<IntArray>): Int {
    var zero = 0 // Count the 0's
    var sx = 0 // starting x index
    var sy = 0 // starting y index
    for (r in grid.indices) { // r = row
        for (c in grid[0].indices) { // c = column
            if (grid[r][c] == 0) zero++ // if current cell is 0, count it.
            else if (grid[r][c] == 1) {
                sx = r // starting x co-ordinate
                sy = c // starting y co-ordinate
            }
        }
    }
    return dfs(grid, sx, sy, zero)
}

fun dfs(grid: Array<IntArray>, x: Int, y: Int, zero: Int): Int {
    // Base Condition
    var zero = zero

    println("num of zeros $zero")
    if (x < 0 || y < 0 || x >= grid.size || y >= grid[0].size || grid[x][y] == -1) {
        return 0
    }
    if (grid[x][y] == 2) {
        return if (zero == -1) 1 else 0 // Why zero = -1, because in above example we have 9 zero's. So, when we reach the final cell we are covering one cell extra then the zero count.
        // If that's the case we find the path and return '1' otherwise return '0';
    }
    grid[x][y] = -1 // mark the visited cells as -1;
    zero-- // and reduce the zero by 1
    val totalPaths = dfs(grid, x + 1, y, zero) +  // calculating all the paths available in 4 directions
            dfs(grid, x - 1, y, zero) +
            dfs(grid, x, y + 1, zero) +
            dfs(grid, x, y - 1, zero)

    // Let's say if we are not able to cover all the zeros in 1 path
    // that means we have failed so we need to backtrack and add zero count
    grid[x][y] = 0
    zero++
    println("# of path is $totalPaths")
    return totalPaths // if we get all the paths, simply return it.
}

fun main() {
    var arr = arrayOf(intArrayOf(1, 0, 0, 0),
            intArrayOf(0, 0, 0,0), intArrayOf(0, 0, 2, -1))
   println(uniquePathsIII(arr))
}