//import java.util.*
////https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
//fun main() {
//    var n = 4
//    var edges = arrayOf(
//        intArrayOf(0, 1, 3),
//        intArrayOf(1, 2, 1),
//        intArrayOf(1, 3, 4)
//    )
//
//    var s = FindCityWithSmallestNeighbors()
//    s.findTheCity(n, edges, 4)
//}
//
//internal class FindCityWithSmallestNeighbors2 {
//
//    // This graph will contain the following here
//    /*
//     0: [1, 2]      the node and all its neighbors here
//
//     */
//    private val graph: MutableMap<Int, MutableList<IntArray>> =
//        mutableMapOf()
//
//    // Keep track of distances at each node
//    // Example : from 0-> 1     the distance would be updated at the index 1
//    // consistently here only over here and that's it
//
//   // Use this to keep track here
//    private lateinit var dist: IntArray
//    private var seen: MutableSet<Int?>? = null
//    var ans = Int.MAX_VALUE
//    fun findTheCity(n: Int, edges: Array<IntArray>, distanceThreshold: Int): Int {
//        dist = IntArray(n)
//        seen = mutableSetOf()
//        var resIdx = -1
//        for (edge in edges) {
//            val u = edge[0]
//            val v = edge[1]
//            val weight = edge[2]
//            graph.computeIfAbsent(u) { ArrayList() }.add(intArrayOf(v, weight))
//
//            graph.computeIfAbsent(v) { mutableListOf() }.add(intArrayOf(u, weight))
//        }
//
//        // # of edges here in code
//        for (i in 0 until n) {
//            init()
//            dijkstra(i, distanceThreshold)
//            if (getCities(i, n, distanceThreshold) <= ans) {
//                ans = getCities(i, n, distanceThreshold)
//                resIdx = i
//            }
//        }
//        return resIdx
//    }
//
//    private fun dijkstra(source: Int, distanceThreshold: Int) {
//        dist[source] = 0
//        val pq = PriorityQueue(Comparator.comparingInt { a: IntArray -> a[1] })
//
//        // Each time we add the source and the distance here
//        pq.offer(intArrayOf(source, 0))
//
//
//        while (!pq.isEmpty()) {
//            val node = pq.poll()
//            val start = node[0]
//            val distance = node[1]
//
//
//            // These 2 are for skipping this code here
//            if (seen!!.contains(start)) continue
//            if (distance >= distanceThreshold) continue
//            seen!!.add(start)
//            if (graph.containsKey(start)) {
//                for (adj in graph[start]!!) {
//                    val nei = adj[0]
//                    val edgeWeight = adj[1]
//                    if (!seen!!.contains(nei) && dist[nei] > dist[start] + edgeWeight) {
//
//                        dist[nei] = dist[start] + edgeWeight
//                        pq.offer(intArrayOf(nei, dist[nei]))
//                    }
//                }
//            }
//        }
//    }
//
//    private fun init() {
//        Arrays.fill(dist, Int.MAX_VALUE)
//        seen!!.clear()
//    }
//
//    private fun getCities(idx: Int, n: Int, distanceThreshold: Int): Int {
//        var count = 0
//        for (i in 0 until n) {
//            if (i == idx) continue
//            if (dist[i] <= distanceThreshold) ++count
//        }
//        return count
//    }
//}