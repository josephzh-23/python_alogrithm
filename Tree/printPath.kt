package Tree

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

    printPath(r)
//    println(Tree.Hard.hasPathSum(root, 8))
}
fun printPath(r: TreeNode?){

    if (r == null) return
    println(r.value)

    // In this case we have reached the end here the leaf node
    // will then know if valid or not
    printPath(r.left)
    printPath(r.right)

}