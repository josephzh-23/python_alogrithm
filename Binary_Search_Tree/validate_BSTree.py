import math

from Binary_Search_Tree.BSTNode import Node


# This is iterative approach
def isValidBSTIter(root):

    # need to traverse this using breadth first traversal here
    s= []
    leftChildVal = -math.inf

    while s or root:

        # Get all the left children in there first (last one to come out)
        while root:
            s.append(root)
            root = root.left

        root = s.pop()
        if root.val <= leftChildVal:
            return False

        leftChildVal = root.val
        root = root.right       #traverse the right children


    return True


# Using the recurisve approach
"""
    Video by Kevin Naughton
"""

def isValidBST(root):
    # these 2 values are none at the start but then will change
    #
    return validate(root, None, None)


def validate(root, max, min):

    if root is None:
        return True
    elif (max and root.val >= max) or (min and root.val <= min):
        return False
    else:
        # Here then we validate the left and the right subtree
        return validate(root.left, root.val, min) and \
               validate(root.right, max, root.val )

# ensure left and right exists

#testing this
root = Node(4)
root.left = Node(3)
root.right = Node(5)
print(isValidBST(root))