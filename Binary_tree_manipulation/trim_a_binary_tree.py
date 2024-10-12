'''
We will check the answer how to do this part right here

-
find teh
'''
from typing import Optional

from Binary_tree.BSTNode import TreeNode


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
        root = root.l if root.val > high else root.r


    if root is None:
        return None
    node = root


    while node.l:

        # left side smaller, go to right
        if node.l.val < low:
            node.l = node.l.r
        # left side bigger go right
        else:
            node = node.l
    node = root
    while node.r:

        
        if node.r.val > high:
            node.r = node.r.l
        else:
            node = node.r
    return root