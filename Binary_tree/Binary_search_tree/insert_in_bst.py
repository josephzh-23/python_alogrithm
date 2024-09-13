# Utility function to insert nodes into the BST
from Binary_tree.BSTNode import TreeNode


def insert(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root