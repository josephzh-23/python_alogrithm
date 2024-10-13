'''


List A: 1 -> 2 -> 3 -> 4 -> 5
List B: 9 -> 4 -> 5


pa points to headA (1)
pb points to headB (9)

basically they will both keep moving until either one reaches the end and then pb
will then switch to headA as said

or if pa reaches end first and then it will come over to headB in that case
'''


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Initialize two pointers, one for each linked list.
        pointerA, pointerB = headA, headB

        # Continue iterating until the two pointers meet or both reach the end.
        while pointerA != pointerB:
            # If pointerA reaches the end, redirect it to the head of list B.
            # Otherwise, move to the next node.
            pointerA = pointerA.next if pointerA else headB

            # If pointerB reaches the end, redirect it to the head of list A.
            # Otherwise, move to the next node.
            pointerB = pointerB.next if pointerB else headA

        # Return either the intersection node or None if the two lists do not intersect.
        return pointerA
