'''
The backtracking solution here

Backtracking solution is much easier here


The dfs function first checks if the current node is None. If it is, then it returns.
Otherwise, it appends the current node value to the path.

    If the current node is a leaf node (i.e., it has no left or right child nodes)
and its value is equal to the target sum, then the current path is added to the result list.

    Otherwise, the dfs function calls itself recursively on the left and right child nodes,
subtracting the current node value from the target sum.
When the recursive calls have completed, the current node is popped from the path.


'''
from typing import List, Optional

from Binary_tree.BSTNode import TreeNode


def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    result = []
    path = []
    self.dfs(root, targetSum, path, result)
    return result


def dfs(self, node, target, path, result):
    if not node:
        return
    path.append(node.val)
    if not node.left and not node.right and node.val == target:
        result.append(path[:])
    self.dfs(node.left, target - node.val, path, result)
    self.dfs(node.right, target - node.val, path, result)
    path.pop()