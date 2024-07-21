'''
We will check the answer how to do this part right here

-
find teh
'''
from typing import Optional

from Binary_Search_Tree.BSTNode import TreeNode


# '''
# How to do this here
#
#
#
def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
) -> Optional[TreeNode]:

        # outside the rnage
    while root and (root.val < low or root.val > high):
        root = root.left if root.val > high else root.right


    if root is None:
        return None
    node = root


    while node.left:

        # left side smaller, go to right
        if node.left.val < low:
            node.left = node.left.right
        # left side bigger go right
        else:
            node = node.left
    node = root
    while node.right:

        
        if node.right.val > high:
            node.right = node.right.left
        else:
            node = node.right
    return root