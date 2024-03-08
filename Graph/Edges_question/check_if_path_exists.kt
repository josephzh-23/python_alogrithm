package Graph.Edges_question

// Check if path exists
// https://leetcode.com/problems/find-if-path-exists-in-graph/
fun main() {
// following will print 2
    // since 0-1-2      2nd connected: 3-4
    println(
            validPath(
                    6, arrayOf(
                    intArrayOf(0, 1), intArrayOf(0, 2),
                    intArrayOf(3, 5), intArrayOf(5, 4), intArrayOf(4, 3)
            ), 0, 4
            )
    )
}

fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
    val graph: MutableMap<Int, MutableList<Int>> = HashMap()
    val seen = BooleanArray(n)
    for (edge in edges) {
        val a = edge[0]
        val b = edge[1]
        graph.computeIfAbsent(
                a
        ) { ArrayList() }.add(b)
        graph.computeIfAbsent(
                b
        ) { ArrayList() }.add(a)
    }
    return dfs(graph, seen, source, destination)
}

private fun dfs(graph: Map<Int, MutableList<Int>>, seen: BooleanArray, currNode: Int, destination: Int): Boolean {


    if (currNode == destination) {
        return true
    }
    if (!seen[currNode]) {
        seen[currNode] = true

        // In the next neighbor here
        for (nextNode in graph[currNode]!!) {

//            println("$currNode and ${graph[currNode]} and $nextNode")
            if (dfs(graph, seen, nextNode, destination)) {
                return true
            }
        }
    }
    return false
}

