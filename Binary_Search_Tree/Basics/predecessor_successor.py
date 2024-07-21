'''
Predecessor is the max key value in its left subtree

Sucessor is the min value in the right subtree here



'''
from Binary_Search_Tree.BSTNode import TreeNode

# the above works really well for bst
def successor(root: TreeNode) -> TreeNode:
    root = root.right
    while root.left:
        root = root.left
    return root

# the max value in the left subtree here
def predecessor(root: TreeNode) -> TreeNode:
    root = root.left
    while root.right:
        root = root.right
    return root


# and then next here we have the code