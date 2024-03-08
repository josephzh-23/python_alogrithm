package Backtracking

import Graph.Islands.directions

var exists = false

//https://leetcode.com/problems/word-search/description/
fun wordSearch(board: Array<CharArray>, word: String): Boolean {


    // get count first and then
    var arr = ArrayList<Char>()
    // another way to store
    for (c in word.toCharArray()) {
        arr.add(c)
    }
    // do a Graph.Edges_question.dfs on this

    var seen = Array(board.size) { BooleanArray(board[0].size) }

    val nr = board.size
    val nc = board[0].size
    for (r in 0 until nr) {
        for (c in 0 until nc) {
            dfs(board, r, c, seen, arr)
        }
    }

    return exists
    // once count then need the code next
}

fun dfs(grid: Array<CharArray>, r: Int, c: Int, seen: Array<BooleanArray>, charArr: ArrayList<Char>) {
    // visited already
    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]) {
        return
    }
    if (charArr.contains(grid[r][c])) {
        charArr.remove(grid[r][c])
    }
    if (charArr.isEmpty()) {
        exists = true
    }

    // else mark as visited
    seen[r][c] = true

    for (d in directions) {
        dfs(grid, r + d[0], c + d[1], seen,
                charArr)
    }
}

fun main() {
    var board = arrayOf(charArrayOf('a', 'b', 'c', 'e'),
            charArrayOf('s', 'f', 'c', 's'),
            charArrayOf('a', 'd', 'e', 'e'))
    var word = "abcced"

    wordSearch(board, word)
    println(exists)
}

/**/

