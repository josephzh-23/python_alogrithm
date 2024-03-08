package Tree.Array

import Tree.Basic.TreeNode


internal class Solution {
    lateinit var nums: IntArray
    fun helper(left: Int, right: Int): TreeNode? {
        if (left > right) return null

        // always choose left middle node as a root
        val mid = (left + right) / 2

        // preorder traversal: node -> left -> right
        val root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    }

    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        this.nums = nums
        return helper(0, nums.size - 1)
    }
}