package Graph.dfs_with_return

import Graph.Islands.b
import Graph.Islands.directions
import Graph.Islands.e
import Graph.Islands.w


// Here we check the number of whites captured by black
/*
1. if w is found, then start a Graph.Edges_question.dfs
2. Continue the Graph.Edges_question.dfs if w is seen and don't stop until the

2. if w is found, but its neighbor has e, set result to 0 and return
3. Change
 */


// count the # of white stones surrounded
fun main() {
    var goBoard2 = arrayOf(
        charArrayOf(w, b, b, e, b, b, b),
        charArrayOf(b, b, e, b, w, w, b),
        charArrayOf(e, e, e, e, w, w, b),
        charArrayOf(b, b, b, b, w, w, e),
        charArrayOf(e, e, e, e, b, b, e)
    )
    println(countNumWhite2(goBoard2))
}


// Notice this is very simliar to dfs with jumping game 5
// Here we check the number of whites captured by black
fun countNumWhite2(grid: Array<CharArray>): Int {
    // and that's it
    var seen = Array(grid.size) { BooleanArray(grid[0].size) }
    var count = 0
    val nr = grid.size

    val nc = grid[0].size
    for (r in 0 until nr) {
        for (c in 0 until nc) {

            // When you see a white start counting
            if (grid[r][c] == 'w') {
//               if(Graph.Edges_question.dfs(grid, r, c)){
                totalCount += (countNumCaptured2(grid, r, c, seen))
            }

        }
    }
    return totalCount
}

// By using this we can tell if captured on all sides
fun countNumCaptured2(
    grid: Array<CharArray>, r: Int, c: Int, seen: Array<BooleanArray>,
): Int {
    // visited already
    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]) {
        return 0
    }
    // If see black continue
    if (grid[r][c] == 'b') {
        return 0
    }

    // See empty return false
    if (grid[r][c] == 'e') {
        return 0
    }
    // Encounter white stone here, inc count
    seen[r][c] = true

    var count = 1
    for (d in directions) {
        println(count)

        // Because it's in all 4 direcitons like said
        count += countNumCaptured2(grid, r + d[0], c + d[1], seen)
    }
    return count
}