//import January_3rd.print
//import java.util.*
//
//// We tweaked this so the ball would only traverse 1 step at a time
//fun Sliding_window.Basic.Sliding_window.Graph.Hard.main() {
//    var arr = arrayOf(intArrayOf(0, 0, 0, 0, 0), intArrayOf(1, 1, 0, 0, 1), intArrayOf(0, 0, 0, 0, 0), intArrayOf(0, 1, 0, 0, 1), intArrayOf(0, 1, 0, 0, 0))
//
//    var ball = intArrayOf(4, 3)
//    var hole = intArrayOf(0, 1)
//    findShortestWay2(arr, ball, hole).print()
//
//}
//
//
//fun findShortestWay2(maze: Array<IntArray>, ball: IntArray, hole: IntArray): String {
//
//
//    // Do we have to use this queue or can we just use the regular one
//
//
//    val pq: PriorityQueue<Point> = PriorityQueue { a: Point, b: Point ->
//
//        // this is used for lexicological order
//
//        /*
//
//        There are two shortest ways for the ball to drop into the hole.
//The first way is left -> up -> left, represented by "lul".
//The second way is up -> left, represented by 'ul'.
//
//        Both ways have shortest distance 6, but the first way
//        is lexicographically smaller because 'l' < 'u'. So the output is "lul".
//         */
//        if (a.distance == b.distance)
////
////            // What if we don't use the following here
//            a.movement.compareTo(b.movement) else a.distance - b.distance
//    }
//
//    // Using just the queue step but not the
//
//    // Use this for the move ment
//    val visited = Array(maze.size) { BooleanArray(maze[0].size) }
//    val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
//    val move = charArrayOf('d', 'u', 'r', 'l')
//
//    pq.offer(Point(ball[0], ball[1], 0, ""))
//    while (!pq.isEmpty()) {
//        val point: Point = pq.poll()
//        if (point.row == hole[0] && point.col == hole[1]) return point.movement
//        visited[point.row][point.col] = true
//
//        for (i in 0..3) {
//            val dir = dirs[i]
//            var row: Int = point.row
//            var col: Int = point.col
//            var distance: Int = point.distance
//
//            var dx = row + dir[0]
//            var dy = col + dir[1]
//            if (isValid2(maze, dx, dy)) {
//                distance++
//                if (!visited[dx][dy]) {
//                    println(point.movement)
//
//                    pq.offer(Point(dx, dy, distance, point.movement + move[i]))
//                }
//                if (row == hole[0] && col == hole[1]) break
//            }
//        }
//    }
//    return "impossible"
//}
//
//fun isValid2(maze: Array<IntArray>, row: Int, col: Int): Boolean {
//    return if (row < 0 || row >= maze.size || col < 0 || col >= maze[0].size || maze[row][col] == 1) false else true
//}
