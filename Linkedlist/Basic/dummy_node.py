class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
Using dummy node and then 

Our goal is to turn 1 -> 2 -> 4 into the following

2 -> 4 -> 8         here and that's good 
'''
# using a dummy results in way less code
def addCode(l1):
    dummy = ListNode()
    cur = dummy
    while l1:
        cur.next = ListNode(l1.val + 2)
        cur = cur.next
        l1 = l1.next
    return dummy.next


