import collections

from Binary_Search_Tree.BSTNode import Node

"""
using queue:
    TC: O(n)
    SC: O(n)
"""
def printLevelOrder(root):

    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    q = []

    # Enqueue Root and initialize height, the entire thing is inserted here
    q.append(root)
    print('total length is ',len(q))
    while q:

        # node count: # of nodes at cur level
        count = len(q)
        while count> 0:

            node = q.pop(0)
            print(node.val)


            # Enqueue left child
            if node.left:
                q.append(node.left)
            # Enqueue right child
            if node.right:
                q.append(node.right)

            count -= 1

# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#
# print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
#
# # The 2nd tester
