


#
def flattenBSTIntoLinkedlist(root):

    s= []

    s.append(root)

    while s:
        cur = s.pop()

        if cur.r:
            s.append(cur.r)

        elif cur.l:
            s.append(cur.l)



def isTreeBalanced(r):


    if not r:
        return None

    lHeight = height(r.l)
    rHeight = height(r.r)

    if rHeight- lHeight >1:
        return False

    return isTreeBalanced(r.l) and isTreeBalanced(r.r)

def height(root):
    if root is None:
        return 0

    # This will keep calling until it gets to root is None and then start
    # to pop off that stck
    return 1 + max(height(root.left), height(root.right))
