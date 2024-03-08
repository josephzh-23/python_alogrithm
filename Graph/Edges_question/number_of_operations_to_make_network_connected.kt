package Graph.Edges_question


// So we would have here a list of
// [[0, 1], [0, 2], [0, 3], [1, 2]]

// Better to use the map here


internal class Solution {
    fun dfs(node: Int, adj: Map<Int?, MutableList<Int?>?>, visit: BooleanArray) {
        visit[node] = true
        if (!adj.containsKey(node)) {
            return
        }
        for (neighbor in adj[node]!!) {
            if (!visit[neighbor!!]) {
                visit[neighbor] = true
                dfs(neighbor, adj, visit)
            }
        }
    }

    fun makeConnected(n: Int, connections: Array<IntArray>): Int {
        if (connections.size < n - 1) {
            return -1
        }
        val adj: MutableMap<Int?, MutableList<Int?>?> = HashMap()
        for (connection in connections) {
            adj.computeIfAbsent(connection[0]) { k: Int? -> ArrayList() }!!.add(connection[1])
            adj.computeIfAbsent(connection[1]) { k: Int? -> ArrayList() }!!.add(connection[0])
        }
        var numberOfConnectedComponents = 0

        // So we are increasing the number of connected componets by 1
        // every single time we visit a node
        val visit = BooleanArray(n)
        for (i in 0 until n) {
            if (!visit[i]) {
                numberOfConnectedComponents++
                dfs(i, adj, visit)
            }
        }
        return numberOfConnectedComponents - 1
    }
}