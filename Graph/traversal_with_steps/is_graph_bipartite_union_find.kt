import January_3rd.print

// This will not actually work since you would have to
// iterate over the adjacent node which works by the theory

// of bfs( adjacent)

// Using union find

// Using unino find code here
// Using union find code here


fun main() {
    var s = arrayOf(intArrayOf(1, 2, 3), intArrayOf(0, 2),
            intArrayOf(0, 1, 3), intArrayOf(0, 2))

    Solution1().isGraphbipartite(s).print()
}

internal class Solution1 {
    lateinit var parent: IntArray
    fun isGraphbipartite(g: Array<IntArray>): Boolean {
        val n = g.size
        parent = IntArray(n + 1)

        //make each node the parent of itself
        for (i in 0..n) parent[i] = i

        //Loop on all edges
        for (i in 0 until g.size) {

            // all the negihbors
            var adj = g[i]
            for(j in 0 until adj.size){

                // Have to check if you same parent first?
                if(find(i) == find(adj[j])){
                    return false
                }
                union(i, adj[j])
            }
        }
        return true
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









