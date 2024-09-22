from Binary_tree.BSTNode import TreeNode

r = TreeNode(1)
r.l = TreeNode(2)
r.r = TreeNode(3)
r.r.r = TreeNode(6)
r.r.l = TreeNode(5)


def printAllRootNodes(r, list):

    if r is None:
        return list

    # reach a node here
    if r.l is None and r.r is None:
        list.append(r)

    printAllRootNodes(r.l, list)
    printAllRootNodes(r.r, list)
    return list

for i in printAllRootNodes(r, []):
    print(i.val)