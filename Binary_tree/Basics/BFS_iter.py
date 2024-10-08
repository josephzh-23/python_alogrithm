# tree is done using level order printing
# done using queue
from Binary_tree.BSTNode import TreeNode


'''

'''
#level order traversal 
def printLevelOrderIter(r):
    # Base Case
    if r is None:
        return
    q = []

    q.append(r)

    while (len(q) > 0):

        print(q[0].val)
        node = q.pop(0)

        if node.l:
            q.append(node.l)

        if node.r:
            q.append(node.r)

root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
root.l.l.l = TreeNode(7)

printLevelOrderIter(root)