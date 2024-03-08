package Backtracking

import java.util.HashMap
// This doesn't acutllay use backtracking just a way
// but just a way of solving problem
fun main() {
    var arr = arrayOf(charArrayOf('1', '2', '3'),
            charArrayOf('4', '5', '.'),
            charArrayOf('7', '8', '8'))

    println(validSquare(arr))
}

// Check if a square is valid
// This is prequel to valid sudoku problems
// Using neetcode.io solution
fun validSquare(b: Array<CharArray>): Boolean {
    var rows: MutableMap<Int, MutableList<Char>> = HashMap<Int, MutableList<Char>>()
    var cols: MutableMap<Int, MutableList<Char>> = HashMap<Int, MutableList<Char>>()

    // Each row and column unique and nothing in between
    for (i in 0 until 3) {
        for (j in 0 until 3) {
            // Check if value seen in column or rows before?
            if (b[i][j] == '.') continue
            else {
                // [0]

                // If don't contains
                if (rows[i]?.contains(b[i][j]) == true ||
                        (cols[j]?.contains(b[i][j]) == true)) {
                    return false
                }

                // If not contains then need to add it
                // These 2 are absolutely necessary
                rows.putIfAbsent(i, ArrayList())
                cols.putIfAbsent(j, ArrayList())
                rows[i]!!.add(b[i][j])
                cols[j]!!.add(b[i][j])

            }
        }
    }
    return true // if gotten to here then must be true here
}

