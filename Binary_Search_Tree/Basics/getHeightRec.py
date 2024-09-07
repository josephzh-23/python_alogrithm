from collections import deque

from Binary_Search_Tree.BSTNode import TreeNode
from Binary_Search_Tree.BSTree import BSTree

"""
height of tree = the level from the leaf node

height = max (height of left, height of right) +1

depth of tree = level from the root 



"""



# TC: O (n) the # of nodes in the tree
def getHeightRec(root):
    if root is None:
        return 0

    # This will keep calling until it gets to root is None and then start
    # to pop off that stck
    return 1 + max(getHeightRec(root.left), getHeightRec(root.right))


#And then using thedata here is actually a little bit better than using the
# other approach here And therefore not always better asdf
# and therefore not always

root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
print ("Height of tree is", getHeightRec(root))