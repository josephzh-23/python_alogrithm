
def getHeightIter(root):
    # empty tree has a height of 0
    if root is None:
        return 0

    # create an empty queue and enqueue the root node
    queue = []
    queue.append(root)

    height = 0

    # loop till queue is empty
    while queue:

        # calculate the total number of nodes at the current level
        numOfNodesCurLevel = len(queue)

        # process each node of the current level and enqueue their
        # non-empty left and right child
        while numOfNodesCurLevel > 0:
            front = queue.pop()

            if front.left:
                queue.append(front.left)

            if front.right:
                queue.append(front.right)

            numOfNodesCurLevel = numOfNodesCurLevel - 1

        # increment height by 1 for each level
        height = height + 1

    return height

# testing the basic fxn
myTree = BSTree();

print("Height of tree: ", myTree.getHeight(myTree.root))
