package Tree

import Tree.Basic.TreeNode
import java.util.*



internal object Main {
    // Iterative function to perform inorder traversal on the tree
    fun inorderIterative(root: TreeNode?) {
        // create an empty stack
        val stack = Stack<TreeNode>()

        // start from the root node (set current node to the root node)
        var curr = root

        // if the current node is null and the stack is also empty, we are done
        while (!stack.empty() || curr != null) {

            if (curr != null) {
                stack.push(curr)
                curr = curr.left
            } else {
                // This is the parent stuff
                curr = stack.pop()
                print(curr.value.toString() + " ")

                // Then we traverse to the right
                curr = curr.right
            }
        }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        /* Construct the following tree
                   1
                 /   \
                /     \
               2       3
              /      /   \
             /      /     \
            4      5       6
                  / \
                 /   \
                7     8
        */
        val root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left!!.left = TreeNode(4)
        root.right!!.left = TreeNode(5)
        root.right!!.right = TreeNode(6)
        root.right!!.left!!.left = TreeNode(7)
        root.right!!.left!!.right = TreeNode(8)
        inorderIterative(root)
    }
}