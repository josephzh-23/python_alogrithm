package Backtracking


import Tree.Basic.TreeNode

// This can be linked to binary tree path problem
//https://leetcode.com/problems/path-sum-ii/description/
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
    pathSum(r, 22)
}
// TC - O(N^2)
fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int?>?> {
    val result: MutableList<List<Int?>?> = ArrayList()
    path(root, targetSum, ArrayList(), result)
    print(result)
    return result
}

private fun path(root: TreeNode?, sum: Int, path: MutableList<Int?>, result: MutableList<List<Int?>?>) {
    if (root == null) return
    path.add(root.value)
    if (root.left == null && root.right == null && sum == root.value) result.add(ArrayList(path))
    path(root.left, sum - root.value, path, result)
    path(root.right, sum - root.value, path, result)

/*
     It only comes here printing after it has reached all the end
     And returned from the previous recursion calls
    It will remove all the added values from before
    and return to the root node
 */
    println(path.toString())
    // We remove from the end
    path.removeAt(path.size - 1)

    // Will print like [5, 4, 11, 7]
    // [5, 4, 11, 2]        [5, 4, 11]
    // [5, 4]           [5]
}