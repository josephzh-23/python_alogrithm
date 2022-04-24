from Linkedlist.linkedlist import Node


# -> is the return annotation
def mergeTwoLists(list1, list2)-> Node:

    #iterative
    if not list1:
        return list1
    if not list2:
        return list2

    # we need to swap node1 and node2 if node1 is bigger
    if list1.data > list2.data:

        # here we swap
        temp = list1
        list1 = list2
        list2 = temp

    res = list1

    while list1 and list2:
    #here you traverse list1 until it's bigger than l2
        while list1 and list1.data <= list2.data:
            temp = list1
            list1 = list1.next

        # point the temp to list2
        temp.next = list2

        # swap to list2 now (since it's the smaller list)
        temp = list1
        list1 = list2
        list2 = temp

    return res



