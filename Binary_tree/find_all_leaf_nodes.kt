package Tree

import Tree.Basic.TreeNode


fun main(args: Array<String>) {
    /* Construct the following tree
               1
             /   \
           2       3
          /      /   \
        4      5       6
              / \
            7     8
    */
    val r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left!!.left = TreeNode(4)
    r.right!!.left = TreeNode(5)
    r.right!!.right = TreeNode(6)
    r.right!!.left!!.left = TreeNode(7)
    r.right!!.left!!.right = TreeNode(8)
    printAllLeafNodes(r, mutableListOf()).forEach{
        println(it.value)
    }
}
fun printAllLeafNodes(r: TreeNode?, list: MutableList<TreeNode>):
MutableList<TreeNode>{

    if(r==null){
        return mutableListOf()
    }
    // reach a leaf node here
    if(r.left==null && r.right==null){
        list.add(r)
    }
    printAllLeafNodes(r.left, list)
    printAllLeafNodes(r.right, list)
    return list
}