



# Ok here
from Binary_Search_Tree.BSTNode import Node


# can also do this wile using traversal
def maxDepth(node):

    if node is None:
        return 0

    else:
        lDepth = maxDepth(node.left)
        print(lDepth)
        rDepth = maxDepth(node.right)

        if lDepth > rDepth:
            return lDepth + 1

        else:
            return rDepth + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('height of the tree is %d' %maxDepth(root))