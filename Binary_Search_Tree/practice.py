from Binary_Search_Tree.BSTNode import Node


def insert(root, val):

    '''
     1
   2    3
 1   7
        n
    '''
    # need pter for traversiing

    cur = root
    while cur:
         #trv to right
        if val > cur.val:
            cur = cur.right
        elif val < cur.val:
            cur = cur.left

    # once no more current
    if val > cur.val:
        cur.right = Node(val)
    else:
        cur.left = Node(val)




