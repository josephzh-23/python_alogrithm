package Tree.Top6

import Tree.Basic.TreeNode

/*
Trav in reverse inorder right, r, left as indicated
notice that the inorder array will always be sorted as mentioned

keep a counter 0, when visiting a node
do a counter ++ check if (counter ==k)  that's the node
you are looking for
 */
class sol3(){

    var kt= 0
    var counter =0
    fun findKthSmallest(k:Int, node: TreeNode){
        kt =k
        traverse(node)
    }
    fun traverse(node: TreeNode?) {
        if (node == null) return

        traverse(node.left)
        counter++
//        if(counter ==kt){
            println(node.value)
//        }

        traverse(node.right)

    }
}

fun main() {
    var root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left?.right = TreeNode(2)
    sol3().findKthSmallest(1, root)

}


