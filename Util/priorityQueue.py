from queue import PriorityQueue

# the smallest item will go at the top
q = PriorityQueue()

q.put(4)
q.put(2)
q.put(5)
q.put(1)
q.put(3)

while not q.empty():
    nextItem = q.get()
    print(nextItem)