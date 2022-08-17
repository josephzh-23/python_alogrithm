class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = None        #this is this by default


# Remember the head will always have value of none when
# first initialized
class LinkedList:
    def __init__(self):
        self.head = None


    # init a newNode and then make new node the head
    def insertAtStart(self,data):

        if not self.head:
            self.head = Node(data)
        else:
            newNode = Node(data)

            newNode.next = self.head
            self.head = newNode



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



    # Returns the length (integer) of the linked list.
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total


    # Need 2 poitners, prev and cur
    def insertAtKthPosition(self, k, data):
        newNode = Node(data)

        # In case it's the very first one
        if k ==1:
            newNode.next = self.head
            self.head = newNode
        else:
            prev = self.head

            i =1


            #traverse first to the right idx
            while i < k-1:
                prev = prev.next
                i+=1

            # then we can try again with this
            temp = prev.next
            newNode.next = temp
            prev.next = newNode


    def getKthNode(self, k):

        cur = self.head
        if k > self.length() or k< 0:
            print("Sorry invalid position")
            return None

        i = 0
        while cur:
            if i ==k:
                return cur.data
            else:
                cur = cur.next
                i +=1


    def length(s):
        i= 0
        cur = s.head
        while cur:
            cur = cur.next
            i+=1

        return i

    def print(s):
        i = 0
        cur = s.head
        while cur:
            print("the node is", cur.data)
            cur = cur.next
            i += 1


    # here using the 2 pointer approach here
    # n is the position to remove the item
    def removeKthNodeFromEnd(self, k):

        #  a dummy variable that pts to head
        dummyNode = Node(0)
        dummyNode.next = self.head

        # make slow and fast node
        fast = dummyNode
        slow = dummyNode

        i = 0

        # traverse fast node until it reaches the
        # kth position
        while i <= k:
            fast = fast.next
            i+=1

        # also traverse both slow and fast
        while fast:
            slow = slow.next
            fast = fast.next

        # Change the slow pter to point to the node
        # after next node

        slow.next = slow.next.next
        return dummyNode.next


    # totally works here
    def reverseSinglyLinkedList(self):

        # if not self.head:
        #     return None

        cur = self.head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # when you get to the last node
        self.head = prev

    # print the linked list in traditional format
    def display(self):
        elems = []
        cur = self.head
        while cur:
            elems.append(cur.data)
            cur = cur.next
        print(elems)

    # Returns the value of the node at 'index'.
    def get(self, index):
        if index >= self.length() or index < 0:  # added 'index<0' post-video
            print("ERROR: 'Get' Index out of range!")
            return None
        curIndex = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur == index: return cur.data
            curIndex += 1

     # Need 3 references nodes
    def deleteNodeAtK(s, k):

        # remove the head
        if k == 0:
            s.head = s.head.next
            return s.head

        else:
            i = 1
            prev = s.head

            while prev and i < k:
                prev = prev.next
                i += 1

            # When you get to the node, then delete the node
            prev.next = prev.next.next
        return s.head


# to test things out
list = LinkedList()
list.insertAtKthPosition(1, 5)
list.insertAtKthPosition(2, 6)
list.display()

# print('the value deleted is', list.deleteNodeAtK(1).data)