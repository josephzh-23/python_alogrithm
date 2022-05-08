

'''
1 -> 2 -> 3
        Using recursive approach, always maintain the last node as the new
    head

# At iteartion 1
- 3.next = 2
   2.next = null

# At iteration 2:

    2.next = 1
    1.next = null
'''
import math



class Solution:
    def reverseList(s, head: ListNode)->ListNode:

        if not head:
            return None

        newHead = head

        # if can keep reversing?
        if head.next:
            newHead = s.reverseList(head.next)

            # Reverse the link between the next node and head
            # this just means the next node of node 3 is pointing at itself
            #Ex:
            #  4 -> 3  before it was 3-> 4
            head.next.next = head

        # If head is the first pter in the list, set the head to null
        head.next = None
        return newHead

# This is very useful







