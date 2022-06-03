


class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = None        #this is this by default

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtStart(s, data):

        node = Node(data)
        node.next = s.head
        s.head = node


    def insertAtKthPosition(s,k, data):
        node= Node(data)

        prev = s.head
        i = 0
        while i <k:
            prev = prev.next
            i+= 1

        # when get there, 5 3  4
        cur = prev.next
        prev.next = node
        node.next = cur


# how would u insert at the end?
    def append(s, data):

        # check for the case when last node is null
        node = Node(data)
        last = s.head
        while last.next:
            last= last.next

        #when u get there
        last.next = node
    def getKthNode(s, k):

        cur = s.head
        i = 0
        while i< k:
            cur =cur.next
            i +=1

        #once it's here
        return cur



    def insertAtStart(s, data):

        new = Node(data)
        new.next = s.head

        s.head = new


    def remove(s, k):

        cur = s.head
        i= 0
        while (i < k):
            cur = cur.next
            i+=1

    def remove(s, k):
        prev = s.head
        i = 0
        while (i < k):
            prev = prev.next
            i += 1

        # when u get there
        cur = prev.next
        prev.next = prev.next.next
        cur.next = None
        return cur

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next

def removeDuplciates(root):

    cur = root

    #start traversing
    while cur.next:

        #dup found
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    def push(s, data):

        node = Node(data)
        node.next = s.head
        s.head = node

class Queue:

    def __init__(self):
        self.front = self.rear = None

    # you add to the back of the queue
    def enqueue(s, item):
        node = Node(item)

        # only has the front right now
        if not s.rear:
            s.front = s.rear = node

        # it already has the rear
        else:
            s.rear = node


    def dequeue(s):
        # going for removal here from the back
        if s.isEmpty():

            return

        # if not empty then want 1st elem
        cur = s.front
        s.front = cur.next


def mergeTwoLlist(n1, n2):
    dummy = Node()
    tail = dummy

    while n1 and n2:
        if n1.val < n2.val:
            tail.next = n1.val
            #move to the next n1
            n1 = n1.next

        else:
            tail.next = l2
            l2 = l2.next

list = []
def checkIfSumExists(root, sum):

    global list
    inOrder(root, list)
    checkIfSumExistsUtil(list, sum)
def inOrder(node, list):

    if not node:
        return

    inOrder(node.left, list)
    list.append(node)
    inOrder(node.right, list)

def checkIfSumExistsUtil(arr, given):

    # for the list
    start = 0
    end = len(list) -1

    while start < end:
        sum = arr[start] + arr[end]

        if sum > given:
            end -1
        elif sum < given:
            start + 1

        elif sum == given:
            #then here we would have then the #1 issue
            return True

        else:
            return False


