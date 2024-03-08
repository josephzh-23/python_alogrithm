package Graph.dfs_with_return

import Graph.Islands.b
import Graph.Islands.e
import Graph.Islands.w


// Here we check the number of whites captured by black
/*
1. if w is found, then start a Graph.Edges_question.dfs
2. Continue the Graph.Edges_question.dfs if w is seen and don't stop until the

2. if w is found, but its neighbor has e, set result to 0 and return
3. Change
 */


//


// count the # of white stones surrounded
fun main() {
    var goBoard2 = arrayOf(charArrayOf(w, w, b, e, b, b, b),
            charArrayOf(b, b, e, b, w, w, b),
            charArrayOf(e, e, e, e, b, b, b),
            charArrayOf(e, e, e, e, e, e, e))
   println(countNumWhite(goBoard2))
}

var totalCount = 0
// Here we check the number of whites captured by black
fun countNumWhite(grid: Array<CharArray>): Int {
    // and that's it
    var seen = Array(grid.size) { BooleanArray(grid[0].size) }
    var count = 0
    val nr = grid.size

    val nc = grid[0].size
    for (r in 0 until nr) {
        for (c in 0 until nc) {
            if (grid[r][c] == 'w') {
//               if(Graph.Edges_question.dfs(grid, r, c)){
                (countNumCaptured(grid, r, c, seen))
                }

            }
        }
    return totalCount
}

// By using this we can tell if captured on all sides
fun countNumCaptured(grid: Array<CharArray>, r: Int, c: Int, seen: Array<BooleanArray>){
    // visited already
    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]) {
        return
    }
    // If see black continue
    if (grid[r][c] == 'b') {
        return
    }

    // See empty return false
    if (grid[r][c] == 'e') {
        totalCount = 0
        return
    }

    // Encounter white stone here, inc count
    seen[r][c] = true
    totalCount++
    countNumCaptured(grid, r + 1, c, seen)
    countNumCaptured(grid, r - 1, c, seen)
    countNumCaptured(grid, r, c + 1, seen)
    countNumCaptured(grid, r, c - 1, seen)
}