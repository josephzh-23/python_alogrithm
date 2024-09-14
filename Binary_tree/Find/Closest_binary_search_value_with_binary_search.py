from Binary_tree.BSTNode import TreeNode

'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.

'''
def closestValue(root, target):
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
