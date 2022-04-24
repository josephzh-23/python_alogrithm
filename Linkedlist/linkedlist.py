class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = None        #this is this by default


class Linkedlist:
    def __init__(self):
        self.head = None


    def insertAtStart(self,data):
        newNode = Node(data)

        # make new node point to the head
        newNode.next = self.head
        # head will become the new node
        self.head = newNode

        # make it equal to head
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

    #Actually need prev and node called newNode
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
            cur = prev.next
            newNode.next = cur
            prev.next = newNode


    def getKthNode(self,n):

        cur = self.head
        if n > self.length() or n< 0:
            print("Sorry invalid position")
            return None

        i = 0
        while cur:
            if i ==n:
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


    # here using the 2 pointer approach here
    # n is the position to remove the item
    def removeKthNodeFromEnd(self, n):

        #  a dummy variable that pts to head
        dummyNode = Node(0)
        dummyNode.next = self.head

        # make slow and fast node
        fast = dummyNode
        slow = dummyNode

        i = 1

        # traverse fast node until it reaches end
        while i <= n+1:
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

    # delete the node at index 'index'
    def erase(self, index):
        if index >= self.length() or index < 0:  # added 'index<0' post-video
            print("ERROR: 'Erase' Index out of range!")
            return
        curIdx = 0

        # Start at the first node
        curNode = self.head
        while True:
            lastNode = curNode
            curNode = curNode.next
            if curIdx == index:
                # here we basically skip over the curNode and make the last Node ->
                # the next of the curNode
                lastNode.next = curNode.next
                return
            curIdx += 1

        # Allows for bracket operator syntax (i.e. a[0] to return first item).
        def __getitem__(self, index):
            return self.get(index)

        #######################################################
        # Functions added after video tutorial

        # Inserts a new node at index 'index' containing data 'data'.
        # Indices begin at 0. If the provided index is greater than or
        # equal to the length of the linked list the 'data' will be appended.
        def insert(self, index, data):
            if index >= self.length() or index < 0:
                return self.append(data)
            cur_node = self.head
            prior_node = self.head
            cur_idx = 0
            while True:
                cur_node = cur_node.next
                if cur_idx == index:
                    new_node = Node(data)
                    prior_node.next = new_node
                    new_node.next = cur_node
                    return
                prior_node = cur_node
                cur_idx += 1

        # Inserts the node 'node' at index 'index'. Indices begin at 0.
        # If the 'index' is greater than or equal to the length of the linked
        # list the 'node' will be appended.
        def insert_node(self, index, node):
            if index < 0:
                print("ERROR: 'Erase' Index cannot be negative!")
                return
            if index >= self.length():  # append the node
                cur_node = self.head
                while cur_node.next != None:
                    cur_node = cur_node.next
                cur_node.next = node
                return
            cur_node = self.head
            prior_node = self.head
            cur_idx = 0
            while True:
                cur_node = cur_node.next
                if cur_idx == index:
                    prior_node.next = node
                    return
                prior_node = cur_node
                cur_idx += 1

        # Sets the data at index 'index' equal to 'data'.
        # Indices begin at 0. If the 'index' is greater than or equal
        # to the length of the linked list a warning will be printed
        # to the user.
        def set(self, index, data):
            if index >= self.length() or index < 0:
                print("ERROR: 'Set' Index out of range!")
                return
            cur_node = self.head
            cur_idx = 0
            while True:
                cur_node = cur_node.next
                if cur_idx == index:
                    cur_node.data = data
                    return
                cur_idx += 1


