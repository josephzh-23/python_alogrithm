'''


To work on this here you need to know to

1. Each node's left pointer should reference its predecessor in the list.
2. Each node's right pointer should reference its successor in the list.

3. The list should be circular, with the last element pointing to the first as its successor, and the first element pointing to the last as its predecessor.
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':


        # Helper function to perform the in-order traversal of the tree.
        def in_order_traverse(node):
            # Base case: if the node is None, return to the previous call.
            if node is None:
                return

            # Recursive case: traverse the left subtree.
            in_order_traverse(node.left)

            # Process the current node.
            nonlocal previous, head
            if previous:

                # Link the previous node with the current node from the left.
                previous.right = node
                # Link the current node with the previous node from the right.
                node.left = previous

            else:
                # If this node is the leftmost node, it will be the head of the doubly linked list.
                head = node

            '''
            Mark the current node as the previous one before the next call.
            so the previous is now updated here 
            '''
            previous = node

            # Recursive case: traverse the right subtree.
            in_order_traverse(node.right)

        # If the input tree is empty, return None.
        if root is None:
            return None

        # Initialize the head and previous pointer used during the in-order traversal.
        head = previous = None
        # Perform the in-order traversal to transform the tree to a doubly linked list.
        in_order_traverse(root)


        # Connect the last node visited (previous) with the head of the list to make it circular.
        previous.right = head
        head.left = previous

        # Return the head of the doubly linked list.
        return head