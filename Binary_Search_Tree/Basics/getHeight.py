from collections import deque

from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.BSTree import BSTree

"""
height of tree = the level from the leaf node

height = max (height of left, height of right) +1

depth of tree = level from the root 



"""


def height(root):
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


# TC: O (n) the # of nodes in the tree
def getHeightRec(root):
    if root is None:
        return 0

    # This will keep calling until it gets to root is None and then start
    # to pop off that stck
    return 1 + max(getHeightRec(root.left), getHeightRec(root.right))


#And then using thedata here is actually a little bit better than using the
# other approach here And therefore not always better asdf
# and therefore not always

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Height of tree is", getHeightIterative(root))
print ("Height of tree is", getHeightRec(root))