'''


Gett the max height of the tree leetcode

And the problem here as said
'''
from Binary_tree.BSTNode import TreeNode


def printLevelOrderIter(r):
    # Base Case
    if r is None:
        return
    q = []

    q.append(r)
    level = 0
    while (len(q) > 0):
        size = len(q)
        level +=1
        while size >0:
            # print(q[0].val)
            node = q.pop(0)

            if node.l:
                q.append(node.l)

            if node.r:
                q.append(node.r)
            size-=1

    print(level)
r = TreeNode(1)
r.l = TreeNode(2)
r.r = TreeNode(3)
r.l.l = TreeNode(4)
r.r.r = TreeNode(5)

# this is the answer here and that's it we need to do here

printLevelOrderIter(r)