
def sameTree(r1, r2):

   #base condition
    if not r1 and not r2:
       return True

    if not r1 or not r2 or r1.val != r2.val:
        return False

    return sameTree(r1, r2)


def getHeight(r):

    if not r:
        return 0
    else:
        1 + getHeight(r.left)


def lowestCommonAncestor(r):

    