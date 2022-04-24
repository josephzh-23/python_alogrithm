
# try out different solution
from Linkedlist.linkedlist import Linkedlist, Node

# list =Linkedlist()
#
# list.append(3)
# list.append(4)
# list.append(5)
# list.display()
#
# list.removeKthNodeFromEnd(1)
# list.display()
# print("the element is " +str(list.getKthNode(2)))

list2 = Linkedlist()
list2.append(3)
list2.append(4)
list2.append(5)
list2.insertAtKthPosition(1, 4)
list2.insertAtKthPosition(2, 5)
list2.insertAtStart(3)
# list2.insertAtKthPosition(3, 6)
# list2.removeKthNodeFromEnd(1)
list2.display()

# list2.reverseSinglyLinkedList()
# # list2.removeKthNodeFromEnd(1)
# list2.display()


def insertAtKthPosition(self, k, data):
    newNode = Node(data)

    i= 0
    if k==1:
        newNode.next = self.head
        self.head = newNode
    else:
        prev = self.head

        # traverse first to the right idx
        while i < k - 1:
            prev = prev.next

        cur = prev.next












