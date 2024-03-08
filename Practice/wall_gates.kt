//package Practice
//
//import Graph.bfs_with_counting.directions
//import Graph.Basics.isInBoundsInt3
//import java.util.*
//
//// Fill empty room with distance to its nearest grid cell
//// Fill the empty room here
//
//fun wallsAndGates(rooms: Array<IntArray>): Unit {
//
//// given a start point here
////    var start = intArrayOf(1,1)
//    // 1 and 1 are the starting point for this
//    var visited =Array(rooms.size){BooleanArray(rooms[0].size)}
//
//    var start = intArrayOf(0, 0)
//    var q: Queue<IntArray> = LinkedList()
//    q.add(start)
//
//    // We know the starting pt right here
//
//
//    visited[start[0]][start[1]] = true
//    while(!q.isEmpty()){
//        var node = q.poll()
//        var x= node[0]; var y = node[1]
//        // YOu need to print the node at that point
//
//
//        directions.forEach { dir ->
//            var dx = x + dir[0]
//            var dy = y + dir[1]
//            if (isInBoundsInt3(rooms, dx, dy) ) {
//                if(!visited[dx][dy]) {
//                    println("removed node is ${rooms[dx][dy]} ")
//                    visited[dx][dy] = true
//
//                    q.offer(intArrayOf(dx, dy))
//                }
//            }
//        }
//    }
//}