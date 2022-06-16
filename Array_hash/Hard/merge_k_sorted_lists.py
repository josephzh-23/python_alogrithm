

# merge sort here
# use the divide and conquer approach, Michael Muinos

'''
to break this up
[start , mid]   |   [mid + 1, end]
[[1, 4, 5] , [1, 3, 4], [2, 6]]

then break this further into
[[1, 4, 5] , [1, 3, 4],
The base case start = end
'''
from typing import List



# def mergeKLists(lists):
#     if not lists:
#         return None
#     return mergeKLists(lists, 0, len(lists)-1)
from Linkedlist.linkedlist import Node
from Linkedlist.printLinkedList import printLinkedlist

'''
 TC:  O (n * log(k))      mergeKLists( log(k)), k # of recursive calls
'''
def mergeKLists(lists: List[Node], start, end):
    if not lists:
        return
    # if len(lists) == 1:
    if start == end:
        return lists[start]
    mid = (start + end) //2

    left = mergeKLists(lists, start, mid)
    right = mergeKLists(lists, mid + 1, end)
    return mergeTwoLists(left, right)

def mergeTwoLists(l1, l2) -> Node:

    # need the dummy node at the start as well
    dummy = Node()
    tail = dummy

    while l1 and l2:

        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        # Need to advance the tail pointer
        tail = tail.next

    # if 1 of them is empty condition, and the other is not
    # no need to traverse l1, since tail.next will inherit everything in l1
    # with tail.next = l1

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next

    # An array of pointers storing the
    # head nodes of the linked lists

k  = 3

arr = [0 for i in range(k)]
node1 = Node(1)
node1.next = Node(3)
node1.next.next = Node(5)
node1.next.next.next = Node(7)
arr[0] = node1

node2 = Node(2)
node2.next = Node(4)
node2.next.next = Node(6)
node2.next.next.next = Node(8)
arr[1] = node2

node3 = Node(0)
node3.next = Node(9)
node3.next.next = Node(10)
node3.next.next.next = Node(11)
arr[2] = node3

# Merge all lists
head = mergeKLists(arr, 0, len(arr)-1)
# printLinkedlist(head)