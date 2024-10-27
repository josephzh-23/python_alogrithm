

'''
Use dfs with a tree here and then next


'''
from Binary_tree.BSTNode import TreeNode


def getChildrenHeight(r):
    # Base Case
    if r is None:
        return
    depth = {r: 0}
    q = [r]

    while (len(q) > 0):

        print(q[0].val)
        node = q.pop(0)
        if node.l:
            depth[node.l]= depth[node] +1
            q.append(node.l)

        if node.r:
            depth[node.r]= depth[node] +1
            q.append(node.r)
    print(depth)

root = TreeNode(3)
root.l = TreeNode(5)
root.r = TreeNode(1)

root.l.l = TreeNode(6)
root.l.r = TreeNode(2)
root.r.l = TreeNode(0)
root.r.r = TreeNode(8)

getChildrenHeight(root)