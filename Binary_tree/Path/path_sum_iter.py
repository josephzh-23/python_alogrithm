from Binary_tree.BSTNode import TreeNode


def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False

    de = [ (root, sum - root.val),]
    while de:
        node, curr_sum = de.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            de.append((node.right, curr_sum - node.right.val))
        if node.left:
            de.append((node.left, curr_sum - node.left.val))
    return False