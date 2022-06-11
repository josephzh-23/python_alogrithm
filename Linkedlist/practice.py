from Linkedlist.linkedlist import Node


def merge2Linkedlist(l1, l2):
    tail = Node(0)

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1

            # advance both the pointers here
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        # update the tail value here
        tail = tail.next

    if l1:
        tail.next = l1
        l1 = l1.next
