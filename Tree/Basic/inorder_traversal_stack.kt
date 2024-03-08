package Tree.Basic

import java.util.*

/*
TC: O(n)
S: O(h)     height of a tree (logN for a binary tree)
 */
// left center right
internal class BinaryTree {
    var root: TreeNode? = null
    fun inorder() {
        if (root == null) return
        val s: Stack<TreeNode> = Stack()
        var curr: TreeNode? = root

        // Traverse the tree
        while (curr != null || s.size > 0) {

            // Reach the left most Node of the
            // curr Node
            while (curr != null) {
                // Place pointer to a tree node on
                // the stack before traversing
                // the node's left subtree
                s.push(curr)
                curr = curr.left
            }

            // Current must be NULL at this point
            curr = s.pop()
            print(curr.value)

            // we have visited the node and its
            // left subtree. Now, it's right
            // subtree's turn
            curr = curr.right
        }
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            // Creating a binary tree and entering
            // the nodes
            val tree = BinaryTree()
            tree.root = TreeNode(1)
            tree.root!!.left = TreeNode(2)
            tree.root!!.right = TreeNode(3)
            tree.root!!.left?.left = TreeNode(4)
            tree.root!!.left?.right = TreeNode(5)
            tree.inorder()
        }
    }
}