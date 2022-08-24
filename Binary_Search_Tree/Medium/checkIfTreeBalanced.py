

"""
    The absolute difference between heights of left and
     right subtrees at any node
 should be less than 1.

    5
  1   5
2  3

This will run in O(n) for TC
"""

# function to find height of binary tree
from Binary_Search_Tree.BSTNode import Node


def height(root):

    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# What's time complexity for this?
# O (n^2) in case of full tree

# O(n) space for call stack using recursion
def isBalanced(r):


    if r is None:
        return True

    lHeight = height(r.left)
    rHeight = height(r.right)

    if abs(lHeight - rHeight) > 1:
        return False

    l = isBalanced(r.left)
    r = isBalanced(r.right)

    if not l or not r:
        return False

    return True

# Driver function to test the above function
"""
Constructed binary tree is
            1
        / \
        2     3
    / \ /
    4 5 6 / 7
"""
# to store the height of tree during traversal

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if isBalanced(root):
    print('Tree is balanced')
else:
    print('Tree is not balanced')

