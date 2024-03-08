package Tree.Basic

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
fun preorderIterative(node: TreeNode) {
    val root = node
    // Base Case
    if (node == null) {
        return;
    }

    // Create an empty stack and push root to it
    val nodeStack = Stack<TreeNode>();
    nodeStack.push(root);

    /* Pop all items one by one. Do following for every popped item
     a) print it
     b) push its right child
     c) push its left child
     Note that right child is pushed first so that left is processed first */
    while (!nodeStack.empty()) {

        // Pop the top item from stack and print it
        val mynode = nodeStack.peek();
        println("value is "+ mynode.value);
        nodeStack.pop();

        // Push right and left children of the popped node to stack
        if (mynode.right != null) {
            nodeStack.push(mynode.right);
        }
        if (mynode.left != null) {
            nodeStack.push(mynode.left);
        }
    }
}