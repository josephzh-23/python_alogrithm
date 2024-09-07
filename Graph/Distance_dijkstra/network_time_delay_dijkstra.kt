package Graph.dijkstra

import java.util.*
import kotlin.collections.HashMap
import kotlin.collections.HashSet

/*
https://leetcode.com/problems/network-delay-time/description/
The format below is very important as discussed

 'a': {['b', 3], ['c', 4], ['d', 7]},
    'b': {['c',1], ['f',5]},
    k: here is the starting point ehre
 */
fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {
    // Step1 : use a map first to add src: [weight, target]
    //Build the graph table

    //Build the graph table
    var graph: MutableMap<Int, MutableList<IntArray>> = HashMap()
    for (time in times) {
        val src = time[0]
        val tar = time[1]
        val weight = time[2]

        // If not contain, then init a new list
        if (!graph.containsKey(src)) {
            graph[src] = LinkedList()
        }

        graph[src]?.add(intArrayOf(tar, weight))
    }

    graph.forEach {
        println("${it.key}, ${it.value[0][0]}")
    }

    // The following sorted by the weight from
    // Saying sort each array by the weight as indicated as below
    // intArrayOf(tar, weight)
    val minHeap: Queue<IntArray> = PriorityQueue { a: IntArray, b: IntArray -> a[1] - b[1] }

    //Define a hashset to keep track of visited nodes

    //Define a hashset to keep track of visited nodes
    val visited: MutableSet<Int> = HashSet()

    var min = 0
    minHeap.add(intArrayOf(k, 0))
    // Step 2 use a queue and visited set
    while (!minHeap.isEmpty()) {

        // The one with the smallest distance
        // [3, 1]
        val node = minHeap.poll()
        val src = node[0];
        val srcDist = node[1]

        if (visited.contains(src)) continue
        min = srcDist
        visited.add(src)
        if (!graph.containsKey(src)) continue

        // THen iterate thru each list of the source
        // 1: [[1,2], [2, 3]
        graph[src]?.forEach {
            val target = it[0]
            val tarDistance = it[1]
            minHeap.add(intArrayOf(target, srcDist + tarDistance))
        }
    }
    print(min)
    return if (visited.size == n) min else -1
}

fun main() {
    val times1 = arrayOf(
        intArrayOf(2, 1, 1),
        intArrayOf(2, 3, 1),
        intArrayOf(3, 4, 1)
    );
    val times2 = arrayOf(
        intArrayOf(1, 2, 1)
    );
    val n = 4;
    val k = 2
    networkDelayTime(times2, 2, 1)

}