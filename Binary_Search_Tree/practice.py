
# need the parent node


def getParentNode(r, value):

    # get the node
    par = None
    cur = r
    while cur:

        if r.val == value:
            par = r
            return par

            # not equal case  3 > 2
        elif r.val > value:
            r= r.right
        else:
            r= r.left


