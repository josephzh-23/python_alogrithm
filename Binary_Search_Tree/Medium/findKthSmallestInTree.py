

def findKthSmallestInTree(r, k):

    stack = []
    cur = r

    # need to get all the left children first
    while cur or stack:
        while cur:

            stack.append(cur)
            cur = cur.left

        cur = stack.pop()

        # because we are starting from the bottom this is why
        # like working above
        k-= 1
        if k==0:
            return cur.val
        cur = cur.right