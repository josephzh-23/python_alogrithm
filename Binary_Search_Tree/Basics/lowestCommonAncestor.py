

# TC: O (nlogn) here only half of nodes traversed
def lowestCommonAncestor(r, p, q):

    if p.val < r.val and q.val < r.val:
        return lowestCommonAncestor(r.left, p, q)
    elif p.val > r.val and q.val > r.val:
        return lowestCommonAncestor(r.right, p, q)
    else:
        return r
