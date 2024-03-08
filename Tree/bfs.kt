package Tree

import Tree.Basic.TreeNode
import java.util.*
import kotlin.collections.ArrayList


fun levelOrder(r: TreeNode?): List<List<Int>> {

    var results = ArrayList<List<Int>>()
    if (r == null) {
        return results
    }

    var q = LinkedList<TreeNode>()
    r?.let {
        q.add(it)
    }
    while (!q.isEmpty()) {
        val curLevel = ArrayList<Int>()
        // The num of nodes in cur level
        for (i in 0 until q.size) {
            val cur = q.remove()
            curLevel.add(cur.value)
            cur.left?.let {
                q.add(it)
            }
            cur.right?.let {
                q.add(it)
            }
        }
        results.add(curLevel.toList())

    }
    results.forEach {
        println(it)
    }
    return results
}


fun main() {
    var root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    insert(root, 6)
    insert(root, 7)
    levelOrder(root)
}