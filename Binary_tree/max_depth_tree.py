

# max depth of tree

# get max depth of

def getMaxDepth(r):

    return max(getHeightRec(r.l), getHeightRec(r.r))

def getHeightRec(root):

    # base case: empty tree has a height of 0
    if root is None:
        return 0

    return 1 + max(getHeightRec(root.left), getHeightRec(root.right))