package Hard

import java.util.*


// N-th queen probability
internal class Solution13 {
    var res: MutableList<List<String>> = LinkedList()
    fun solveNQueens(n: Int): List<List<String>> {
        val board = Array(n) { CharArray(n) }
        for (cs in board) {
            Arrays.fill(cs, '.')
        }
        helper(board, 0, 0, n)
        return res
    }

    private fun helper(board: Array<CharArray>, row: Int, col: Int, n: Int) {
        var row = row
        var col = col
        var n = n

        // Column out of bound
        // Then go to the next row
        if (col == board[0].size) {
            col = 0
            row++
        }

        // When you traverse to end need to have 4 queens

        // n is 0 then add to the res
        if (n == 0) {
            res.add(toString(board))
            return
        }
        // You ahve reached the last row here
        if (row == board.size) return

        // Place queen here if valid
        if (isValid(board, row, col)) {
            board[row][col] = 'Q'
            n--
            helper(board, row, col + 1, n)
            // backtrack unchoose the option
            board[row][col] = '.'
            n++
        }

        // This means not valid
        // If we decide to Skip this cell, we place a '.', put it
        // as empty here
        helper(board, row, col + 1, n)
    }

    private fun toString(board: Array<CharArray>): List<String> {
        val list: MutableList<String> = LinkedList()
        var str: StringBuilder
        for (cs in board) {
            str = StringBuilder()
            for (cur in cs) {
                str.append(cur)
            }
            list.add(str.toString())
        }
        return list
    }

    // this makes
    private fun isValid(board: Array<CharArray>, row: Int, col: Int): Boolean {

        val N = board.size

        // TOP AND DOWN
        // because queen move in vertical directions
        // Here iterating top and down see if anything not
        // emtpy
        for (i in 0 until N) {
            if (board[i][col] != '.') return false
            if (board[row][i] != '.') return false
        }

        // Top left + top right + down left + down right
        var i = row
        var j = col

        // this is when you go in the diagonal
        // in the upper left diagnoal direction
        while (0 <= i && 0 <= j) {
            // if there is a queen there then no good
            if (board[i][j] != '.') return false
            i--
            j--
        }
        // Top right
        i = row
        j = col
        while (0 <= i && j < N) {
            if (board[i][j] != '.') return false
            i--
            j++
        }
        // Down Right
        i = row
        j = col
        while (i < N && j < N) {
            if (board[i][j] != '.') return false
            i++
            j++
        }

        // Down left position in leetcode
        i = row
        j = col
        while (i < N && 0 <= j) {
            if (board[i][j] != '.') return false
            i++
            j--
        }
        return true
    }
}