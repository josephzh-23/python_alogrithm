package Graph
import Graph.Islands.directions
import java.lang.Integer.max


fun main() {

    dfsmmatrix()
}


fun dfsmmatrix() {
    // and that's it
    var grid = arrayOf(intArrayOf(0, 0, 1, 0),
            intArrayOf(0, 0, 0, 0),
            intArrayOf(0, 1, 3, 0))
    var seen = Array(grid.size) { BooleanArray(grid[0].size) }
    var maxi = 0
    val nr = grid.size
    val nc = grid[0].size
    for (r in 0 until nr) {
        for (c in 0 until nc) {
           maxi = max(maxi, dfs(grid, r, c, seen, 0))
        }
    }
    println(maxi)
}

fun dfs(grid: Array<IntArray>, r: Int, c: Int, seen: Array<BooleanArray>,
        maxi:Int):Int {

    var max = maxi
    // visited already
    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]) {
        return 0
    }


    // When it reaches the end then do sth here


    if(max < grid[r][c]){
        max = grid[r][c]
    }
    seen[r][c] = true
//    println(grid[r][c])

    for (d in directions) {
       max = max(max, dfs(grid, r + d[0], c + d[1], seen, max))
    }

    println(max)
    return max
    // It would automatically come here

}