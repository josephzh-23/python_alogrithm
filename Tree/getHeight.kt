package Tree

import Tree.Basic.TreeNode

/*
TC: O(n)    n : total num of the ndoes in the tree
SC: O(h)    for the call stack : h: the height of the tree here
 */

// Recursive function to calculate the height of a given binary tree
fun height(root: TreeNode?): Int {
    // base case: empty tree has a height of 0
    return if (root == null) {
        0
    } else 1 + Math.max(height(root.left), height(root.right))

    // recur for the left and right subtree and consider maximum depth
}

