package Graph

// And using this we have the code below

internal class DisjointSet(N: Int) {
    private val parents: IntArray
    fun Union(a: Int, b: Int) {
        val rootA = find(a)
        val rootB = find(b)
        // If both a and b have same root, i.e. they both belong to the same set, hence we don't need to take union
        if (rootA == rootB) return
        // Take union by assigning rootA as the parent of rootB
        parents[rootB] = rootA
    }

    fun find(a: Int): Int {
        // Traverse all the way to the top (root) going through the parent nodes
        var a = a
        while (a != parents[a]) {
            a = parents[a]
        }
        return a
    }

    fun isInSameGroup(a: Int, b: Int): Boolean {
        // Return true if both a and b belong to the same set, otherwise return false
        return find(a) == find(b)
    }


    /*
    WHile obtaining ancestor, compress path by assining
    assigning the grandparent of the node as the parent (
    thereby skipping connections and moving nodes closer to the root).
     */
    private fun findWithCompression(a: Int): Int {
        var a = a
        while (a != parents[a]) {
            // Path compression
            // a's grandparent is now a's parent
            parents[a] = parents[parents[a]]
            a = parents[a]
        }
        return a
    }
    init {
        parents = IntArray(N + 1)
        // Set the initial parent node to itself
        for (i in 1..N) {
            parents[i] = i
        }
    }
}