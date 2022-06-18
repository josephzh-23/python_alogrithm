def invertTree(root):


    invertTree(root.left)
    # swap the left and right
    if root.left and root.right:
        root.left, root.right = root.right, root.left
