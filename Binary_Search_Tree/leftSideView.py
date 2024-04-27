from Binary_Search_Tree.BSTNode import TreeNode, insert


def printLeftSide(root):
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
        print(' number of current level', sizeOfCurLevel)

        for i in range(sizeOfCurLevel):

            # we want to look at the last thing on the current level
            # check to see if this is the last thing on our value,
            # print(cur)
            cur = q.pop(0)

            #checking if this is the first element on each level
            if i == 0:
                visibleValues.append(cur.val)

            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)

    return visibleValues


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# funny enough this only prints the left view
list = printLeftSide(root)
for i in list:
    print(i)










