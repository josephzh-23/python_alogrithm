from Binary_tree.Basics.BFS_rec import root
from Binary_tree.BSTNode import TreeNode


def mergeTree(t1: TreeNode, t2: TreeNode):
    # the base condition if root doesn't exist it will return
    # must have a base condition
    if not t1 and not t2:
        return None

    v1 = t1.val if t1 else 0
    v2 = t2.val if t2 else 0
    r = TreeNode(v1 + v2)
    r.l = mergeTree(t1.l if t1 else None, t2.l if t2 else None)
    r.r = mergeTree(t1.r if t1 else None, t2.r if t2 else None)
    return root