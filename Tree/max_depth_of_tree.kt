package Tree

import Tree.Basic.TreeNode
import java.lang.Integer.max
import java.util.*

/*
We will do pre-order traversal of this question

 */
fun maxDepth(r: TreeNode): Int { // the value here
    var stack = Stack<Pair<TreeNode?, Int>>()
    var res = 0

    while (stack.isNotEmpty()) {
        var (node, depth) = stack.pop()
        node?.let {
            res = max(res, depth)
            stack.add(Pair(it.left, depth + 1))
            stack.add(Pair(it.right, depth + 1))
        }
    }
    return res
}