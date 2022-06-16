from Linkedlist.linkedlist import Node
from Linkedlist.printLinkedList import printLinkedlist


def removeDuplicateFromSorted(head):

    # traverse thru this
    cur = head
    while cur.next:
        # duplicate
        if cur.data == cur.next.data:
            cur = cur.next.next
        #duplicate
        else:
            cur = cur.next

    return head
new = Node(12)
new.next = Node(13)
new.next = Node(13)
new.next = Node(13)

removeDuplicateFromSorted(new)
printLinkedlist(new)

