from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.BSTree import BSTree

"""
height of tree = the level from the leaf node

height = max (height of left, height of right) +1

depth of tree = level from the root 



"""
def getHeightIterative(root):


    if root is None:
        return 0

    q = []

    q.append(root)
    height = 0

    while (True):


        nodeCount = len(q)
        if nodeCount == 0:
            return height

        height += 1

        # Dequeue all nodes of current level and Enqueue
        # all nodes of next level
        while (nodeCount > 0):
            node = q[0]
            print('the node is', node.val)

            # here we dequeue each root node and check if
            # it has any sub children
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

            nodeCount -= 1





# testing the basic fxn
myTree = BSTree();

print("Height of tree: ", myTree.getHeight(myTree.root))


def getHeightRec(root):
    if root is None:
        return 0

    # This will keep calling until it gets to root is None and then start
    # to pop off that stck
    return 1 + max(getHeightRec(root.left), getHeightRec(root.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Height of tree is", getHeightIterative(root))
print ("Height of tree is", getHeightRec(root))