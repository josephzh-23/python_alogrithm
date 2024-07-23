'''
And then here much better here

each value is [0, 25] here

Reset the max

Do a preorder first here and then

1. Here then the code is good
2.
'''
from typing import Optional

from Binary_Search_Tree.BSTNode import TreeNode

finalStr = ''

alphabets = [0] * 26


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallest_string = ""
        self.dfs(root, "")
        print(self.smallest_string)
        return self.smallest_string

    # Helper function to find the lexicographically smallest string
    def dfs(self, root, current_string):
        # If the current node is NULL, return
        if not root:
            return

        # Construct the current string by appending
        # the character corresponding to the node's value
        current_string = chr(root.val + ord('a')) + current_string

        # If the current node is a leaf node
        if not root.left and not root.right:

            # We have reached the end here
            if not self.smallest_string or self.smallest_string > current_string:
                self.smallest_string = current_string

        # Recursively traverse the left subtree
        if root.left:
            self.dfs(root.left, current_string)

        # Recursively traverse the right subtree
        if root.right:
            self.dfs(root.right, current_string)