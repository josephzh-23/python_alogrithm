from Binary_tree.BSTNode import TreeNode


def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False

    sum -= root.val
    if not root.l and not root.r:  # if reach a leaf
        return sum == 0
    return self.hasPathSum(root.l, sum) or self.hasPathSum(
        root.r, sum
    )