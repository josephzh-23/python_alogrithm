//import java.util.*
//
//
//internal class Tree.Count.Solution {
//    fun minKnightMoves(x: Int, y: Int): Int {
//        // the offsets in the eight directions
//        val offsets = arrayOf(intArrayOf(1, 2), intArrayOf(2, 1), intArrayOf(2, -1), intArrayOf(1, -2), intArrayOf(-1, -2), intArrayOf(-2, -1), intArrayOf(-2, 1), intArrayOf(-1, 2))
//
//        // - Rather than using the inefficient HashSet, we use the bitmap
//        //     otherwise we would run out of time for the test cases.
//        // - We create a bitmap that is sufficient to cover all the possible
//        //     inputs, according to the description of the problem.
//
//        /*
//        Why 607?    abs(x) + abs(y) = 300
//        min : -300 and max 300
//         */
//        val visited = Array(607) { BooleanArray(607) }
//        val queue: Deque<IntArray> = LinkedList()
//        queue.addLast(intArrayOf(0, 0))
//        var steps = 0
//        while (queue.size > 0) {
//            val currLevelSize = queue.size
//            // iterate through the current level
//            for (i in 0 until currLevelSize) {
//                val curr = queue.removeFirst()
//                if (curr[0] == x && curr[1] == y) {
//                    return steps
//                }
//                for (offset in offsets) {
//                    val next = intArrayOf(curr[0] + offset[0], curr[1] + offset[1])
//                    // align the coordinate to the bitmap
//                    if (!visited[next[0] + 302][next[1] + 302]) {
//                        visited[next[0] + 302][next[1] + 302] = true
//                        queue.addLast(next)
//                    }
//                }
//            }
//            steps++
//        }
//        // move on to the next level
//        return steps
//    }
//}