package Graph.Edges_question

import java.util.*


// This is the solution from the bfs one




fun main() {
    var arr = arrayOf(
        intArrayOf(1, 2), intArrayOf(3), intArrayOf(3), intArrayOf()
    )

    allPathSourceTarget23(arr)
}
/*
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
 */
fun allPathSourceTarget23(graph: Array<IntArray>): List<List<Int>> {
    val result: MutableList<List<Int>> = ArrayList()
    val queue: Queue<List<Int>> = LinkedList()
    queue.add(Arrays.asList(0))
    val goalNode = graph.size - 1
    while (!queue.isEmpty()) {

        // So the path here would be sth like
        // [0]      [0, 1]      [0, 2]
        val path = queue.poll()

        // we check by the last node in here
        val lastNode = path[path.size - 1]

        println(path)
        if (lastNode == goalNode) {
            result.add(ArrayList(path))
        } else {
            val neighbors = graph[lastNode]
            for (neighbor in neighbors) {
                // initially it will be 0
                // then [0, 1]  and [0, 2] here
                // Basically for each neighbor we will have a list
                val list: MutableList<Int> = ArrayList(path)
                list.add(neighbor)
                queue.add(list)
            }
        }
    }
    return result
}