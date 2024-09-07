//package Graph.dijkstra
//
//import java.util.*
//
//// var dist = |xi - xj| + |yi - yj|
//// |val| = absolute value there
//
//// Return the minimum cost to make all points connected. All points are connected
//// if there is exactly one simple path between any two points
//
//fun Graph.Edges_question.Sliding_window.maining_window.Sliding_window.Graph.Hard.main() {
//    var pts = arrayOf(intArrayOf(0, 0),
//    intArrayOf(2, 2,), intArrayOf(3, 10), intArrayOf(5, 2),
//    intArrayOf(7,0))
//    minCostConnections(pts).also { println(it) }
//}
//
////https://leetcode.com/problems/min-cost-to-connect-all-points/description/
//fun minCostConnections( points: Array<IntArray>): Int {
//
//    var visited = HashSet<Int>()
//    var cost = 0
//    // A min heap here  a[0] means the first idx the array here basically
//    // This will be a minheap based on teh distance here
//      val minHeap = PriorityQueue { a: IntArray, b: IntArray -> a[2] - b[2] }
//
//    // We will add to this the the format will be
//    // [beginning price, the start,   and then k + 1 stops]
//
//    var num = points.size
//    minHeap.offer(intArrayOf(0, 0, 0))
//    while (!minHeap.isEmpty() && visited.size < num) {
//        val cur = minHeap.poll()
//        // cur[0] would be the starting point here
//        val endId = cur[1]
//        val curCost = cur[2]
//        // This means the below has been visited
//        if (visited.contains(cur[1])) continue
//
//        cost += curCost
//        // So we know it has been added
//        visited.add(endId)
//        for(i in 0 until num){
//            if(!visited.contains(i)){
//                val startPtForNext = endId
//                minHeap.add(intArrayOf(endId, i, distance(points, startPtForNext, i)))
//            }
//        }
//    }
//    return cost
//}
//
//// using the end id you would get following here
//fun distance(points:Array<IntArray>, i: Int, j: Int):Int{
//    return Math.abs(points[i][0] - points[j][0]) +
//            Math.abs(points[i][1] - points[j][1])
//}
//
//
//
