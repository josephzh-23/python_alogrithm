package Tree.Hard

import Tree.Basic.TreeNode

fun main() {
    var r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left!!.left = TreeNode(4)
    r.right!!.left = TreeNode(5)
    r.right!!.right = TreeNode(6)

    r.right!!.left!!.left = TreeNode(7)
    r.right!!.left!!.right = TreeNode(8)

    // You
    println(hasPathSum(r, 15))
}


fun hasPathSum(root: TreeNode?, sum: Int): Boolean {
    var sum = sum
    if (root == null) return false
    println("$sum with value ${root.value}")
    sum -= root.value

    // In this case we have reached the end here the leaf node
    // will then know if valid or not
    return if (root.left == null && root.right == null) sum == 0

    else
        hasPathSum(root.left, sum) || hasPathSum(root.right, sum)
}