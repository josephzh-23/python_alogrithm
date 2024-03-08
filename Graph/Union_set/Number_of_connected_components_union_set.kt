// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
fun main() {
    var edges = arrayOf(
        intArrayOf(0, 1),
        intArrayOf(1, 2),
        intArrayOf(3, 4)
    )

    var edges2 = arrayOf(
        intArrayOf(0, 1),
        intArrayOf(1, 2),
        intArrayOf(2, 3),
        intArrayOf(3, 4)
    )
    /*
    Here the answer should give 2, since 0 - 1 - 2 connected
    and 3-4 connected here.
     */
    countComponents(5, edges2)
}

/*
Time complexity == O (n + M* log(n))    (with compression)
 no path compression here then we get          O (m *n)

n = num of nodes given   m = num of edges we have
 */


fun countComponents(n: Int, edges: Array<IntArray>): Int {
    var u = UnionFind22(n)
    for (edge in edges) {
        u.union(edge[0], edge[1])
    }
    print(u.numOfComponets)
    return u.numOfComponets
}

class UnionFind22(n: Int) {
    private val parents: IntArray
    private val ranks: IntArray

    // This vairable is used to check if a cycle
    var isCycle = false

    /*
    basically for every edges where there is no component
     */
    var numOfComponets = 0

    init {
        parents = IntArray(n)
        ranks = IntArray(n)
        numOfComponets = n
        for (i in parents.indices) {
            parents[i] = i
            ranks[i] = 1
        }
    }

    fun find(cur: Int): Int {
        var cur = cur
        var root = cur
        //  Find the root first
        while (root != parents[root]) {
            root = parents[root]
        }
        // Path Compression
        /*
            With path compression
            E - d - c- b - a- f

           E's root node is f, once we find root node, we make everything
           point to the root node(make it its parent), D->f, c-> f
           Everytime we do look up for d, c, e, f we can find its compoinent parent

           Now it's much more efficient
         */
        while (cur != root) {
            val curParent = parents[cur]
            parents[cur] = root
            cur = curParent
        }
        return root
    }

//    fun findComponentSize(cur: Int): Int {
//        val parent = find(cur)
//        return ranks[parent]
//    }


    // With each successful union, the number of componeent decreases
    fun union(node1: Int, node2: Int) {
        val node1Parent = find(node1)
        val node2Parent = find(node2)

        // If the same parent, that means a cycle is found
        if (node1Parent == node2Parent) {
            isCycle = true
            return
        }

        // And in the else case it would just keep going
        if (ranks[node1Parent] > ranks[node2Parent]) {
            parents[node2Parent] = node1Parent
            ranks[node1Parent] += ranks[node2Parent]
        } else {
            parents[node1Parent] = node2Parent
            ranks[node2Parent] += ranks[node1Parent]
        }
        numOfComponets--
    }
}