


'''
    1
  2   3
4  5   6

The above will then print '4 5 2 6 3 1' so a bit more different

'''
# the root comes in last
# A function to do postorder tree traversal
# left, right, root
from Binary_Search_Tree.BSTNode import TreeNode


def postOrderRec(root):
    if root:
        postOrderRec(root.l)
        postOrderRec(root.r)

        print(root.val),


# and then work
# and this can be done using 2 stacks here
def postOrderIterative(root):
    if root is None:
        return

        # Create two stacks
    s1 = []
    s2 = []

    # Push root to first stack
    s1.append(root)

    # Run while first stack is not empty
    while s1:

        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)

        # Push left and right children of
        # removed item to s1
        if node.l:
            s1.append(node.l)
        if node.r:
            s1.append(node.r)

        # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.val, end=" ")


# inOrderIter(root)

root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.r.l = TreeNode(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

# inOrderIterative(root)



# Driver program to test above function
root = TreeNode(1)
root.l = TreeNode(2)
root.r = TreeNode(3)
root.l.l = TreeNode(4)
root.l.r = TreeNode(5)
root.r.l = TreeNode(6)
root.r.r = TreeNode(7)
postOrderIterative(root)