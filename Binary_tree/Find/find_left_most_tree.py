'''
Use dfs method for this
'''
from typing import Optional

from Binary_tree.BSTNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = -1
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        return self.bottomLeftValue

    def dfs(self, current: TreeNode, depth: int):
        if not current:
            return

        if depth > self.maxDepth:  # If true, we discovered a new level
            self.maxDepth = depth
            self.bottomLeftValue = current.val

        self.dfs(current.l, depth + 1)
        self.dfs(current.r, depth + 1)
        return
