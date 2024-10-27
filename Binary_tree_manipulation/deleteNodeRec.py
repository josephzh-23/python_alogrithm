
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
    There r 3 cases as mentioned before
    1. Node to be deleted is the leaf: Simply remove from the tree.
    2. Node to be deleted has only one child:
        Copy the child to the parent node and delete the child

    3.Node to be deleted has two children:
    
        Find inorder successor of the node.
        , Copy contents of the inorder successor to the node and
       delete the inorder successor.
'''


def deleteNode(root, key):
    # Base Case, return when the deleted node has no left or right children
    if root is None:
        return root

    # this will make sure it keeps going down
    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            inOrderSuccessor = root.right
            root = None
            return inOrderSuccessor

        elif root.right is None:
            inOrderSuccessor = root.left
            root = None
            return inOrderSuccessor

        # Node with two children cases
        # Get the inorder successor
        # (smallest in the right subtree)

        inOrderSuccessor = minValueNode(root.right)

        # Copy the inorder successor's
        # content to this node

        root.key = inOrderSuccessor.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, inOrderSuccessor.key)

    # this is what makes this recursive
    return root


def minValueNode(n):
    cur = n

    # loop down to find the leftmost leaf
    while cur.l is not None:
        cur = cur.l

    return cur