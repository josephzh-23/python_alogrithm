package Graph.Edges_question


//For each edge (u, v), traverse the graph with a depth-first search
// to see if we can connect u to v. If we can, then it must be the duplicate edge.

var MAX_EDGE_VAL = 1000

fun main() {
    var edges = arrayOf(intArrayOf(1, 2),
    intArrayOf(1, 3), intArrayOf(2, 3))
    findRedundantConnection(edges).forEach {
        println(it)
    }
}
fun findRedundantConnection(edges: Array<IntArray>): IntArray {
    var seen: MutableSet<Int> = HashSet()

    val graph: Array<ArrayList<Int>> = Array(MAX_EDGE_VAL + 1) { ArrayList<Int>() }
    for (i in 0..MAX_EDGE_VAL) {
        graph[i] = ArrayList()
    }
    for (edge in edges) {
        seen.clear()
        if (!graph[edge[0]].isEmpty() && !graph[edge[1]].isEmpty() &&
                dfs(graph, edge[0], edge[1], seen)) {
            return edge
        }
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    }
    throw AssertionError()
}

fun dfs(graph: Array<ArrayList<Int>>, source: Int, target: Int,
seen:MutableSet<Int>): Boolean {
    if (!seen.contains(source)) {
        seen.add(source)
        if (source == target) return true
        for (nei in graph[source]) {
            if (dfs(graph, nei, target, seen)) return true
        }
    }
    return false
}