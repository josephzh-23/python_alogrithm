package Graph.Top_6

import January_3rd.print
import java.util.*


var dict = IntArray(26)
var a = 'a'

fun main() {
    var numCourses = 4

    var preReq = arrayOf(charArrayOf('a', 'd'),
    charArrayOf('f', 'b'), charArrayOf('b', 'd'), charArrayOf('f', 'a'),
        charArrayOf('d', 'c')
    )

    findOrder(6, preReq).forEach {
        print(it)
    }
}
// Comparing the alphabets here
// This gets the build order self problem as said before
// We do this with the other one
fun findOrder(numCourses: Int, prerequisites: Array<CharArray>): CharArray {
    val adjList: MutableMap<Char, MutableList<Char>?> = HashMap()
    val indegree = mutableMapOf<Char, Int>()
    val topologicalOrder = CharArray(numCourses)

    // Create the adjacency list representation of the graph
    for (i in prerequisites.indices) {
        val src = prerequisites[i][0]
        val dest = prerequisites[i][1]
        val lst = adjList.getOrDefault(src, ArrayList())!!
        lst.add(dest)
        adjList[src] = lst

        indegree.putIfAbsent(src, 0)
        // Record in-degree of each vertex
        indegree.putIfAbsent(dest, 0)

        // THe source also needs 0 as well
        indegree[dest] = indegree[dest]!! + 1
    }

    // Add all vertices with 0 in-degree to the queue
    val q: Queue<Char> = LinkedList<Char>()

    // Add all the char that has 0 frequencies here a
    while (a.hashCode() <= 'z'.hashCode()) {
        if (indegree[a] == 0) {
            q.add(a)
        }
        a++
    }
    var i = 0

    println(q)
    // Process until the Q becomes empty
    while (!q.isEmpty()) {
        val node = q.remove()
        topologicalOrder[i++] = node

        // Reduce the in-degree of each neighbor by 1
        if (adjList.containsKey(node)) {
            for (neighbor in adjList[node]!!) {
                println("the neighbor is $neighbor")

                // You check how many number with the char
                indegree[neighbor] = indegree[neighbor]?.minus(1) ?: 0

                // If in-degree of a neighbor becomes 0, add it to the Q
                if (indegree[neighbor] == 0) {

                    q.add(neighbor)
                }
            }
        }
    }
    topologicalOrder.forEach { println(it.toString()) }
    return topologicalOrder
}