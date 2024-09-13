'''


This is a hard problem
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

4 cases
Root on the left side here
The path starts at the root and goes down through the root's left child.
We don't know how long the path is, but it could extend to the bottom of the left subtree.

Root on the right side:
The path starts at the root and goes down through the root's right child. Very similar to the
previous case, but the direction is toward the right.

case 3:
Both the l and r
The path involves both the left and the right child.

case 4 : no child
The path doesn't involve any child. The root itself is the only element of the path with maximum sum.

Steps:
Scenario 1:
Max path sum passes through the node
1. This means we must first find the path sum from the left and the right subtree.
 Once we have both, we decide whether to include their contribution

 meaning: need to process children before node (so post-order here)

Scenario 2:
Does not go thru node,

The maximum path sum here
1.
'''
from typing import Optional

from Binary_tree.BSTNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> float:
        maxPath = -float("inf")

        # post order traversal of subtree rooted at `node`
        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath

            if not node:
                return 0

            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gainFromLeft = max(gainFromSubtree(node.l), 0)

            # add the gain / path sum from right subtree. 0 if negative
            gainFromRight = max(gainFromSubtree(node.r), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)

            # return the max sum for a path starting at the root of subtree
            return max(gainFromLeft + node.val, gainFromRight + node.val)

        gainFromSubtree(root)
        return maxPath
