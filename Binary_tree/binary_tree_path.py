'''



'''
from Binary_tree.BSTNode import TreeNode


def binaryTreePath(r):
    res = str(r.val)

    # and have a strating point

    def dfs(r, res):
        if r is None:
            return res

        elif r.l:
            res+= '->'
            res+= str(r.l)
            dfs(r.l, res)

        elif r.r:
            res += str('->')
            res += r.r
            dfs(r.r, res)

    value = dfs(r, res)

    print(value)


r = TreeNode(1)
r.l = TreeNode(2)
r.r = TreeNode(3)
r.l.l = TreeNode(4)

binaryTreePath(r)