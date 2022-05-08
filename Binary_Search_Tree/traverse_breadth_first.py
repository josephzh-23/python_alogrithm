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
    queue = []

    # Enqueue Root and initialize height, the entire thing is inserted here
    queue.append(root)
    print('total length is ',len(queue))
    while (len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue.pop(0))
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# The 2nd tester
