'''

All the crud oeprations are in order of O (1) in doubly linkedlist


Can traverse in both directions here,both backward and forward here
2.Inserting a new node is quicker.

3. It's easier to reverse a doubly linked list.

Applications of doubly linkedlist here

Check the following for the implementation here
'''
# Node of a doubly linked list
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # reference to next node in DLL
        self.next = next
        # reference to previous node in DLL
        self.prev = prev
        self.data = data

# Function to insert a node at the beginning of a doubly linked list
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Function to traverse all the elements in the linked list here
def traverse(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


# to insert after a given node here

'''
1. Set next of new node to point to the next of given node 
2. Set the "previous" pointer of the new node to point to the given node.

3. If the next node of the given node
 is not None, update the "previous" pointer of that node to point to the new node.
So this completes the linking 

'''


# Function to insert a node after a given node in a doubly linked list
def insert_after_node(node, data):
    if node is None:
        print("Error: The given node is None")
        return
    new_node = Node(data)
    new_node.prev = node
    new_node.next = node.next

    if node.next:
        node.next.prev = new_node

    node.next = new_node


