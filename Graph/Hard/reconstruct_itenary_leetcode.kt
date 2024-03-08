import java.util.*


internal class Solution3332 {
    var graph: MutableMap<String, MutableList<String>?> = HashMap()
    var path: MutableList<String> = LinkedList()
    fun findItinerary(tickets: List<List<String>>): List<String> {
        //Create the graph lexical order
        for (ticket in tickets) {
            val start = ticket[0]
            val end = ticket[1]
            if (!graph.containsKey(start)) {
                graph[start] = LinkedList()
            }
            if (!graph.containsKey(end)) {
                graph[end] = LinkedList()
            }
            graph[start]!!.add(end)
        }
        for (key in graph.keys) {
            Collections.sort(graph[key])
        }

        //Find itinerary path
        val start = "JFK"
        findItinerary(start, tickets.size)
        return path
    }

    private fun findItinerary(start: String, edgesCount: Int): Boolean {
        val list: MutableList<String>? = graph[start]
        path.add(start)
        //Base Case
        if (list!!.size == 0) {
            return if (edgesCount == 0) true else false
        }
        for (i in list.indices) {
            val top: String = list.removeAt(i)
            if (findItinerary(top, edgesCount - 1)) return true
            list.add(i, top)
            path.removeAt(path.size - 1)
        }
        return false
    }
}