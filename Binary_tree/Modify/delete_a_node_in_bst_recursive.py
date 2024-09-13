'''
And then here we have the code

'''
from Binary_tree.BSTNode import TreeNode


def deleteNode(root: TreeNode, val: int) -> TreeNode:

    cur = root
    # a leaf node you can delete right away
    # case 2:
    # delete a node that only has 1 child, simply do the swapping here with the current node, and then delete the right child here
    # which is a leaf node here

    '''
    case 2 when only 1 child delete either left or right as said 

    '''
    if cur.l:
        cur = cur.l
        cur.l = None
    if cur.r:
        cur = cur.r
        cur.r = None

    # if the value is in the left, then go left
    if val < root.val:
        root.l = deleteNode(root.l, val)

    # if value in the right, then go right here
    elif val > root.val:
        root.r = deleteNode(root.r, val)


    # else found it then delete this here
    # Node with only one child or no child
    if root.l is None:
        return root.r
    elif root.r is None:
        return root.l


    # then you just go ahead and then delete here
    # and then you can just keep going here with the current value

    # then you just delete from this value here the one value only here
    root.key = inorderSucessor(root.r)

    root.r = deleteNode(root.r, root.key)

def inorderSucessor(root):
    minv = root.key
    while root.left:
        minv = root.left.key
        root = root.left
    return minv
