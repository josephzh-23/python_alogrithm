package Tree

import Tree.Basic.TreeNode

internal class BinaryTre23e {
    var root: Node? = null

    companion object {
        // Returns the max value in a binary tree
        fun findMax(node: TreeNode?): Int {
            if (node == null) return Int.MIN_VALUE
            var res: Int = node.value
            val lres: Int = findMax(node.left)
            val rres: Int = findMax(node.right)
            if (lres > res) res = lres
            if (rres > res) res = rres
            return res
        }

        /* Driver code */
        @JvmStatic
        fun main(args: Array<String>) {

            val root = TreeNode(1)
            root.left = TreeNode(8)
            root.left?.left = TreeNode(8)
            root.left?.left?.right = TreeNode(831)
            root.left?.left?.right?.left = TreeNode(5)
            root.left?.left?.right?.right = TreeNode(6)
            root.right = TreeNode(7)
            root.right?.right = TreeNode(8)
            root.right?.right?.left = TreeNode(9)

            // Function call
            println("Maximum element is "
                    + Companion.findMax(root))
        }
    }
}