# tree is done using level order printing
# done using queue
from Binary_Search_Tree.BSTNode import TreeNode


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

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)

printLevelOrderIter(root)