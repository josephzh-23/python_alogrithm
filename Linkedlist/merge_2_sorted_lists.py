from Linkedlist.linkedlist import Node, LinkedList

'''
    l1 :   1   2  4 
    l2:    1   3  4  5  6
    
    output: dummy -> 1 -> 1 -> 2-> 3-> 4
'''



# this is the answer from before here and that seems to be the probelm here that you don't have any more data
# at the time of shooitng adn that seems to be the problem that you are experiencing right here
# and that seems to be someone else's fault rather than what you were saying here

# -> is the return annotation
def mergeTwoLists(l1, l2) -> Node:
    dummy = Node()
    tail = dummy

    while l1 and l2:
        # and thsi seems to be the answer here for now and then you can move unto the next one
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        # Need to advance the tail pointer
        tail = tail.next

    # if 1 of them is empty condition, and the other is not
    # no need to traverse l1, since tail.next will get everything in l1
    # with tail.next = l1
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next


# Create 2 lists
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.append(5)
listA.append(10)
listA.append(15)

listB.append(2)
listB.append(3)
listB.append(20)

# Call the merge function
listA.head = mergeTwoLists(listA.head, listB.head)

# Display merged list
print("Merged Linked List is:")
listA.print()
listB.print()
# mergeTwoLists()
