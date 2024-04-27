

# Using max heap here
# Python3 implementation of Max Heap
import sys



# Python MaxHeap
# public functions: push, peek, pop
# private functions: __swap, __floatUp, __bubbleDown

class OwnMaxHeap:
    def __init__(self, items=[]):
        super().__init__()

        # the array used for this for adding value and all that
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            # this is the original
            self.floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            # self.bubbleDown(1)

            self.bubbleDown(0)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def floatUp(s, index):

        parent = index//2

        # this means we are already at the top, otherwise
        # keep floating up like you said
        if index <= 1:
            return
        elif s.heap[index] > s.heap[parent]:
            s.swap(index, parent)
            s.floatUp(parent)

    def rightChild(self, pos):
        return (2* pos) + 1

        # Function to return the position of
        # the left child for the node currently
        # at pos

    def leftChild(self, pos):

        return 2 * pos

    # used when popping
    def bubbleDown(self, index):
        left = self.leftChild(index)
        right = self.rightChild(index)

        # this largest means the index of the largest
        # element
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubbleDown(largest)


    def size(self):
        return len(self.heap)-1

    # The testing driver function here
# m = MaxHeap([95, 3, 21])
# m.push(10)
# print(str(m.heap[0:len(m.heap)]))
# print(str(m.pop()))