

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
Partiiton list pooblem here

Given the head of a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

And this is important as said

Because if you have the code

1 ->

Remember the head here would be [1, 4, 3, 2, 5, 2]
'''
from palindrome_linkedlist import ListNode


def partition(head: ListNode, x):
# these don't really do anything here
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)



    '''
    
    If node.val < x:  the node should be part of the before list. So we move it to before list.
    else: move it to after list 
   
    '''
    p1 = dummy1, p2 = dummy2
    p = head

    while p:
        if p.data >= x:
            p2.next = p
            p2 = p2.next
            p.next = p2
        else:
            p1.next = p



'''
Hvae 2 lists here 
all the less values in left 
all the greater values in right here 

left: 1 -> 2 -> 2 ->  
right: 4 -> 3-> 5  

we want 2 at left end point at the right list start  [4, to 2] here 
'''




