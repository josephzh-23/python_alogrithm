# A function to do inorder tree traversal

'''
Depth first traversal:
    In order traversal, post-order and pre-order are all
depth first traversal, and they all start from the bottom leaves

    1
  2   3
4   5
Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3         -> from the bottom here
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
Breadth-First or Level Order Traversal: 1 2 3 4 5

    if you want to trverse left first, add right to stack first
'''

from collections import deque

from Binary_Search_Tree.BSTNode import Node

#left, root and then right
def inOrderRec(root):

    # the base condition if root doesn't exist it will return
    # must have a base condition
    if root:

        # First recur on left child
        inOrderRec(root.left)
        print(root.val)
        inOrderRec(root.right)

'''
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
'''
# need to get down to the left most root first
def inOrderIter(root):

    stack = []

    cur = root

    # we need to get down to the left most node first
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        # then traverse the right
        cur = stack.pop()
        print(cur)
        cur = cur.right






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


'''
Depth first traversal:
    In order traversal, post-order and pre-order are all
depth first traversal, and they all start from the bottom leaves

    1
  2   3
4   5

(b) Preorder (Root, Left, Right) : 1 2 4 5 3
'''
# root, left and right, this is the exact
def PreorderIter(root):
    # Base CAse
    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Driver program to test above function
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
PreorderIter(root)


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