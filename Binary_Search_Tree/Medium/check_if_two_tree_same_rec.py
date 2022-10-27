


# Check if 2 trees are the same


# O( p + q)     the # of nodes in p and q combined here
from Binary_Search_Tree.BSTNode import Node


def isSameTree(self, p: Node, q: Node) -> bool:
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False

    return self.isSameTree(p.left, q.left) and \
    self.isSameTree(p.right, q.right)