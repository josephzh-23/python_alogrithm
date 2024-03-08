import Tree.Basic.TreeNode

//package Tree
// O(n)
//// Low and high represent the ranges here
internal class Solution33 {
    fun validate(root: TreeNode?, low: Int?, high: Int?): Boolean {
        // Empty trees are valid BSTs.
        if (root == null) {
            return true
        }
        // The current node's value must be between low and high.
        return if (low != null && root.value <= low || high != null && root.value >= high) {
            false
        } else validate(root.right, root.value, high) && validate(root.left, low, root.value)
        // The left and right subtree must also be valid.
    }

    fun isValidBST(root: TreeNode?): Boolean {
        return validate(root, null, null)
    }
}