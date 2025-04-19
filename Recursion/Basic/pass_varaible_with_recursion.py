

'''
Work on
'''
def height(root):
    if root is None:
        return -1

    # compute the height of left and right subtrees
    lHeight = height(root.left)
    rHeight = height(root.right)
    return max(lHeight, rHeight) + 1

'''
'''