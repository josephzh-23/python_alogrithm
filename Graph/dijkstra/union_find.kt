package Graph.Top_6

// This is basedon the union find example

internal class Solution1 {
    lateinit var parent: IntArray
    fun findRedundantConnection(edges: Array<IntArray>): IntArray? {
        val n = edges.size
        parent = IntArray(n + 1)

        //make each node the parent of itself
        for (i in 0..n) parent[i] = i

        //Loop on all edges
        for (edge in edges) {
            if (find(edge[0]) == find(edge[1])) return edge
            union(edge[0], edge[1])
        }
        return null
    }

    fun find(node: Int): Int {
        var node = node
        while (parent[node] != node) {
            node = parent[node]
        }
        return node
    }

    // No path compression here
    fun union(i: Int, j: Int) {
        val iRoot = find(i)
        val jRoot = find(j)
        if (iRoot != jRoot) {
            parent[jRoot] = iRoot
        }
    }
}