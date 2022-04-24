'''

'''

# Driver program to test the above functions
# Let us create the following BST
#       50
#    /     \
#   30     70
#  / \     / \
# 20 40  60   80
from Binary_Search_Tree.BSTNode import Node, insert
from Binary_Search_Tree.traversal_depth_first import inOrderTraverseRecur

node = Node(50)
node =insert(node, 30)
node = insert(node, 70)
node = insert(node, 20)
node = insert(node, 40)


inOrderTraverseRecur(node)
