
# the root here
def findMaxInTree(r):

    if (r is None):
        return float('-inf')

    res = r.data
    lres = findMaxInTree(r.left)
    rres = findMaxInTree(r.left)

    #
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res











