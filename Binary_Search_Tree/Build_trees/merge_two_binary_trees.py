from Binary_Search_Tree.BFS_rec import Node, root
from Binary_Search_Tree.BSTNode import TreeNode


def mergeTree(t1: TreeNode, t2: TreeNode):
    # the base condition if root doesn't exist it will return
    # must have a base condition
    if not t1 and not t2:
        return None

    v1 = t1.val if t1 else 0
    v2 = t2.val if t2 else 0
    r = TreeNode(v1 + v2)
    r.left = mergeTree(t1.left if t1 else None, t2.left if t2 else None)
    r.right = mergeTree(t1.right if t1 else None, t2.right if t2 else None)
    return root