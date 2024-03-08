package Graph

import java.util.*

/*
For example, the pair [0, 1],
indicates that to take course 0 you have to first take course 1.
 */
// We have an indegree order, topological order
internal class Solution13 {
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
        val isPossible = true

        // This is the matrix adjacency list
        // src  ->  destination here
        // 0 : [ 1, 2, 3 ]
        val adjList: MutableMap<Int, MutableList<Int>> = HashMap()

        // This gets decreased when the destination is visited here
        val indegree = IntArray(numCourses)

        // The topological order
        val topologicalOrder = IntArray(numCourses)

        // Create the adjacency list representation of the graph
        for (i in prerequisites.indices) {

            /*
             So here : [0, 1]       [0]     [1] take 1 before you take 0 over here
             */
            val dest = prerequisites[i][0]
            val src = prerequisites[i][1]

//            val lst = adjList.getOrDefault(src, ArrayList())
//            lst.add(dest)
//            adjList[src] = lst


            // Need to add this otherwise if absent
            adjList.putIfAbsent(src, ArrayList())
            adjList[src]?.add(dest)
            // Record in-degree of each vertex
            indegree[dest] += 1
        }

        // Add all vertices with 0 in-degree to the queue
        val q: Queue<Int> = LinkedList()
        for (i in 0 until numCourses) {

            //No more indegrees here
            if (indegree[i] == 0) {
                q.add(i)
            }
        }
        var i = 0
        // Process until the Q becomes empty
        while (!q.isEmpty()) {
            val node = q.remove()
            topologicalOrder[i++] = node

            // Reduce the in-degree of each neighbor by 1
            if (adjList.containsKey(node)) {

                // For the neighbor of that node
                for (neighbor in adjList[node]!!) {
                    indegree[neighbor]--

                    // If in-degree of a neighbor becomes 0, add it to the Q
                    if (indegree[neighbor] == 0) {
                        q.add(neighbor)
                    }
                }
            }
        }

        // Check to see if topological sort is possible or not.
        return if (i == numCourses) {
            topologicalOrder

            // If we get to this point here there is no cycle
        } else IntArray(0)

    }
}