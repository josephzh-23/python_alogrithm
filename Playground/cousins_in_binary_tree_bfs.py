'''


Gett the max height of the tree leetcode

And the problem here as said

We keep doing this and then
'''
from Binary_tree.BSTNode import TreeNode


def printLevelOrderIter(r, x, y):

    res = []
    # Base Case
    if r is None:
        return
    q = [r]

    level = 0
    while (len(q) > 0):
        size = len(q)
        level +=1
        while size >0:
            node = q.pop(0)


            print('node value',node.val)

            if node.l:
                q.append(node.l)
                if node.l.val == x:
                    res.append((node, level))
            if node.r:
                q.append(node.r)
                if node.r.val == y:
                    res.append((node, level))


            size-=1
    if len(res) < 2:
        return False
    t1, t2 = res
    return t1[0] != t2[0] and t1[1] == t2[1]
r = TreeNode(1)
r.l = TreeNode(2)
r.r = TreeNode(3)
r.l.l = TreeNode(4)
r.r.r = TreeNode(5)

# this is the answer here and that's it we need to do here

print(printLevelOrderIter(r, 3, 5))