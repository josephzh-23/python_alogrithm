package Tree.Count

import Tree.Basic.TreeNode
import java.util.*

fun hasPathSumIter(root: TreeNode?, sum: Int): Boolean {
    if (root == null) return false
    val node_stack: LinkedList<TreeNode> = LinkedList()
    val sum_stack: LinkedList<Int> = LinkedList()
    node_stack.add(root)
    sum_stack.add(sum - root.value)
    var node: TreeNode
    var curr_sum: Int
    while (!node_stack.isEmpty()) {
        node = node_stack.pollLast()
        curr_sum = sum_stack.pollLast()
        if (node.right == null && node.left == null && curr_sum == 0) return true
        if (node.right != null) {
            node_stack.add(node.right!!)
            sum_stack.add(curr_sum - node.right!!.value)
        }
        if (node.left != null) {
            node_stack.add(node.left!!)
            sum_stack.add(curr_sum - node.left!!.value)
        }
    }
    return false
}