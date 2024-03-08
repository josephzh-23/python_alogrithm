import java.util.HashMap

// Can also check out the mini problem here


fun isValidSudoku(board: Array<CharArray>): Boolean {

    var rows: MutableMap<Int, MutableList<Char>> = HashMap<Int, MutableList<Char>>()
    var cols: MutableMap<Int, MutableList<Char>> = HashMap()

    /*
     will have the key key = (r/3 , c/3), using the code here then can figure out
     here we will have to round down since r is = 1
     */
    var squares :MutableMap<Pair<Int, Int>, MutableList<Char>> =
            HashMap<Pair<Int, Int>, MutableList<Char>>()
    // Each row and column unique and nothing in between
    for (i in 0 until 9) {
        for (j in 0 until 9) {
            // Check if value seen in column or rows before?
            if (board[i][j] == '.') continue
            else {
                // [0]
                // If don't contains
                if (rows[i]?.contains(board[i][j]) == true ||
                        (cols[j]?.contains(board[i][j]) == true)
                        ||squares[Pair(i, j)]?.contains(board[i][j]) == true) {
                    return false
                }

                // If not contains then need to add it
                // These 2 are absolutely necessary
                rows.putIfAbsent(i, ArrayList())
                cols.putIfAbsent(j, ArrayList())
                rows[i]!!.add(board[i][j])
                cols[j]!!.add(board[i][j])
                var row = i/3
                var col = j/3
                squares.putIfAbsent(Pair(row, col), ArrayList())
                squares[Pair(row, col)]!!.add(board[i][j])
            }
        }
    }
    return true // if gotten to here then must be true here

    // the valid sudoku problem here
}


fun main() {
    var arr = arrayOf(charArrayOf('8', '3', '.', '.', '7', '.', '.', '.','.'),
            charArrayOf('6', '.', '.', '1', '9', '5', '.', '.','.'),
            charArrayOf('.', '9', '8', '.', '.', '.', '.', '6','.'),
            charArrayOf('8', '.', '.', '.', '6', '.', '.', '.','3'),
            charArrayOf('4', '.', '.', '8', '.', '3', '.', '.','1'),
            charArrayOf('7', '.', '.', '.', '2', '.', '.', '.','6'),
            charArrayOf('.', '6', '.', '.', '.', '.', '2', '8','.'),
            charArrayOf('.', '.', '.', '4', '1', '9', '.', '.','5'),
            charArrayOf(',', '.', '.', '.', '8', '.', '.', '7','9'),
    )
    println(isValidSudoku(arr))
}





