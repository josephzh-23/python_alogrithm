package Hard

import Tree.Basic.TreeNode


fun main() {
    var r = TreeNode(5)
    r.left = TreeNode(4)
    r.left!!.left = TreeNode(11)
    r.left!!.left!!.left  = TreeNode(7)
    r.left!!.left!!.right  = TreeNode(2)

    r.right = TreeNode(8)
    r.right!!.right = TreeNode(4)
    r.right!!.left = TreeNode(13)
    r.right!!.right!!.left = TreeNode(5)
    r.right!!.right!!.right = TreeNode(1)
    pathSumRec(r, 22)
}

fun pathSumRec(root: TreeNode?, targetSum: Int): List<List<Int?>?> {
    val result: MutableList<List<Int>> = ArrayList()
    pathSum(root, targetSum, ArrayList(), result)
    println(result)

    return result
}

private fun pathSum(root: TreeNode?, sum: Int, path: MutableList<Int>, result: MutableList<List<Int>>) {
    if (root == null) return
    path.add(root.value)
    if (root.left == null && root.right == null && sum == root.value) result.add(path)
    pathSum(root.left, sum - root.value, ArrayList<Int>(path), result)
    pathSum(root.right, sum - root.value, ArrayList<Int>(path), result)
}