import Util.printList
import java.util.*
// This is an extra hard problem leetcode here

fun main() {
    var n = 7
    var edges = arrayOf(
        intArrayOf(0, 1), intArrayOf(0, 2),
        intArrayOf(1, 4), intArrayOf(1, 5), intArrayOf(2, 3), intArrayOf(2, 6)
    )
    var labels = "abaedcd"
    printList(countSubTrees(n, edges, labels).toList())
}


// So at the beginnign we will insert Element(0, -1)
class Element(var id: Int, var parent: Int)

fun dfs(
    element: Element, adj: Map<Int?, MutableList<Int?>?>,
    labels: CharArray, ans: IntArray
): IntArray {


    var curNode = element.id
    var parent = element.parent
    // Node count has 26 letters, and then for the first one
    // a: 1    for example
    val nodeCounts = IntArray(26)

    if (!adj.containsKey(curNode)) return nodeCounts
    for (child in adj[curNode]!!) {
        if (child == parent) {
            continue
        }

        val childCounts = dfs(Element(child!!, curNode), adj, labels, ans)
        // Add frequencies of the child node in the parent node's frequency array.
        for (i in 0..25) {

            // Say if 1 has child 2 and child 2 has b
            nodeCounts[i] += childCounts[i]
        }
    }

    // here we increment the count of the current node label
    var ch = labels[curNode]
    nodeCounts[ch.toInt() - 'a'.toInt()] = 1

    ans[curNode] = nodeCounts[ch.toInt() - 'a'.toInt()]
    return nodeCounts
}

fun countSubTrees(n: Int, edges: Array<IntArray>, labels: String): IntArray {
    val adj: MutableMap<Int?, MutableList<Int?>?> = HashMap()
    for (edge in edges) {
        val a = edge[0]
        val b = edge[1]
        adj.computeIfAbsent(a) { ArrayList() }!!.add(b)
        adj.computeIfAbsent(b) { ArrayList() }!!.add(a)
    }

    val ans = IntArray(n)
    val label = labels.toCharArray()
    dfs(Element(0, -1), adj, label, ans)
    return ans
}