

# TC: O (nlogn) here only half of nodes traversed
def lowestCommonAncestor(r, p, q):

    # both of them are on the left side
    if p.val < r.val and q.val < r.val:
        return lowestCommonAncestor(r.left, p, q)

    # both of them are on the right side
    elif p.val > r.val and q.val > r.val:
        return lowestCommonAncestor(r.right, p, q)

    #       6
    #    2    8
    else:
        return r
  

