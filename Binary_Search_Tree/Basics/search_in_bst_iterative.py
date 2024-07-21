from Binary_Search_Tree.BSTNode import TreeNode


def searchBST(root: TreeNode, val: int) -> TreeNode:
    while root is not None and root.val != val:
        if val < root.val:
            root = root.left
        else:
            root = root.right
    return root



