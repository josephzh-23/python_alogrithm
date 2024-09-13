from Binary_tree.BSTNode import TreeNode
from Binary_tree.dfS import inOrderRec, preOrderRec, postOrderRec

root = TreeNode(1)
root.l = TreeNode(2)
root.r= TreeNode(3)

root.l.l = TreeNode(4)
root.l.r = TreeNode(5)

inOrderRec(root)


#
# inOrderTraverse(root)
# preOrderTraverse(root)
# postOrderTraverse(root)