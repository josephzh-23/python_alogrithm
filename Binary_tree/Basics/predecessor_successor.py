'''
Predecessor is the max key value in its left subtree

Sucessor is the min value in the right subtree here



'''
from Binary_tree.BSTNode import TreeNode

# the above works really well for bst
def successor(root: TreeNode) -> TreeNode:
    root = root.r
    while root.l:
        root = root.l
    return root

# the max value in the left subtree here
def predecessor(root: TreeNode) -> TreeNode:
    root = root.l
    while root.r:
        root = root.r
    return root


# and then next here we have the code