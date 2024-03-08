package Tree.Array

import Tree.Basic.TreeNode

/*
"""
   Input:  String_Array {1, 2, 3}  the middle one will be at the top
Output: A Balanced BST
     2
   /  \
  1    3

Input: String_Array {1, 2, 3, 4}
Output: A Balanced BST
      3
    /  \
   2    4
 /
1
"""

Time complexity: O(N)O(N) since we visit each node exactly once.

Space complexity: O(\log N)O(logN).

The recursion stack requires O(\log N)O(logN) space because the tree
is height-balanced. Note that the O(N)O(N) space used to store the output does not count as auxiliary space, so it is not included in the space complexity.

 */
internal class Solution14 {
    lateinit var nums: IntArray
    fun helper(left: Int, right: Int): TreeNode? {
        if (left > right) return null

        // always choose left middle node as a root
        val p = (left + right) / 2

        // preorder traversal: node -> left -> right
        val root = TreeNode(nums[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root
    }

    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        this.nums = nums
        return helper(0, nums.size - 1)
    }
}