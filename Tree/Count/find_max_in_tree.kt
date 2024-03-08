package Tree.Count

import Tree.Basic.TreeNode
import java.lang.Integer.max


//
class Solution12() {
    var prev: Int? = null

    var maximum = 0
    fun findMaxInTree(r: TreeNode) {

        // And then when you come here
        // you would begin with sth like
        // use a max

        traverse(r, maximum)
        println(maximum)

    }

    fun traverse(node: TreeNode?, max: Int) {
        if (node == null) return

        traverse(node.left, max)

        // max gets updated when compared to previous
        if (prev != null) {
            maximum = max(maximum, prev!!)
        }

        prev = node.value
        traverse(node.right, maximum)

    }
}


fun main() {
    var s = Solution12()
    val root = TreeNode(1)
    root.left = TreeNode(8)
    root.left?.left = TreeNode(8)
    root.left?.left?.right = TreeNode(831)
    root.left?.left?.right?.left = TreeNode(5)
    root.left?.left?.right?.right = TreeNode(6)
    root.right = TreeNode(7)
    root.right?.right = TreeNode(8)
    root.right?.right?.left = TreeNode(9)
    root.right?.right?.left?.left = TreeNode(10)
    root.right?.right?.left?.right = TreeNode(11)

    s.findMaxInTree(root)
}