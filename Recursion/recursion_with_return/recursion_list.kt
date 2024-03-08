package Recursion.recursion_with_return

import Tree.Basic.TreeNode

// Root comes first, then left subtree
// right subtree

/*
           3
      4         5
    1   6     3   7
    [3, 4, 1, 6, 5, 3, 7]
 */
fun main() {
    var root = TreeNode(3)
    root.left = TreeNode(4)
    root.left!!.left = TreeNode(1)
    root.left!!.right = TreeNode(6)

    root.right = TreeNode(5)
    root.right!!.left = TreeNode(3)
    root.right!!.right = TreeNode(7)
    preorderTraversal(root)
}
fun preorderTraversal(root: TreeNode?): List<Int>? {
    val res: MutableList<Int> = ArrayList()
    if (root == null) {
        return res
    }
    res.add(root.value)
    // Can do print and then you would see the printed list here
    println(root.value)
    root.left?.let {
        res.addAll(preorderTraversal(it)!!)
    }
    res.addAll(preorderTraversal(root.right)!!)
    return res
}