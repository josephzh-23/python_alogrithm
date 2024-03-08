package Graph.dijkstra

import January_3rd.print
import java.util.*


fun main() {
    var n = 3
    var edges = arrayOf(intArrayOf(0, 1), intArrayOf(1, 2), intArrayOf(0, 2))

    var succProb = doubleArrayOf(0.5, 0.5, 0.2)
    maxProbability(n, edges, succProb, 0, 2).print()
}

fun maxProbability(n: Int, edges: Array<IntArray>, succProb: DoubleArray, start: Int, end: Int): Double {
    val prob = DoubleArray(n)


    val maxHeap = PriorityQueue<Int>()
    val adjList: MutableMap<Int, MutableList<IntArray>> = mutableMapOf()
    for (i in edges.indices) {

//        adjList
        // These 2 should be the opposite here
        adjList.computeIfAbsent(edges[i][0]) { mutableListOf() }
            .add(intArrayOf(edges[i][1], i))
        adjList.computeIfAbsent(edges[i][1]) {
            mutableListOf()
        }
            .add(intArrayOf(edges[i][0], i))
    }
    prob[start] = 1.0
    maxHeap.offer(start)
    while (!maxHeap.isEmpty()) {
        val cur = maxHeap.poll()
        adjList[cur]?.let {
            for (nei in it) {
                if (prob[cur] * succProb[nei[1]] > prob[nei[0]]) {
                    prob[nei[0]] = prob[cur] * succProb[nei[1]]
                    maxHeap.offer(nei[0])
                }
            }
        }
    }
    return prob[end]
}