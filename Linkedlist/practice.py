

# implement linkedlist

# insert linkedlist at the start
from Linkedlist.linkedlist import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtStart(s, val):
        if s.head == None:
            s.head= Node(val)
        else:
            newNode = Node(val)

            newNode.next = s.head
            s.head = newNode


    def append(s, data):
        while cur.next