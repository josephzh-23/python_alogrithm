package Graph.traversal_with_steps


import java.util.*

//flights where flights[i] = [fromi, toi, pricei]

// we just change the conditions very slightly here
// Uses dijkstra's algorithm
// Time Limit Exceeded
// https://leetcode.com/problems/cheapest-flights-within-k-stops/
fun findCheapestPriceNoStops(n: Int, flights: Array<IntArray>, src: Int, dst: Int, K: Int): Int {
    val g = Array(n) { IntArray(n) }
    for (f in flights) {
        g[f[0]][f[1]] = f[2]
    }
    // A min heap here  a[0] means the first idx the array here basically
    val minHeap = PriorityQueue { a: IntArray, b: IntArray -> a[0] - b[0] }

    // We will add to this the beginning price,
    // the start,   and then k + 1 stops
    // This will still be based on the price here
    minHeap.offer(intArrayOf(0, src))
    while (!minHeap.isEmpty()) {
        val cur = minHeap.poll()
        val price = cur[0]
        val place = cur[1]
//        val remainStops = cur[2]
        if (place == dst) return price
//        if (remainStops > 0) {
            for (end in 0 until n) {
                if (g[place][end] > 0) {
                    minHeap.offer(intArrayOf(price + g[place][end], end))
                }
//            }
        }
    }
    return -1
}

fun main() {
    var flights = arrayOf(intArrayOf(0, 1, 100),
    intArrayOf(1, 2, 100), intArrayOf(2, 0, 100), intArrayOf(1, 3, 600),
    intArrayOf(2, 3, 200))
    var n = 4
    // this should give 300 since no stop
    println(findCheapestPriceNoStops(4, flights,0, 2, 0))
    // the number of testers here
}



