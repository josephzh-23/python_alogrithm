internal class Solution12 {
    fun isBipartite(graph: Array<IntArray>): Boolean {
        val n = graph.size
        val colors = IntArray(n)

        for (i in 0 until n) {
            //This graph might be a disconnected graph. So check each unvisited node.

            // Make sure it's 0 first over here
            if (colors[i] == 0 && !validColor(graph, colors, 1, i)) {
                return false
            }
        }
        return true
    }

    // Check color on the node first
    // We basically pass in an alternating colors here
    fun validColor(graph: Array<IntArray>, colors: IntArray, color: Int, node: Int): Boolean {
        if (colors[node] != 0) {
            return colors[node] == color
        }

        // Make unvisited == 1 over here
        colors[node] = color

        // For the next in graph here
        // graph[0]: [1, 2, 3] an interesting take here
        // We basically pass in teh opposite of that color here
        // it would be -color
        for (next in graph[node]) {
            if (!validColor(graph, colors, -color, next)) {
                return false
            }
        }
        return true
    }
}

