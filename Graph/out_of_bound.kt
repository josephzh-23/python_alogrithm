//package Graph
//
//
///*
//1. things to watch out fo the array out of bound index error here
//2.
// */
//
///*
//The graph here is
//1  1  1   1
//1  1  1   1
//1  0  0   1
//1  1  1   1
// */
//var w = 'w'
//var b = 'b'
//var e = 'e'
//var grid2 = arrayOf(charArrayOf(w, w, w, w),
//        charArrayOf(w, w, w, w),
//        charArrayOf(b, w, w, w),
//        charArrayOf(w, w, w, w))
//fun checkOutOfBound(){
//
//    // and to work on this problem here
//    val x= 0
//    val y = 0
//
//    val curColor = grid[x][y]
//    val row = grid.size
//    val col = grid[0].size
//
//    val directions = arrayOf(intArrayOf(1, 0), intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1))
//    for(dir in directions){
//        val newRow = x + dir[0]
//        val newCol = y + dir[1]
//
//        // then we can find the path between nodes here
//        // There is the arrayout of bound index exception here
//        if (newRow < 0 ||newCol < 0) {
//            println("new row and col is $newRow and $newCol")
//            println("out of bound ")
//        }else{
//            println(" within bound")
//        }
//    }
//}
//
//fun Backtracking.Tree.Hard.Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//
//    checkOutOfBound()
//}