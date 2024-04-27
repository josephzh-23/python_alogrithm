from Binary_Search_Tree.binaryTree import Node


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # when enqueue do it from the front
    def enqueue(s,data):

        node = Node(data)
        if not s.rear:
            s.front = s.rear = node
        else:
            s.rear = node

    def dequeue(s):

        if s.front:
            s.front = s.front.next
        return s.front