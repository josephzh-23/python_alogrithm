package Tree

import Tree.Basic.TreeNode
import Tree.Basic.preorder


// A fxn that constructs a bst tree from a node tree

fun sortedArrayToBST(arr: IntArray, start: Int, end:Int): TreeNode?{

    if(start > end){
        return null
    }

    // get the middle element and then make it root here
    // this is based on what's passed in here
    val mid = (start + end)/2
    val node = TreeNode(arr[mid])

    node.left = sortedArrayToBST(arr, start, mid-1)
    node.right = sortedArrayToBST(arr, mid + 1, end)

    return node
}



fun main(args: Array<String>) {


    val arr = intArrayOf(1, 2, 3, 4, 5, 6, 7)
    val n = arr.size

    val root = sortedArrayToBST(arr, 0, n-1)
    preorder(root)
}