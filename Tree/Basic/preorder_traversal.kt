package Tree.Basic

// Data structure to store a binary tree node


// Recursive function to perform preorder traversal on the tree
fun preorder(root: TreeNode?) {
    // return if the current node is empty
    if (root == null) {
        return
    }
    print(root.value.toString() + " ")
    preorder(root.left)
    preorder(root.right)
}

fun main(args: Array<String>) {
    /* Construct the following tree
               1
             /   \
           2       3
          /      /   \
        4      5       6
              / \
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
    preorder(root)
}