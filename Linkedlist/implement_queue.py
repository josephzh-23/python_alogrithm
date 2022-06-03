# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL
from Linkedlist.linkedlist import Node


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    '''
(enqueue)->  1   2  3   4   5   ->  (deque)
            rear          front 
        we enqueue to the rear and then dequeu from the front 
    '''

    #Again we add to the rear of the queue
    def EnQueue(self, item):
        node = Node(item)

        # this means first element
        if self.rear is None:
            self.front = self.rear = node

        # A rear already exists
        else:
            # the last element become this
            # you don't necessarily need this one below
            # self.rear.next = node
            self.rear = node

    # Method to remove an item from the front
    def DeQueue(self):

        if self.isEmpty():
            return
        cur = self.front
        self.front = cur.next

        # if this is the last one removed
        if (self.front is None):
            self.rear = None


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    # q.DeQueue()
    # q.DeQueue()
    q.EnQueue(30)
    # q.EnQueue(40)
    # q.EnQueue(50)
    # q.DeQueue()
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
