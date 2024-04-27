
# This is the leet code accepted answer
# Reverse a singly linkedlist, need 3 pointer here
def reverseSinglyLinkedList(head):

    if not head:
        return None

    cur = head
    prev = None

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

