



# Ok here
from Binary_tree.BSTNode import TreeNode


# can also do this wile using traversal
def maxDepth(node):

    if node is None:
        return 0

    else:
        lDepth = maxDepth(node.l)
        print(lDepth)
        rDepth = maxDepth(node.r)

        if lDepth > rDepth:
            return lDepth + 1

        else:
            return rDepth + 1

root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)

print('height of the tree is %d' %maxDepth(root))