package Graph.Top_6

fun isOutOfBounds2( board: Array<CharArray>, x: Int, y:Int): Boolean {
    return (x< 0|| y< 0 || x> board.size - 1|| y> board[0].size -1)
}