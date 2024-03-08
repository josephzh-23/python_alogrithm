package Graph.Union_set


// This is very effective when given a bunch of edges and then a list of list
// and then you see what would happen here
/*
We want to check the number of edges here, where we have the edges
as
 */

//var arr = intArrayOf(0, 1, 1, 2)
fun main() {
    // this below forms 0 1 2
    var edges = arrayOf(intArrayOf(0, 1),
            intArrayOf(0, 2),
            intArrayOf(1, 2))
    // the passed in n is very important
    var u = UnionFind22(4)
    for(edge in edges){
        u.union(edge[0], edge[1])
    }

    print(u.numberOfRedundantConnections)

}


class UnionFind22(n: Int) {
    private val parents: IntArray
    private val ranks: IntArray

    // This vairable is used to check if a cycle
    var numberOfRedundantConnections = 0

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
            numberOfRedundantConnections++
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
