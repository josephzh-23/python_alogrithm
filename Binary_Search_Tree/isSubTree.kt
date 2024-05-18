package Tree

import Tree.Basic.TreeNode

/*
TC: O(m * n)    for every n node in the tree
check if the tree rooted at node is = to the subroot,
check takes O (m) time M = # of nodes in the subroot

SC: O( m + n)  There will be at most NN recursive call to
Graph.Edges_question.dfs ( or isSubtree).
Now, each of these calls will have MM recursive
calls to isIdentical.
 */
internal class Solution5 {
    fun isSubtree(root: TreeNode?, subRoot: TreeNode?): Boolean {

        // If this node is Empty, then no tree is rooted at this Node
        // Hence, "tree rooted at node" cannot be equal to "tree rooted at subRoot"
        // "tree rooted at subRoot" will always be non-empty, as per constraints
        if (root == null) {
            return false
        }

        // Check if the "tree rooted at root" is identical to "tree roooted at subRoot"
        return if (isIdentical(root, subRoot)) {
            true
        } else isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)

        // If not, check for "tree rooted at root.left" and "tree rooted at root.right"
        // If either of them returns true, return true
    }

    private fun isIdentical(node1: TreeNode?, node2: TreeNode?): Boolean {

        // If any of the nodes is null, then both must be null
        return if (node1 == null || node2 == null) {
            node1 == null && node2 == null
        } else node1.value === node2.value && isIdentical(node1.left, node2.left) && isIdentical(node1.right, node2.right)

        // If both nodes are non-empty, then they are identical only if
        // 1. Their values are equal
        // 2. Their left subtrees are identical
        // 3. Their right subtrees are identical
    }
}