//package Graph.dfs_with_return
//
//
//import Graph.bfs_with_counting.directions
//
//
//
//// How to count variables in a grid
//fun Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//
//    dfsMatrix()
//}
//
//// This gives you the totla numebr of 1s here
//fun dfsMatrix() {
//    // and that's it
//    var grid = arrayOf(intArrayOf(0, 0, 1, 0),
//            intArrayOf(0, 0, 0, 0),
//            intArrayOf(0, 1, 1, 0))
//    var seen = Array(grid.size) { BooleanArray(grid[0].size) }
//    var tot = 0
//    val nr = grid.size
//    val nc = grid[0].size
//    for (r in 0 until nr) {
//        for (c in 0 until nc) {
//            tot +=Graph.Edges_question.dfs(grid, r, c, seen, 0)
//        }
//    }
//    println(tot)
//}
//
//// This will find all the sum as stated
//fun Graph.Edges_question.dfs(grid: Array<IntArray>, r: Int, c: Int, seen: Array<BooleanArray>,
//count:Int) :Int{
//    var count = count
//    // visited already
//    if (r < 0 || c < 0 || r >= grid.size || c >= grid[0].size || seen[r][c]
//            || grid[r][c] == 0) {
//
//    // And then using the code here we would get what we want in no time
//        // as said
//        return 0
//    }
//
//    seen[r][c] = true
//    if(grid[r][c] == 1){
//        return 1
//    }
//    println(count)
//
//    for (d in directions) {
//        count +=Graph.Edges_question.dfs(grid, r + d[0], c + d[1], seen, count)
//    }
//    return count
//}