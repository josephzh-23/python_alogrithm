'''
And then here we have the code

'''
from Binary_Search_Tree.BSTNode import TreeNode


def deleteNode(root: TreeNode, val: int) -> TreeNode:

    cur = root
    # a leaf node you can delete right away
    # case 2:
    # delete a node that only has 1 child, simply do the swapping here with the current node, and then delete the right child here
    # which is a leaf node here

    '''
    case 2 when only 1 child delete either left or right as said 

    '''
    if cur.left:
        cur = cur.left
        cur.left = None
    if cur.right:
        cur = cur.right
        cur.right = None

    # if the value is in the left, then go left
    if val < root.val:
        root.left = deleteNode(root.left, val)

    # if value in the right, then go right here
    elif val > root.val:
        root.right = deleteNode(root.right, val)


    # else found it then delete this here
    # Node with only one child or no child
    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left


    # then you just go ahead and then delete here
    # and then you can just keep going here with the current value

    # then you just delete from this value here the one value only here
    root.key = inorderSucessor(root.right)

    root.right = deleteNode(root.right, root.key)

def inorderSucessor(root):
    minv = root.key
    while root.left:
        minv = root.left.key
        root = root.left
    return minv
