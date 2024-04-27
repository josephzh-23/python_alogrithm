'''

Use the Floyd’s Cycle-Finding algorithm, also known as the “Tortoise and the Hare” approach. It uses two pointers that move through the list at different speeds.
Initialize two pointers, slow and fast, to the head of the linked list.

Move the slow pointer one step at a time, while the fast pointer moves two steps at a time.

If a cycle exists in the linked list, the fast pointer will eventually catch up to the slow pointer (they will become equal). This is because the fast pointer will keep looping inside the cycle until the slow pointer enters and they eventually meet.
Once they meet, reinitialize one of the pointers (let’s say fast) to the head of the linked list. Move both pointers one step at a time. They will meet again at the node where the cycle begins.
If no cycle exists, return null.

Part 1 question
The reason the above algorithm works is because

fast pter and slow pter will meet evnentually at 1 point

Part 2 question here
1. Move hare back to the start of the point
2. And now when they both move at 1 step at a time they will meeet at the start of the cyle

3. Fast pter will outloops the slow one by 1 lap here,

2 * slow pter = fast pter here

Fast pter = p + 2c - x
slow pter = 2 (p + c - x) = (2p + 2c - 2x = p + 2c - x )

left with
p - x = 0 here
p = x

p (starting pt until the starting pt of cycle)
x (the node in cycle from the starting pt o fthe cycle)

'''
from typing import Optional

from palindrome_linkedlist import ListNode


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize tortoise and hare pointers
    tortoise = head
    hare = head

    # Move tortoise one step and hare two steps
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next

        # Check if the hare meets the tortoise
        if tortoise == hare:
            break

    # Check if there is no cycle
    if not hare or not hare.next:
        return None

    # Reset either tortoise or hare pointer to the head
    hare = head

    # Move both pointers one step until they meet again
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next

    # Return the node where the cycle begins
    return tortoise