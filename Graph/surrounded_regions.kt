package Graph

// What to do in this case

// Surrounded region
//Graph.Edges_question.dfs ->


/*
Eric programming
The steps
1. Start with teh boundary first
When you see an o, start a Graph.Edges_question.dfs in all directions

2. We can traverse all the borders first, and find the os
and turn it into #s as said
We want to find all elem = o that's connected to border 'o'
turn into #
3. When you see an x you can terminate the search as said

4. At the end, do a linear search thru all, turn 'o' into x
and turn 1 back to o like said.

Conditions
1. If sth not on the boundary no good, it will be surrounded by x
2. SO if a bunch of 'o's connected to a boundary o, can't be
surrounded by x

3. Apply a Graph.Edges_question.dfs and then check if anything to boundary, start from the
boudnary 'o's and convert if can or not
 */

internal class Solution {

    // Used to turn o into this x variable as saiud
    val temp = '#'
    val X = 'X'
    val O = 'O'
    var m = 0
    var n = 0
    lateinit var board: Array<CharArray>
    fun solve(board: Array<CharArray>) {
        this.board = board
        m = board.size
        n = board[0].size


        // iterate the columns border to find O
        for (row in 0 until m) {

            // The 1st and last row of the column border
            dfs(row, 0)
            dfs(row, n - 1)
        }
        // iterate the rows border to find O
        for (col in 0 until n) {

            // The first and last column of the row border here
            dfs(0, col)
            dfs(m - 1, col)
        }
        // traverse the grid to convert O to X
        for (row in 0 until m) {
            for (col in 0 until n) {

                // If we see any # then turn that back to O
                if (board[row][col] == temp) {
                    board[row][col] = O

                    // See any O change to X since it's not
                    // the ones connected to the boarder as we know
                } else if (board[row][col] == O) {
                    board[row][col] = X
                }
            }
        }
    }

    private fun dfs(row: Int, col: Int) {
        if (row < 0 || row == m || col == n || col < 0) return
        if (board[row][col] != O) return

        // For turning into # if we see O, otherwise
        // simply just return right
        board[row][col] = temp
        //Graph.Edges_question.dfs all directions
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    }
}


// The Sliding_window.practice section here
fun main(){

    var goBoard2 = arrayOf(charArrayOf('x','x', 'x', 'x'),
            charArrayOf('x', 'o', 'o', 'x'),
            charArrayOf('x', 'x', 'o', 'x'),
            charArrayOf('x', 'o', 'x', 'x'))
    surroundedRegion(goBoard2)
}
fun surroundedRegion(board: Array<CharArray>){
    //
    // 0 should not be flipped here
    // - It is on the border, or
    //- It is adjacent to an 'O' that should not be flipped.
    //The bottom 'O' is on the border, so it is not flipped.
    //The other three 'O' form a surrounded region, so they are flipped.

    // Graph.Edges_question.dfs

    // Using the solve and go problem
    // and that's it
    var seen = Array(board.size) { BooleanArray(board[0].size) }
    var count = 0
    val nr = board.size

    val nc = board[0].size
    for (r in 0 until nr) {
        for (c in 0 until nc) {
            if (board[r][c] == 'o') {
//               if(Graph.Edges_question.dfs(board, r, c)){
                (flip(board, r, c, seen))
            }

        }
    }
    board
}


fun flip(grid: Array<CharArray>, r: Int, c: Int, seen: Array<BooleanArray>) {
    // visited already, if on the boundary then return already
    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]
            || r == 0 || r == grid.size - 1 || c == 0 || c == grid[0].size - 1) {
        return
    }

    // See empty return false
    if (grid[r][c] == 'x') {
        return
    }

    // Encounter white stone here, inc count
    seen[r][c] = true
    // If see o
    grid[r][c] = 'x'

    flip(grid, r + 1, c, seen)
    flip(grid, r - 1, c, seen)
    flip(grid, r, c + 1, seen)
    flip(grid, r, c - 1, seen)
}
