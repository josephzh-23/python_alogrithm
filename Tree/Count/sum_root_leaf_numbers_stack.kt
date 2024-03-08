package Tree.Count

import Tree.Basic.TreeNode



import java.util.*

// Preorder iterative traversal here

// Preorder iterative process traversal leetcode

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
    val root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left!!.left = TreeNode(4)
    root.right!!.left = TreeNode(5)
    root.right!!.right = TreeNode(6)
    root.right!!.left!!.left = TreeNode(7)
    root.right!!.left!!.right = TreeNode(8)
    preorderIterative(root)
}
// An iterative process to print preorder traversal of Binary tree
fun preorderIterative(node: TreeNode):Int {

    var rootToLeaf = 0 ; var curNumber = 0
    val root = node

    // We will keep a sum here with a stack here
    // Create an empty stack and push root to it
    val nodeStack = Stack<Pair<TreeNode, Int>>();
    nodeStack.push(Pair(root, 0));

    while (!nodeStack.empty()) {

        // Pop the top item from stack and print it
        val p = nodeStack.pop()
        println("value is "+ p.first.value);

        var root = p.first
        var curNumber = p.second

        // Push right and left children of the popped node to stack
        if (root != null) {
            curNumber = curNumber * 10 + root.value

            // Once we have reached the bottom over here this is what's found
            if(root.left == null && root.right == null){
                rootToLeaf += curNumber
            }else{
                nodeStack.push(Pair(root.right!!, curNumber))
                nodeStack.push(Pair(root.left!!, curNumber))
            }
        }

    }
    return rootToLeaf!!
}