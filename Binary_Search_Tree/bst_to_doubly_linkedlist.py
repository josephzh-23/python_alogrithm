
'''
A visualization
        12
      7    24
    2   8
  n   n
1st iter        when u get to 2, no more left and right then return
            prev = None -> 2
2nd iter        when u get to 7
            prev = 2
            node = 7    node.left = 2     7 -> 2
            update prev.right = 7       2 -> 7
'''

# much more scalable solution
from Binary_Search_Tree.BSTNode import Node

prev= head = None

def bstToDoublyLinkedList(node):

    global prev, head
    if not node:
        return

    bstToDoublyLinkedList(node.left)

    if not prev:
        head = node
        prev = node
    else:
        node.left = prev
        prev.right = node

        # update the node as well
        prev = node

    bstToDoublyLinkedList(node.right)

