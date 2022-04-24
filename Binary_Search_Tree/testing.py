from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.traversal_depth_first import inOrderTraverseRecur, preOrderTraverse, postOrderTraverse

root = Node(1)
root.left = Node(2)
root.right= Node(3)

root.left.left = Node(4)
root.left.right = Node(5)




#
# inOrderTraverse(root)
# preOrderTraverse(root)
# postOrderTraverse(root)