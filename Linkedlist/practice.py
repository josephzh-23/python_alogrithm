

# implement linkedlist

# insert linkedlist at the start
from Linkedlist.linkedlist import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtStart(s, val):
        if s.head == None:
            s.head= Node(val)
        else:
            newNode = Node(val)

            newNode.next = s.head
            s.head = newNode


    def append(s, data):
        newNode = Node(data)

        if s.head is None:
            s.head = newNode
            return

        cur = s.head
        while cur.next:
            cur = cur.next

        #once there
        cur.next = newNode

    # need to use temp position
    def insertAtKthPosition(s, k, data):

        newNode = Node(data)

        if k ==1:
            newNode.next = s.head
        else:
            prev = s.head

        i = 1
        while i < k-1:
            prev = prev.next

        # we need sth to store next of prev node
        temp = prev.next
        newNode.next = temp
        prev.next = newNode


# how to get the kth node
    def getKthNode(s, k):

        i = 0
        cur = s.head

        while i < k:
            cur = cur.next
            i+=1

        return cur

    def removeKthNodeFromEnd(self, k):

        # make slow and fast both point at the head
        fast = self.head
        slow = self.head

        i = 0

        '''     The  scenario where k = 1
         1 , 2 , 3, 4
         s  f
            s    f
        traverse fast node until it reaches the
        kth position
        '''
        while i <= k:
            fast = fast.next
            i += 1

        # Step 2: now move both pointers forward
        while fast:
            slow = slow.next
            fast = fast.next

        # Change the slow pter to point to the node
        # after next node

        slow.next = slow.next.next
        return slow.next
    def display(self):
        elems = []
        cur = self.head
        while cur:
            elems.append(cur.data)
            cur = cur.next
        print(elems)



list = LinkedList()
list.append(7)
list.append(1)
list.append(3)
list.append(2)
list.removeKthNodeFromEnd(1)
list.display()