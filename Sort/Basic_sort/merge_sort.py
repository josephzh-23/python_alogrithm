'''



In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together.
4-> 2 -> 1-> 3

and then becomes

4-> 2 -> null
1-> 3 here

Then into
4-> null
2-> null
1-> null
3-> null
right.next = null and then the next thing here is what you want after the

first one

Using the sort list here we would have sth that's simliar to what you want here


'''
from palindrome_linkedlist import ListNode

class Solution:
    def sortList(s, head:ListNode):

        if not head or not head.next:
            return None

        # split the list into 2 halves first here
        left = head
        right = s.getMid(head)

        ''' 
        Split the list hereand this really makes sense here and then 
        we can call sort list next then 
        '''
        tmp = right.next
        right.next = None
        right = tmp

        left = s.sortList(left)
        right = s.sortList(right)
        return s.merge(left, right)

    def getMid(s, head):
        slow, fast = head, head.next

        '''
        
        Shift the slow pointer by one 
        and then fast by 2 here and then by the time that the fast pointer will be out of 
        bound, slow pointer will be at the net 
        '''
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(s, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1= list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next