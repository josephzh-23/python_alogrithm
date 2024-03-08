internal class UnionFind(size: Int) {
    var parent: IntArray
    var rank: IntArray

    init {
        parent = IntArray(size)
        for (i in 0 until size) parent[i] = i
        rank = IntArray(size)
    }

    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    fun union(x: Int, y: Int) {
        val xset = find(x)
        val yset = find(y)
        if (xset == yset) {
            return
        } else if (rank[xset] < rank[yset]) {
            parent[xset] = yset
        } else if (rank[xset] > rank[yset]) {
            parent[yset] = xset
        } else {
            parent[yset] = xset
            rank[xset]++
        }
    }
}

fun possibleBipartition(n: Int, dislikes: Array<IntArray>): Boolean {


    val adj: MutableMap<Int, MutableList<Int>?> = HashMap()
    for (edge in dislikes) {
        val a = edge[0]
        val b = edge[1]
        adj.computeIfAbsent(
            a
        ) { ArrayList() }!!
            .add(b)
        adj.computeIfAbsent(
            b
        ) { ArrayList() }!!
            .add(a)
    }
    val dsu = UnionFind(n + 1)
    for (node in 1..n) {
        if (!adj.containsKey(node)) continue

        // Go through each node in the list
        for (neighbor in adj[node]!!) {
            // Check if the node and its neighbor is in the same set.
            if (dsu.find(node) == dsu.find(neighbor)) return false
            // Move all the neighbours into same set as the first neighbour.
            dsu.union(adj[node]!![0], neighbor)
        }
    }
    return true
}