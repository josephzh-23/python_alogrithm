



# Ok here
from Binary_Search_Tree.BSTNode import TreeNode


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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('height of the tree is %d' %maxDepth(root))