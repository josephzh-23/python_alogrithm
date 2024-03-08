//package Graph.bfs_with_counting
//
//import java.util.*
//
//// This is to find all the surrounded white stones here
//// given an entire board here
//
//var goBoard2 = arrayOf(charArrayOf(w, w, b, e, b, b, b),
//        charArrayOf(b, b, e, b,  w, w, b),
//        charArrayOf(e, e, e, e, b, e, b),
//        charArrayOf(e, e, e, e, e, e, e))
//
//fun Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    println(solveGodfs(goBoard2))
//}
//// use this in a Graph.Edges_question.dfs problem here
//// see if this works
//fun solveGodfs(board: Array<CharArray>):Int{
//
//    // and to work on this problem here
//    val m = board.size
//    val n = board[0].size
//    val visited = Array(m) { BooleanArray(n) }
//
//    val aList: ArrayList<IntArray> = ArrayList<IntArray>()
//
//
//
//    var totalCount = 0
//
//    var count = 0
//    // Add the coord for all white stones
//    for (i in 0 until board.size) {
//        for (j in 0 until board[i].size) {
//            if (board[i][j] == 'w') {
//                aList.add(intArrayOf(i, j))
//            }
//        }
//    }
//    // For each coordinate where there is list
//    for (coord in aList) {
//        val r = coord[0]
//        val c = coord[1]
//        count += bfsBoard(board, visited, r, c)
//    }
//    return count
//}
//
//fun bfsBoard(board: Array<CharArray>,visited: Array<BooleanArray>,  r: Int, c:Int):Int{
//
//    var count = 0
//    // valid is needed to check if you can capture sth
//    var surrounded = true
//    // Move in 4 directions
//    val directions = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
//    val q: Queue<IntArray> = LinkedList()
//
//    q.offer(intArrayOf(r, c))
//    while(!q.isEmpty()){
//        var node = q.poll()
//        var x= node[0]; var y = node[1]
//        if(isOutOfBounds(board, x, y) || visited[x][y] ||
//                board[x][y] == 'b')continue
//
//        // This means you have run into an empty stone
//        // spot so no count returned
//        if (board[x][y] == 'e') {
//            surrounded = false
//        } else {
//            // Here a white stone is encountered
//            visited[x][y] = true
//            // So within the bound here
//            directions.forEach { dir ->
//                q.offer(intArrayOf(x + dir[0], y + dir[1]))
//            }
//            count++
//        }
//    }
//
//    return if (surrounded) count else 0
//}
//
//fun isInBoundsChar(board: Array<CharArray>, x: Int, y:Int): Boolean {
//    if (x< 0|| y< 0 || x>= board.size|| y>= board[0].size){
//        return false
//    }else return true
//}
//
