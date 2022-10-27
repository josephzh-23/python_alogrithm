# tree is done using level order printing
# done using queue
from Binary_Search_Tree.BSTNode import Node


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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

printLevelOrderIter(root)