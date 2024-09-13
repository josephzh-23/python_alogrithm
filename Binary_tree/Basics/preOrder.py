

# preOrder
#  Preorder (Root, Left, Right) : 1 2 4 5 3
from Binary_tree.BSTNode import TreeNode

def preOrderRec(r):
    if r:
        print(r.val)
        preOrderRec(r.l)
        preOrderRec(r.r)


# let's run the above here
r = TreeNode(1)
r.r = TreeNode(3)
r.r.r = TreeNode(4)
r.r.r.r = TreeNode(5)
r.r.l = TreeNode(2)

preOrderRec(r)





'''

This means root comes before all its children is what it means 
    1
  2   3
4   5
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
'''
# root, left and right, this is the exact opposite of printLevelOrder()
def PreorderIter(root):
    # Base CAse
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()

        if node:
            if node.r:
                # print('right val', node.right.val, end=" ")
                stack.append(node.r)
            if node.l:
                stack.append(node.l)


# Driver program to test above function
root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
# PreorderIter(root)