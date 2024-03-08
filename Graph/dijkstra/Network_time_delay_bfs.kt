import January_3rd.print
import java.util.*


// We will make sure htis works first and then modify here



// We can just use this with a bfs for simplicity here
fun main() {
    var times = arrayOf(
        intArrayOf(2, 1, 1),
        intArrayOf(2, 3, 1),
        intArrayOf(3, 4, 1)
    )
    var (n, k) = arrayOf(4, 2)

    networkDelayTime(times, n, k).print()
}



fun networkDelayTime(times: Array<IntArray>, n: Int, k: Int): Int {

    // create an adj list of eahc node and its connections


    val adj: MutableMap<Int, MutableList<IntArray>?> = HashMap()
    for (i in times)  // The 2nd value is the price
        adj.computeIfAbsent(
            i[0]
        ) { value: Int? -> ArrayList() }!!
            .add(intArrayOf(i[1], i[2]))


    // Create an array of min visit time to the each node here
    val minimumVisitTimes = IntArray(n + 1)

    // At the start it's all this here
    Arrays.fill(minimumVisitTimes, -1)
    minimumVisitTimes[k] = 0

    // Push node unto the queue here
    val queue = ArrayDeque<Int>()
    queue.add(k)

    // WHie the q has nodes
    while (queue.size != 0) {

        // Pop node off the q
        val node = queue.remove()

        // For each of the exstiign node, check if the min time to visit
        // from cur node < existing min visit time
        val timeToCurNode = minimumVisitTimes[node]

        adj[node]?.let {
            for (neighbor in it) {
                val destNode = neighbor[0]
                val timeToDestNode = neighbor[1]
                if (minimumVisitTimes[destNode] == -1 || timeToCurNode + timeToDestNode <
                    minimumVisitTimes[destNode]
                ) {

                    //
                    minimumVisitTimes[destNode] = timeToCurNode + timeToDestNode

                    // Push the adjcent node unto the q if the min time was udpated here
                    queue.add(destNode)
                }
            }
        }
    }

    // Find the max visit tiem from all nodes here
    var maxVisitTime = -1
    for (i in 1 until n + 1) {
        val visitTime = minimumVisitTimes[i]

        // if one of the visit time is still this, then impossible to reach
        // all the nodes
        if (visitTime == -1) {
            return -1
        }
        if (visitTime > maxVisitTime) {
            maxVisitTime = visitTime
        }
    }
    return maxVisitTime
}
