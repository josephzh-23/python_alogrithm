
'''

Same as getting the height of the binary tree here
'''
from Binary_tree.BSTNode import TreeNode

r = TreeNode(3)
r.r = TreeNode(1)
r.r.l = TreeNode(0)
r.r.r = TreeNode(8)

r.l = TreeNode(5)
r.l.l = TreeNode(6)
r.l.r = TreeNode(2)
r.l.r.l = TreeNode(7)
r.l.r.r = TreeNode(4)



def getMaxDepth(r):

    return max(getHeightRec(r.l), getHeightRec(r.r))

def getHeightRec(root):

    # base case: empty tree has a height of 0
    if root is None:
        return 0

    return 1 + max(getHeightRec(root.l), getHeightRec(root.r))

print(getMaxDepth(r))