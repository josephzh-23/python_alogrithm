from Binary_Search_Tree.BSTNode import TreeNode


def closestValue(self, root, target):
    min_val = root.val

    while root:
        if abs(root.val - target) < abs(min_val - target):
            min_val = root.val

        # on the right side
        if target > root.val:
            root = root.right
        # if on the left side
        else:
            root = root.left

    return min_val
