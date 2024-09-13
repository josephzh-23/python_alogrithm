
"""
There r 3 cases to examine

   - traverse down the tree
1. A case with no child node, the leaf node, set it to none


2. A case where deleting node has 2 children node
    1) get mininmum key with in that subtree, same as finding inOrder Successor

    2) recursively delete the successor. Note that the successor
    will have at most one child (right child)

    3) copy value of the successor to the current node

3. A case where the deleting node has  1 child node
     - if the node to be deleted is not a root node, set its parent to it child

"""

# Helper function to find minimum value node in the subtree rooted at `curr`
def findMin(curr):
    while curr.left:
        curr = curr.left
    return curr

# Function to delete a node from a BST

"""
Need a parent pter and cur pter 
"""
def deleteNode(root, key):

    parent = None

    curr = root

    # search key in the BST and set its parent pointer
    while curr and curr.data != key:

        # update the parent to the current node
        parent = curr

        # if the given key is less than the current node, go to the left subtree;
        # otherwise, go to the right subtree
        if key < curr.data:
            curr = curr.l
        else:
            curr = curr.r

    # return if the key is not found in the tree
    if curr is None:
        return root

    # Case 1: node to be deleted has no children, i.e., it is a leaf node
    if not curr.l and not curr.r:

        # if the node to be deleted is not a root node, then check its
        # left or right child, and set it to none
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None

        # if the tree has only a root node, set it to None
        else:
            root = None

    # Case 2: node to be deleted has two children
    elif curr.l and curr.r:

        # find its inorder successor node
        successor = findMin(curr.r)

        # store successor value
        val = successor.data

        # recursively delete the successor. Note that the successor
        # will have at most one child (right child)
        deleteNode(root, successor.data)

        # copy value of the successor to the current node
        curr.data = val

    # Case 3: node to be deleted has only one child
    else:

        # choose a child node
        if curr.l:
            child = curr.l
        else:
            child = curr.r

        # if the node to be deleted is not a root node, set its parent
        # to its child
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child

        # if the node to be deleted is a root node, then set the root to the child
        else:
            root = child

    return root