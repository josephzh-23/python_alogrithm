from Linkedlist.linkedlist import Node
from Linkedlist.printLinkedList import printLinkedlist


def removeDuplicateFromSorted(head):

    # traverse thru this
    cur = head
    while cur.next:
        # if duplicate then do following
        if cur.data== cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
new = Node(12)
new.next = Node(13)
new.next.next = Node(13)
new.next.next.next = Node(13)
new.next.next.next.next = Node(11)

head = removeDuplicateFromSorted(new)
printLinkedlist(head)

