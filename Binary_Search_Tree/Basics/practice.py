

def isSameTree(p, q):

    if not p and not q:
        return True

    elif not p or not q or p.val!=q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
