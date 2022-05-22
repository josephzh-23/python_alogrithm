# A function to do inorder tree traversal

'''
Depth first traversal:
    In order traversal, post-order and pre-order are all
depth first traversal, and they all start from the bottom leaves

    1
  2   3
4   5
Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 1 5 3         -> from the bottom here
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
Breadth-First or Level Order Traversal: 1 2 3 4 5
'''

from collections import deque

from Binary_Search_Tree.BSTNode import Node

#left, root and then right
def inOrderRecur(root):
    if root:

        # First recur on left child
        inOrderRecur(root.left)
        print(root.val)
        inOrderRecur(root.right)



# Need 1 cur pter
# keep moving down the left tree
def inOrderIter(root):
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


        # here no more left pointers, all the rest right p
        else:
            '''
                Imagine 7
                       / \
                          9
            '''
            curr = stack.pop()
            print(curr.val, end=' ')
            curr = curr.right








# A function to do postorder tree traversal
# left, right, root
def postOrderRec(root):
    if root:
        postOrderRec(root.left)
        postOrderRec(root.right)

        print(root.val),



# root, left and right
def preOrderRec(root):
    if root:
        print(root.val),

        preOrderRec(root.left)
        preOrderRec(root.right)



# root, left and right, start from the top
# Add the right child first
def PreorderIter(root):
    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while (len(nodeStack) > 0):

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.val, end=" ")

        # All the right nodes at bottom of stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)


# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
# PreorderIter(root)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# inOrderIterative(root)

# and then work