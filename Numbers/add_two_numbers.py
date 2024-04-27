from palindrome_linkedlist import ListNode

'''
The tc then becomes O(max(m, n))

What are the 3 cases to look out for here 

1. When 1 list is longer than the other 
2. The other when one list is null, which means an empty list 
3. The sum could have 1 extra of 1 at the end, that's easy to forget


'''
def addTwoNumbers(l1: ListNode, l2: ListNode):
    # these 2 are a must here

    # and then here we have the next thing

    dummyNode = ListNode(0)
    cur = dummyNode
    carry = 0

    while l1 or l2 or carry != 0:
        if l1:
            x = l1.data
        else: x= 0

        if l2:
            y = l2.data
        else: y = 0

        sum = carry + x + y
        carry = sum /10

        cur.next = ListNode(sum % 10)
        cur = cur.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummyNode.next










