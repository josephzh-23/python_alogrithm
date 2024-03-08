package Graph


// O number of network operations connected here
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/editorial/
// Question number of operations to make the network connected here
fun main() {
    var s = Solution14()
//    var edges = arrayOf(
//        intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(0, 3),
//
//        intArrayOf(1, 2), intArrayOf(1, 3)
//    )
    var edges = arrayOf(
        intArrayOf(0, 1), intArrayOf(0, 2), intArrayOf(0, 3),

        intArrayOf(1, 2)
    )
    s.findRedundantConnection(edges)?.forEach {
        it.forEach { println(it) }
    }
}

/*
Using below gives O(n) as expected
s1: [1, 2] put this into a set, and
then put this into [2, 3]
s1: [1, 2, 3 , 4]
and both 1-4 are in the same set, this would result in cycle

// Connections
 */

// This is for undirected graph so the need to do for both

internal class Solution14 {
    lateinit var parent: IntArray
    lateinit var excessiveEdges: MutableList<IntArray>
    fun findRedundantConnection(edges: Array<IntArray>): MutableList<IntArray>? {
        val n = edges.size

        excessiveEdges = mutableListOf()
        parent = IntArray(n + 1)

        //make each node the parent of itself
        for (i in 0..n) parent[i] = i

        //Loop on all edges
        for (edge in edges) {
            // Ancestors are same then that's the edge to return
            if (find(edge[0]) == find(edge[1])) excessiveEdges.add(edge)
            // else in the other case you just keep them together in the same boat
            union(edge[0], edge[1])
        }

        if (excessiveEdges.isNotEmpty()) {
            return excessiveEdges
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