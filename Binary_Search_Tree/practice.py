from Binary_Search_Tree.BSTNode import Node


def printLevelOrderIter(r):

    if r is None:
        return

    q = []

    # then add to this
    q.append(r)
    while (len(q) > 0):
        print(q[0].val)
        node = q.pop(0)

        # check left
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# to test this

def preOrder()
