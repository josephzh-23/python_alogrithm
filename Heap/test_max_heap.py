'''
test max heap here



'''
from Heap.max_heap import MaxHeap

v = MaxHeap()
v.push((1, 2, 3))
v.push((4, 2, 3))
v.push((2, 2, 3))

print(v.pop())