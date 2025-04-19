'''


To make a binary tree algorithm run in O(h) time complexity — where h is the height of the tree — the key is to avoid visiting all nodes and instead limit traversal only along a single path from root to leaf, or a similarly narrow path (like root-to-root between two nodes).

 Traverses only a path from the root to a specific node or between two nodes (e.g., Lowest Common Ancestor).

 Using dfs here

 dfs here ->
'''
from cmath import inf
from typing import Optional

from Binary_tree.BSTNode import TreeNode

'''
This is based on the problem closest value closest value up above here 
- And this runs in O(h) as said 
'''


class Solution:
    def closest_value(self, root: TreeNode, target: float) -> int:
        # Initialize the closest_value with the root's value
        closest_value = root.val

        # Initialize the minimum difference found
        minimum_difference = float('inf')

        # Iterate over the nodes of the binary search tree
        while root:
            # Calculate the current difference between node's value and the target
            current_difference = abs(root.val - target)

            # If the current difference is smaller or equal but with a lesser value, update the closest_value
            if current_difference < minimum_difference or (
                    current_difference == minimum_difference and root.val < closest_value):
                minimum_difference = current_difference
                closest_value = root.val

            # Move left if the target is smaller than the current node's value
            if root.val > target:
                root = root.left
            # Otherwise, move right
            else:
                root = root.right

        # Once we find the closest value, return it
        return closest_value


















