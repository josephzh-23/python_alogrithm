import Tree.Basic.TreeNode

// Try finding max here

fun main() {
    var root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left!!.left = TreeNode(4)
    root.right!!.left = TreeNode(5)
    root.right!!.right = TreeNode(6)

    root.right!!.left!!.left = TreeNode(7)
    root.right!!.left!!.right = TreeNode(8)
    var max = 0
    inorderTraversal(root, max)
    println(max)
}

fun inorderTraversal(r: TreeNode?, max: Int): List<Int> {
    val res: MutableList<Int> = ArrayList()



    helper(r, res, max)
    res.forEach {
        println(it)
    }
    return res

}

fun helper(r: TreeNode?, res: MutableList<Int>, max: Int) {
   var max = max
    if (r != null) {
        if (r.value > max) {
            max = r.value
        }
        helper(r.left, res, max)
        res.add(r.value)
        helper(r.right, res, max)
    }
}