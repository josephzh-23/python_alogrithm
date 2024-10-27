'''
test max heap here



'''
from Queue_heap.max_heap import MaxHeap

v = MaxHeap()
v.push((2, 3, 3))
v.push((4, 3, 3))
v.push((2, 2, 3))

print(v.pop())
print(v.pop())