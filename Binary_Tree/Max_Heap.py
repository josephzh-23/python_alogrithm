import sys

"""
Heap with N elements has height = Log2N
    N = 6       height = 2

i: the index of child node

    Parent position = i/2
    Left child position = 2i
    Right child position = 2i + 1
"""


class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChildIndex(self, pos):

        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(s, fpos, spos):
        # self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
        #                                     self.Heap[fpos])
        s.heap[fpos], s.heap[spos] = s.heap[spos], s.heap[fpos]

    # Function to heapify the node at pos
    def maxHeapify(s, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not s.isLeaf(pos):
            if (s.heap[pos] < s.heap[s.leftChild(pos)] or
                    s.heap[pos] < s.heap[s.rightChildIndex(pos)]):

                # Swap with the left child and heapify
                # the left child
                if s.heap[s.leftChild(pos)] > s.heap[s.rightChildIndex(pos)]:

                    s.swap(pos, s.leftChild(pos))
                    s.maxHeapify(s.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    s.swap(pos, s.rightChildIndex(pos))
                    s.maxHeapify(s.rightChildIndex(pos))

    # Function to insert a node into the heap
    def insert(s, element):

        if s.size >= s.maxsize:
            return

        s.size += 1

        # insert element at the end
        s.heap[s.size] = element

        current = s.size

        while s.heap[current] > s.heap[s.parent(current)]:
            s.swap(current, s.parent(current))
            current = s.parent(current)

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(self.heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.heap[2 * i + 1]))

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):

        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


# Driver Code
if __name__ == "__main__":
    print('The maxHeap is ')

    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.Print()

    print("The Max val is " + str(maxHeap.extractMax()))
