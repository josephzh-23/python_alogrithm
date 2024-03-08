package Tree

import Tree.Basic.TreeNode

// in order left, r, right
// preOrder: r, left and right
// postOrder: left, right, center
fun main() {
    var root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left!!.left = TreeNode(4)
    root.right!!.left = TreeNode(5)
    root.right!!.right = TreeNode(6)

    root.right!!.left!!.left = TreeNode(7)
    root.right!!.left!!.right = TreeNode(8)
    inorderTraverse(root)
}

fun inorderTraverse(root: TreeNode?): List<Int> {
    val res: MutableList<Int> = ArrayList()
    helper2(root, res)
    res.forEach {
        println(it)
    }
    return res

}

fun helper2(root: TreeNode?, res: MutableList<Int>) {
    if (root != null) {
        helper2(root.left, res)
        res.add(root.value)
        helper2(root.right, res)
    }
}