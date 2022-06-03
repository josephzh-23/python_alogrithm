def rightSideView(root):
    visibleValues = []
    if root:
        return visibleValues

    q = []
    q.append(root)

    # q is not empty here
    while q:

        # this is the size of the current level we are looking at
        sizeOfCurLevel = len(q)

        for i in sizeOfCurLevel:

            # we want to look at the last thing on the current level
            # check to see if this is the last thing on our value,
            print(cur)
            cur = q.pop()

            #checking if this is the last value on the current level
            if i == sizeOfCurLevel-1:
                visibleValues.append(cur.val)

            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)
    return visibleValues















