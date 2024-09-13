package Graph.Union_set


/*
Using below gives O(n) as expected
s1: [1, 2] put this into a set, and
then put this into [2, 3]
s1: [1, 2, 3 , 4]
and both 1-4 are in the same set, this would result in cycle


 */

// This is for undirected graph so the need to do for both

internal class Solution13 {
    lateinit var parent: IntArray
    fun findRedundantConnection(edges: Array<IntArray>): IntArray? {
        val n = edges.size


        parent = IntArray(n + 1)

        //make each node the parent of itself
        for (i in 0..n) parent[i] = i

        //Loop on all edges
        for (edge in edges) {
            // Ancestors are same then that's the edge to return
            // It can'be the same
            if (find(edge[0]) == find(edge[1])) return edge
            // else in the other case you just keep them together in the same boat
            union(edge[0], edge[1])
        }
        return null
    }
    // Find the ancestor of each node
    fun find(node: Int): Int {
        var node = node
        while (parent[node] != node) {
            node = parent[node]
        }
        return node
    }

    fun union(i: Int, j: Int) {
        val iRoot = find(i)
        val jRoot = find(j)
        // Only perform union if not the same
        if (iRoot != jRoot) {
            parent[jRoot] = iRoot
        }
    }
}