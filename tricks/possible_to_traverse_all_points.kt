package tricks



fun main() {
    // This will let you know when it's done
    var arr = arrayOf(intArrayOf(1, 1, 1, 1),
            intArrayOf(0, 0, 0,1), intArrayOf(0, 0, 1, 1))
    uniquePathsIII(arr)
}
// 1 is accessible, 0: blocked here
fun uniquePathsIII(grid: Array<IntArray>): Int {
    var ones = 0 // Count all the ones

    // The hypothetical starting point here
    var sx = 0 // starting x index
    var sy = 0 // starting y index
    for (r in grid.indices) { // r = row
        for (c in grid[0].indices) { // c = column
            if (grid[r][c] == 1) ones++ // if current cell is 0, count it.

//            else if (grid[r][c] == 1) {
//                sx = r // starting x co-ordinate
//                sy = c // starting y co-ordinate
//            }
        }
    }
    return dfs(grid, sx, sy, ones)
}


// mark this as -1 to avoid overflow
// ending condition: everything is cleaned here and that's it
fun dfs(grid: Array<IntArray>, x: Int, y: Int, ones: Int): Int {
    // Base Condition, this will keep getting smaller over here
    var ones = ones
    if (x < 0 || y < 0 || x >= grid.size || y >= grid[0].size || grid[x][y]==-1
            ||grid[x][y]== 0) {
        return 0
    }
    println(ones)
    // We have found the path looking for here
    if(ones== 1) {

        return 1
    }
        // If that's the case we find the path and return '1' otherwise return '0';
    grid[x][y] = -1 // mark the visited cells as -1;
    ones-- // and reduce the zero by 1
    val totalAns = dfs(grid, x + 1, y, ones) + dfs(grid, x - 1, y, ones) + dfs(grid, x, y + 1, ones) + dfs(grid, x, y - 1, ones)

    // Let's say if we are not able to count all the paths. Now we use Backtracking over here
    grid[x][y] = 1
    ones++
    return totalAns // if we get all the paths, simply return it.
}