import math


def isValidBST(root):

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