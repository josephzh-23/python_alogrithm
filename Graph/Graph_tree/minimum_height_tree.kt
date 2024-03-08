package Graph.Graph_tree

import January_3rd.print
import java.util.*

// TC: O(n) here and space: O(n)

fun main() {
    var arr = arrayOf(intArrayOf(3, 0),
    intArrayOf(3, 1), intArrayOf(3, 2), intArrayOf(3, 4)
    , intArrayOf(5, 4))
    findMinHeightTrees(6,arr).print()
}
fun findMinHeightTrees(
    n: Int,
    edges: Array<IntArray>
): List<Int> {
    var n = n
    val res: MutableList<Int> = ArrayList()
    if (n <= 0) return res
    if (n == 1) {
        res.add(0)
        return res
    }
    val degree = IntArray(n)
    val adj: MutableList<MutableList<Int>> = ArrayList()
    for (i in 0 until n) {
        adj.add(ArrayList())
    }
    for (e in edges) {
        degree[e[0]]++
        degree[e[1]]++
        adj[e[0]].add(e[1])
        adj[e[1]].add(e[0])
    }
    val q: Queue<Int> = LinkedList()
    for (i in 0 until n) {
        if (degree[i] == 1) {
            q.add(i)
        }
    }
    while (n > 2) {
        var size = q.size
        n -= size
        while (size-- > 0) {
            val v = q.poll()

            // So here basically 3 has a degree of 4
            // And each time its neighbor popped, its degree gets down by1
            // Check the neighbor of v
            // Each time it's checked --
            for (i in adj[v]) {

                println(i)
                degree[i]--

                if (degree[i] == 1) {
                    q.add(i)
                }
            }
        }
    }
    res.addAll(q)
    return res
}