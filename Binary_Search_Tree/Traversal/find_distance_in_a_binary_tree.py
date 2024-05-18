'''


0.
Can be done using the lowest common ancestor here

1. Find distnace between 2 nodes in a tree
'''
def lowestCommonAncestor(r, p, q):
    if not r:
        return None


    if p == q:
        return r


    left = lowestCommonAncestor(r.left, p, q)
    right = lowestCommonAncestor(r.right, p, q)

    # returnt he right
    if left and right:
        return r
