# maybe can use this to find the parent of the root we want
from Binary_Search_Tree.BSTNode import Node


def inOrderRec(root, value):
    # this is how to use a global previous varaible here
    global prev
    # the base condition if root doesn't exist it will return
    # must have a base condition
    if root:

        # First recur on left child
        inOrderRec(root.left, value)
        print(root.val)

        if prev.left and prev.right:
            if prev.left.val == value or prev.right.val == value:
                # prev = root.right
                print('ancestor found', prev.val)

        prev = root
        inOrderRec(root.right, value)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrderRec(root, 4)
