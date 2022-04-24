# A function to do inorder tree traversal

'''
Depth first traversal:
    In order traversal, post-order and pre-order are all
depth first traversal
'''
#root, left and right
from collections import deque

from Binary_Search_Tree.BSTNode import Node


def inOrderTraverseRecur(root):
    if root:

        # First recur on left child
        inOrderTraverseRecur(root.left)
        print(root.val)
        inOrderTraverseRecur(root.right)




def inOrderTraverseItertive(root):

    if root is None:
        return

    # Use a stack
    stack = deque()

    # start from root node
    curr = root

    while stack or curr:

        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left

        # if current node exists, push it into the stack
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child

            '''
                Imagine 7
                       / \
                      4   9
            '''
            curr = stack.pop()
            print(curr.val, end=' ')
            curr = curr.right








# A function to do postorder tree traversal
# left, right, root
def postOrderTraverse(root):
    if root:
        postOrderTraverse(root.left)
        postOrderTraverse(root.right)

        print(root.val),


# A function to do preorder tree traversal
def preOrderTraverse(root):
    if root:
        print(root.val),

        preOrderTraverse(root.left)
        preOrderTraverse(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

inOrderTraverseItertive(root)