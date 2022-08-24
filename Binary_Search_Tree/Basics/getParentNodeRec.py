# Python program to print ancestors of given node in
# binary tree

# A Binary Tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getParentNode(r, target):
    if r is None:
        return False

    if r.data == target:
        return True

    # If target is present in either left or right subtree
    # of this node, then print this node

    if getParentNode(r.left, target) or getParentNode(r.right, target):
        print(r.data, end=' ')
        return True

    # Else return False
    return False


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

getParentNode(root, 7)