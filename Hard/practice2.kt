import Tree.Basic.TreeNode

//fun pathSum(root: Tree.Basic.TreeNode?, targetSum: Int): List<List<Int>> {
//
//
//
//}


// in order left, r, right
// preOrder: r, left and right
// postOrder: left, right, center
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
    inorderTraverse(r, 22)
}

var result = mutableListOf<MutableList<Int>>()
fun inorderTraverse(root: TreeNode?, sum: Int): List<Int> {
    val res: MutableList<Int> = ArrayList()
    helper2(root, res, sum )
//    res.forEach {
//        println(it)
//    }
//    return res
   result.forEach {
       println(it)
   }
    return emptyList()
}

fun helper2(r: TreeNode?, res: MutableList<Int>, remainingSum: Int) {

    var res = res
    if (r != null) {
        if(r.left == null && r.right == null){
            result.add(res)
        }
        helper2(r.left, res, remainingSum-r.value)
        if(remainingSum==0){
            res.add(r.value)
        }
        helper2(r.right, res, remainingSum-r.value)

        // Because we have found 1 path or have failed
        // When it backtracks to here
        remainingSum + r.value
        res.removeLast()
    }

}