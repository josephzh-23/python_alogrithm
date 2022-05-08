


class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = None        #this is this by default

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtStart(s,data):
        newNode = Node(data)

        # 1 2 3,    4
        # 4-> 1     4 -> 1
        newNode.next = s.head
        s.head = newNode
        # Adds new node containing 'data' to the end of the linked list.

    def append(self, data):

        newNode = Node(data)

        # if the new linkedlist is empty need to make this
        # new node the new head

        if self.head is None:
            self.head = newNode
            return

        # Need to traverse till last node and then insert there
        last = self.head
        while last.next:
            last = last.next

        # point to new Node
        last.next = newNode

    # prev and new Node
    def insertAtKthPosition(self, k, data):
        # 1 , 4, 3

        prev = s.head
        """
        Get to kth pos
        prev = 4
        prev.n = 5
        cur = prev.cur
        """
        newNode = Node(data)

        i = 0
        while i < k-1:
            prev = prev.next

        cur = prev.next
        prev.next = newNode
        newNode.next = cur

    def print(s):
        i = 0
        cur = s.head
        while cur:
            print("the node is", cur.data)
            cur = cur.next
            i += 1


    def removeKthNodeFromEnd(s, n):

        # rmv 5th elem here,
        dummy = Node(0)
        dummy.next = s.head

        fast = dummy
        slow = dummy

        i = 0
        while i<= n-1:
            fast = fast.next
            i+=1


        while fast.next:
            fast =fast.next
            slow = slow.next

        slow.next = slow.next.next





s = Linkedlist()
s.append(4)
s.append(5)
s.insertAtKthPosition(1, 3)
s.removeKthNodeFromEnd(1)
s.print()







