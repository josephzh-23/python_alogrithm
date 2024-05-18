


#
def flattenBSTIntoLinkedlist(root):

    s= []

    s.append(root)

    while s:
        cur = s.pop()

        if cur.right:
            s.append(cur.right)

        elif cur.left:
            s.append(cur.left)



def isTreeBalanced(r):


    if not r:
        return None

    lHeight = height(r.left)
    rHeight = height(r.right)

    if rHeight- lHeight >1:
        return False

    return isTreeBalanced(r.left) and isTreeBalanced(r.right)

def height(root):
    if root is None:
        return 0

    # This will keep calling until it gets to root is None and then start
    # to pop off that stck
    return 1 + max(height(root.left), height(root.right))
