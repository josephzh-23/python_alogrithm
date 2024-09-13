from Binary_tree.BSTNode import TreeNode, insert


def rightSideView(root):
    visibleValues = []
    if not root:
        return visibleValues

    q = []
    q.append(root)

    # q is not empty here
    while q:

        # this is the size of the current level we are looking at
        sizeOfCurLevel = len(q)
        i=0
        for i in range(sizeOfCurLevel):

            # we want to look at the last thing on the current level
            # check to see if this is the last thing on our value,
            print(cur)
            cur = q.pop(0)

            #checking if this is the last value on the current level
            if i == sizeOfCurLevel-1:
                visibleValues.append(cur.val)

            if cur.l:
                q.append(cur.l)

            if cur.r:
                q.append(cur.r)

    return visibleValues


root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)

# funny enough this only prints the left view
list = rightSideView(root)
for i in list:
    print(i)










