package Tree

import Tree.Basic.TreeNode

fun insert(root: TreeNode?, key: Int): TreeNode {

    /* If the tree is empty,
           return a new node */
    var root = root
    if (root == null) {
        root = TreeNode(key)
        return root
    } else if (key < root.value) root.left = insert(root.left, key)
    else if (key > root.value) root.right = insert(root.right, key)

    /* return the (unchanged) node pointer */return root
}