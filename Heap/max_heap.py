


import heapq

'''

This max heap here is simply a wrapper around the object that you see above 
and this is why it's so important that we are doing the code here this is 
improtant as said 
'''
class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)
class MinHeap(object):
  def __init__(self): self.h = []
  def push(self, x): heapq.heappush(self.h, x)
  def pop(self): return heapq.heappop(self.h)
  def peek(self): return self.h[0]
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def push(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def pop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val
  def peek(self): return self.h[0]

