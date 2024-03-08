package Tree

import Tree.Basic.TreeNode
import java.util.*
import kotlin.collections.ArrayList

/*
In this example we will ahve to add the example given above here
and then we have the code
 */ // We will add a new level at the each end of the queue here

fun bfs(r: TreeNode?): Int {

    var level = 1
    if (r == null) {
        return 0
    }

    var q = LinkedList<TreeNode>()
    r.let {
        q.add(it)
    }
    while (!q.isEmpty()) {
        for (i in 0 until q.size) {
            val cur = q.remove()
            cur.left?.let {
                q.add(it)
            }
            cur.right?.let {
                q.add(it)
            }
        }
        level += 1
    }
    return level
}