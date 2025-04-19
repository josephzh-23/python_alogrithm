'''

What are the steps here?

Sort list here
 4-> 2 -> 1 -> 3

 1. Make 2 pointers slow and fast

2. Recursive sorting

We now call sortList(head) which sorts the sublist 4 -> 2, and sortList(t) which sorts the sublist 1 -> 3.

In the sublist 4 -> 2, we would further divide it into 4 and 2, and since these are single nodes, they serve as our base cases and are already sorted.

3. Merging up here

-

'''
from palindrome_linkedlist import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one element it is already sorted.
        if head is None or head.next is None:
            return head
        '''
         4-> 2 -> 1 -> 3
         
         in the above case splits into 4-> 2 
         and 1->3 
        '''
        # Find the middle of the list to split the list into two halves.
        slow, fast = head, head.next


        while fast and fast.next_node:
            slow, fast = slow.next_node, fast.next_node.next_node

        # Split the list into two halves.
        temp = slow.next_node
        slow.next_node = None
        left_half, right_half = self.sortList(head), self.sortList(temp)

        # Merge the two sorted halves.
        dummy_node = ListNode()
        current = dummy_node
        while left_half and right_half:
            # Compare the current elements of both halves and attach the smaller one to the result.
            if left_half.value <= right_half.value:
                current.next_node = left_half
                left_half = left_half.next_node
            else:
                current.next_node = right_half
                right_half = right_half.next_node
            current = current.next_node

        # Attach the remaining elements, if any, from either half.
        current.next_node = left_half or right_half

        # Return the head of the sorted list.
        return dummy_node.next_node