//package Graph.bfs_with_counting
//
//import Graph.Basics.isInBoundsInt
//import java.util.*
//
//
//// Lets you know how many islands surrounded by 0s here
//fun checkSurroundedRegion(grid: Array<IntArray>): Int {
//
//// given a start point here
////    var start = intArrayOf(1,1)
//// 1 and 1 are the starting point for this
//    var visited = Array(grid.size) { BooleanArray(grid[0].size) }
//
//    // Check # of perimeters
//    var count = 0
//    var start = intArrayOf(0, 0)
//    var q: Queue<IntArray> = LinkedList()
//    q.add(start)
//
//
//
//    visited[start[0]][start[1]] = true
//
//
//    while (!q.isEmpty()) {
//        var node = q.poll()
//        var x = node[0];
//        var y = node[1]
//        // YOu need to print the node at that point
//
//        // using this can let you know how many we have that's surrounded
//        //by 0
//
//        // Tell you how many we have here
//
//
//        directions.forEach { dir ->
//
//
//            var dx = x + dir[0]
//            var dy = y + dir[1]
//            if (isInBoundsInt(grid, dx, dy)) {
//                if(grid[dx][dy] == 1)
//                if (!visited[dx][dy]) {
//                    println("removed node is ${grid[dx][dy]} ")
//                    visited[dx][dy] = true
//                    q.offer(intArrayOf(dx, dy))
//                }
//            }
//        }
//    }
//}