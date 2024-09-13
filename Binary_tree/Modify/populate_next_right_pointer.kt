package Tree.Top6

import java.util.*
import kotlin.collections.ArrayList


/*
O(n)    o(n)
 */
class Node(var `val`: Int) {
    var left: Node? = null
    var right: Node? = null
    var next: Node? = null
}
class Solution13 {
    fun connect(r: Node?): Node? {
        var cur = r
        var results = ArrayList<Int>()

        var q = LinkedList<Node>()
        r?.let {
            q.add(it)
        }

        cur?.next = null
        while (!q.isEmpty()) {
            val curLevel = ArrayList<Int>()

            // At each level when begin
            var dummy = Node(0)

            // The num of nodes in cur level

            for (i in 0 until q.size) {
                var node = q.remove()

                // 2-> 3 -> null
                dummy.next = node

                // Traverse forward here
                dummy.next?.also { dummy = it }

                node.left?.let {
                    q.add(it)
                }
                node.right?.let {
                    q.add(it)
                }
            }
        }
        return r
    }
}