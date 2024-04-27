from Binary_Search_Tree.BSTNode import TreeNode
from Binary_Search_Tree.dfS import inOrderRec, preOrderRec, postOrderRec

root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

inOrderRec(root)


#
# inOrderTraverse(root)
# preOrderTraverse(root)
# postOrderTraverse(root)