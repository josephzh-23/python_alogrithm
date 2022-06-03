# Python3 program to delete the
# middle of a linked list

# Linked List Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create and handle list operations
class LinkedList:

    def __init__(self):

        # Head of the list
        self.head = None

    # Add new node to the list end
    def addToList(self, data):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = newNode

    # Returns the list in string format
    def __str__(self):

        linkedListStr = ""
        temp = self.head

        while temp:
            linkedListStr += str(temp.data) + "->"
            temp = temp.next

        return linkedListStr + "NULL"

    # Method deletes middle node
    def deleteMid(self):

        # Base cases
        if (self.head is None or
                self.head.next is None):
            return

        # Initialize slow and fast pointers
        # to reach middle of linked list
        slow_Ptr = self.head
        fast_Ptr = self.head

        # Find the middle and previous of middle
        prev = None

        # To store previous of slow pointer
        while (fast_Ptr is not None and
               fast_Ptr.next is not None):
            fast_Ptr = fast_Ptr.next.next
            prev = slow_Ptr
            slow_Ptr = slow_Ptr.next

        # Delete the middle node
        prev.next = slow_Ptr.next


# Driver code
linkedList = LinkedList()

linkedList.addToList(1)
linkedList.addToList(2)
linkedList.addToList(3)
linkedList.addToList(4)

print("Given Linked List")
print(linkedList)

linkedList.deleteMid()

print("Linked List after deletion of middle")
print(linkedList)

# This code is contributed by Debidutta Rath