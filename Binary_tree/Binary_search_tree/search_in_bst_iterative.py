from Binary_tree.BSTNode import TreeNode


def searchBST(root: TreeNode, val: int) -> TreeNode:
    while root is not None and root.val != val:
        if val < root.val:
            root = root.l
        else:
            root = root.r
    return root



