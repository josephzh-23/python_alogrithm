
# O (m) or O (n) where m and n are # of nodes of each tree
# as explained already
def isSameTree(p, q):

    if not p and not q:
        return True

    if not p or not q or p.val !=q.val:
        return False

    return isSameTree(p.left, q.left) and \
    isSameTree(p.right, q.right)

