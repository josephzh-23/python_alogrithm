

// This checks if the white stone is captured or not in the code
// Check if the board is captured
// 1 : black stone      0: white stone  // this way we can check if surrounded or not

fun capture(board: Array<CharArray>): Boolean {
    val m = board.size
    val n = board[0].size
    for (i in 0 until m) {
        for (j in 0 until n) {
            // If we see a
            if (board[i][j] == '0') {
                if (!dfs(board, i, j)) {
                    return false
                }
            }
        }
    }
    return true
}


fun dfs(board: Array<CharArray>, i: Int, j: Int): Boolean {
    val m = board.size
    val n = board[0].size
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] == '1') {
        return true
    }

    // Surroudned
    if (board[i][j] == '-') {
        return false
    }
    board[i][j] = '1'
    return dfs(board, i - 1, j) && dfs(board, i + 1, j) && dfs(board, i, j - 1) && dfs(board, i, j + 1)
}











