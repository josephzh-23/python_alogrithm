package Tree

internal class Node(var key: Int) {
    var left: Node?
    var right: Node? = null

    init {
        left = right
    }
}

internal class BinaryTree {
    // Root of Binary Tree
    var root: Node? = null

    /* Given a binary tree, print its nodes according to the
      "bottom-up" postorder traversal. */
    // Wrappers over above recursive functions
    @JvmOverloads
    fun printPostorder(node: Node? = root) {
        if (node == null) return

        // first recur on left subtree
        printPostorder(node.left)

        // then recur on right subtree
        printPostorder(node.right)

        // now deal with the node
        print(node.key.toString() + " ")
    }

    companion object {
        // Driver code
        @JvmStatic
        fun main(args: Array<String>) {
            val tree = BinaryTree()
            tree.root = Node(1)
            tree.root!!.left = Node(2)
            tree.root!!.right = Node(3)
            tree.root!!.left!!.left = Node(4)
            tree.root!!.right!!.left = Node(5)

            tree.root!!.right!!.right = Node(6)

            tree.root!!.right!!.left!!.left = Node(7)
            tree.root!!.right!!.left!!.right = Node(8)
            // Function call
            println(
                    "\nPostorder traversal of binary tree is ")
            tree.printPostorder()
        }
    }
}