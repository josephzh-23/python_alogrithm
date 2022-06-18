import collections

from Binary_Search_Tree.BSTNode import Node

"""
Ex:
    1
  2   3
4  5  6  7

the level order would be: 1 2 3 4 5 6 7
using queue:
    TC: O(n)
    SC: O(n)
"""


def printLevelOrderRec(r):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)


def printLevelOrderIter(r):
    # Base Case
    if r is None:
        return
    q = []

    q.append(r)

    while (len(q) > 0):

        print(q[0].val)
        node = q.pop(0)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)


# Driver Program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print("Level Order Traversal of binary tree is -")
# printLevelOrder(root)
# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# The 2nd tester


