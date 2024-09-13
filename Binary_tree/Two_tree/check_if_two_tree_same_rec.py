


# Check if 2 trees are the same


# O( p + q)     the # of nodes in p and q combined here
from Binary_tree.BSTNode import TreeNode


def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return self.isSameTree(p.l, q.l) and \
    self.isSameTree(p.r, q.r)