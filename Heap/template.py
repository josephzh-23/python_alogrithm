'''

Find kth largest element here leetcode

'''
from Heap.max_heap import MaxHeap, MinHeap


def findKthLargest(nums, k):

    heap = MinHeap()
    for i, num in enumerate(nums):
        if len(heap) < k:
            # if this is smaller here then this is good right?

            heap.push(num)

        else:
            # we continue to pop if not right ?

            print('this is', num, 'and', heap[0])
            if num > heap[0]:
                heap.pop()
                heap.push(num)

    for e in heap:
        print(e)

nums = [3,2,1,5,6,4]
k = 2
findKthLargest(nums, k)