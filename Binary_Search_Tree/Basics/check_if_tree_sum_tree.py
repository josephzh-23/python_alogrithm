

def isSum(r):

    # and then what here?

    # and you can see that we have

    if not r:
        return 0

    # and this is for starter here and we are getting even better here
    return sum(r.left) + r.data + sum(r.right)


def isSumTree(r):
    # and then here a bit more
    # this is problem 1 here
    # If node is None or it's a leaf

    # the sum tree here might not be the worst

    # node then return true
    # then this has reached the bottom here and we are done
    if (r == None or
            (r.left is None and
             r.right is None)):
        return 1
    # we have to take care of the one aat the bottom here
#these 2 are it here
    ls = sum(r.left)
    rs = sum(r.right)

    if r.data== ls + rs and isSumTree(r.left) and isSumTree(r.right):
        return 1

    return 0