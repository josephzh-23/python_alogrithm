package Graph.Top_6


internal class Solution6 {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        val graph: MutableMap<Int, MutableList<Int>> = HashMap()
        val seen = BooleanArray(n)
        for (edge in edges) {
            val a = edge[0]
            val b = edge[1]
            graph.computeIfAbsent(a) { `val`: Int? -> ArrayList() }.add(b)
            graph.computeIfAbsent(b) { `val`: Int? -> ArrayList() }.add(a)
        }
        return dfs(graph, seen, source, destination)
    }

    private fun dfs(graph: Map<Int, MutableList<Int>>, seen: BooleanArray, currNode: Int, destination: Int): Boolean {
        if (currNode == destination) {
            return true
        }
        if (!seen[currNode]) {
            seen[currNode] = true
            for (neigh in graph[currNode]!!) {
                if (dfs(graph, seen, neigh, destination)) {
                    return true
                }
            }
        }
        return false
    }
}