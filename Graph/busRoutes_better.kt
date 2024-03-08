package Graph

import java.awt.Point
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.HashSet
import kotlin.collections.MutableList
import kotlin.collections.MutableSet

fun main() {
    var routes = arrayOf(intArrayOf(1, 2, 7),
            intArrayOf(3, 6, 7))
    var (src, tar) = intArrayOf(1, 6)
    numBusesToDestinationBetter(routes, src, tar)
}

fun numBusesToDestinationBetter(routes: Array<IntArray>, source: Int, target: Int): Int {
    if (target == source) return 0
    val N = routes.size
    val stopWithRoutes: MutableMap<Int, MutableList<Int>> = HashMap()
    for (route in 0 until N) {
        for (stop in routes[route]) {
            Arrays.sort(routes[route])
            // This makes sure this gets sth here
            stopWithRoutes.putIfAbsent(stop, ArrayList())

            // Here it woudl be like 1 -> 0
            // 5 -> 0, 1
            stopWithRoutes[stop]!!.add(route)
        }
    }
    val visitedRoutes: MutableSet<Int?> = HashSet()
    // [stops, # of buses taken so far here)
    val visitedStops: MutableSet<Int?> = HashSet()

    // queue = [(source, 0)]    (stop, bus number taken so far here)
    // Perform BFS by adding connected stops by routes each time
    val queue: Queue<Point> = LinkedList()

    // Build the graph.  Two buses are connected if
    // they share at least one bus stop.

    queue.add(Point(source, 0))

    while (!queue.isEmpty()) {
        val info: Point = queue.poll()
        val curStop: Int = info.x
        val busesTaken: Int = info.y
        if (!visitedStops.contains(curStop)) {

            // first check if we have reached the target
            if (curStop == target) {
                println(busesTaken)
                return busesTaken
            }

            // add the current stop to the visitedStops
            visitedStops.add(curStop)
        }

        // next add all unvisited stops in connected routes to the queue
        for (connectedRoute in stopWithRoutes[curStop]!!) {
            if (!visitedRoutes.contains(connectedRoute)) {
                for (connectedStop in routes[connectedRoute]) {
                    if (!visitedStops.contains(connectedStop)) {
                        queue.add(Point(connectedStop, busesTaken+1))
                    }
                }
                visitedRoutes.add(connectedRoute)
            }
        }
    }
    println()
    return -1
}
