from Binary_Search_Tree.BSTNode import Node
from Binary_Search_Tree.BSTree import BSTree

"""
height of tree = the level from the leaf node

height = max (height of left, height of right) +1

depth of tree = level from the root 



"""
def getHeightIterative(root):

    """
    traverse level by level, whenever move down a level
    incremeent height by 1

        Check the # of nodes at each level, stop traversing when
    # of nodes at next level 0

            3. Dequeue all nodes of current level and Enqueue
        all nodes of next level
    """
    if root is None:
        return 0

    # Create a empty queue for level order traversal
    q = []

    # Enqueue Root and Initialize Height
    q.append(root)
    height = 0

    while (True):

        # nodeCount(queue size) indicates number of nodes
        # at current level
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



# Driver program to test above function
# Let us create binary tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Height of tree is", getHeightIterative(root))