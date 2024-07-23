'''
Having a dummy node #1 here, and then

The approach simplifies reversing linked list nodes by breaking the
list into segments of K nodes and reversing each segment individually.
So basically, Starting from the head here, can be broken down into 3 parts here

1. reverseLinkedList() : same as reversing a linnkedlist here
2. getKthNode() :
    Given a starting node, it traverses K nodes in the list and returns the Kth node, allowing the segmentation of the list into smaller parts for reversal.

3. kReverse():

Algorithm here
1. Initi a temp to the head of the linkedlist using temp to traverse to the kth node here

2.On reaching the Kth Node, preserve the Kth Node’s next node as `nextNode`
and set the Kth Node’s next pointer to `null`.
This effectively breaks the linked list in a smaller list of size K that can be reversed and attached back.

3. Reverse the linkedlist of what u had before above

4. The reversed list now retunrs a modified list with temp at its tail and the kthNode(the next node) pointing at its head
here.  Update the `temp`s `next` pointer to `nextNode`.

5. Continue traversal,
If a segment has fewer than K Nodes, leave them unmodified and return the new head.
Use the prevLast pointer to maintain the link between the end of the previous reversed segment and the current segment.


'''
from palindrome_linkedlist import ListNode


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedList(head):
    # Initialize 'temp' at the
    # head of the linked list
    temp = head

    # Initialize 'prev' to None,
    # representing the previous node
    prev = None

    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev


# Function to get the Kth node from a given position in the linked list
def getKthNode(temp, k):
    # Decrement K as we already start from the 1st node
    k -= 1

    # Decrement K until it reaches the desired position
    while temp is not None and k > 0:
        # Decrement k as temp progresses
        k -= 1

        # Move to the next node
        temp = temp.next

    # Return the Kth node
    return temp


# Function to reverse nodes in groups of K
def kReverse(head, k):
    # Initialize a temporary node to traverse the list, this is what will be reversed as we keep going here
    temp = head

    # Initialize a pointer to track the last node of the previous group
    prevLast = None

    # Traverse through the linked list
    while temp is not None:

        # Get the Kth node of the current group
        kThNode = getKthNode(temp, k)

        # If the Kth node is NULL (not a complete group)
        if kThNode is None:
            # If there was a previous group,link the last node to the current node
            if prevLast:
                prevLast.next = temp

            # Exit the loop
            break

        # Store the next node after the Kth node
        nextNode = kThNode.next
        # Disconnect the Kth node prepare for reversal
        kThNode.next = None

        # Reverse the nodes from temp to the Kth node
        reverseLinkedList(temp)

        # Adjust the head if the reversal
        # starts from the head
        if temp == head:
            head = kThNode
        else:
            # Link the last node of the previous group to the reversed group
            prevLast.next = kThNode

        # Update the pointer to the
        # last node of the previous group
        prevLast = temp

        # Move to the next group
        temp = nextNode

    # Return the head of the
    # modified linked list
    return head


# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list with
# values 5, 4, 3, 7, 9 and 2
head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(7)
head.next.next.next.next = Node(9)
head.next.next.next.next.next = Node(2)

# Print the original linked list
print("Original Linked List: ", end="")
printLinkedList(head)

# Reverse the linked list
head = kReverse(head, 4)

# Print the reversed linked list
print("Reversed Linked List: ", end="")
printLinkedList(head)