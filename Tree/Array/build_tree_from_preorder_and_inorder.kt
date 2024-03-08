package Tree.Array

import Tree.Basic.TreeNode


// Whatever inorder you have preorder
    // always the 1st elem in the preorder

    // 1. find the preorder root in the inorder []
    // f we know the position of Root,
    // we can recursively split the entire array into 2 subtrees.

    // 2. Everything on the left will be on the lft subtree
    // Everything on right on the right subtree

    // 3. After each iter, the new left preorder[] = the left of
    // previous inorder[]

fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {

    //1. put inorder traversal into the hashmap
    // Hashmap: <number> : <index>

    // inOrder  9 3 15  20  7
    //          0 1  2  3   4   now they are paired
    val inMap: MutableMap<Int, Int> = HashMap()
    for (i in inorder.indices) {
        inMap[inorder[i]] = i
    }

    // Pointers for each part
    return buildTree(preorder, 0, preorder.size - 1, inorder, 0,
            inorder.size - 1, inMap)
}

fun buildTree(preorder: IntArray, preStart: Int, preEnd: Int, inorder: IntArray?, inStart: Int, inEnd: Int, inMap: Map<Int, Int>): TreeNode? {

    // Now this has become invalid
    if (preStart > preEnd || inStart > inEnd) return null


    val root = TreeNode(preorder[preStart])


    val inRootIndex = inMap[root.value]!!

    // This gives the number of indexes left in the case
    val numsLeft = inRootIndex - inStart
    root.left = buildTree(preorder, preStart + 1, preStart + numsLeft, inorder,
            inStart, inRootIndex - 1, inMap)!!
    root.right = buildTree(preorder, preStart + numsLeft + 1, preEnd, inorder,
            inRootIndex + 1, inEnd, inMap)!!
    return root
}

fun main(args: Array<String>) {
    val preorder = intArrayOf(10, 20, 40, 50, 30, 60)
    val inorder = intArrayOf(40, 20, 50, 10, 60, 30)
    val root = buildTree(preorder, inorder)
}
