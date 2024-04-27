from Binary_Search_Tree.bfs_tree_rec import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# still working on this


# we will use this as following very interesting and then
# using this we could have sth more than this


def printCounterClockwise(r):
    # Base Case

    res = []
    if r is None:
        return
    q = []

    q.append(r)

    # how do you know whne you get to the bottom level here?
    while (len(q) > 0):

        print(q[0].val)
        sizeOfCurLevel = len(q)

        # we want to get the first and the last element here
        for i in range(sizeOfCurLevel):
            node = q.pop(0)
            i = 0

            if i == 0 or i == len(sizeOfCurLevel) -1:

                res.append(node.val)
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        # how to know when at last level of a tree?
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printCounterClockwise()