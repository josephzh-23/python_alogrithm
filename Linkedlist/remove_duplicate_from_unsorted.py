from Linkedlist.linkedlist import Node
from Linkedlist.printLinkedList import printLinkedlist


def removeDuplicateFromUnsorted(head):

    cur = head
    prev = None

    dupValues = {}
    while cur:
        if cur.data not in dupValues:
            dupValues[cur.data] = 1
            prev = cur
            cur = cur.next
        else:
            prev.next = cur.next
            cur= cur.next

    return head


new = Node(12)
new.next = Node(14)
new.next.next = Node(13)
new.next.next.next = Node(13)
new.next.next.next.next = Node(11)

head = removeDuplicateFromUnsorted(new)
printLinkedlist(head)