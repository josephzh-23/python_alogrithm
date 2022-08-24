import heapq


# TC: O (n log k) + O (N) for traversing
# log (k) for heapify
from Heap.heap_recursive import MinHeap
from Heap.max_heap import MaxHeap

# Find smallest -> use max heap
# Find biggest -> use min heap

# this need to be done using minHeap
h = heapq
def findKthSmallest(nums, k):
# push everything in first and then start popping

    maxHeap = MaxHeap()
    for num in nums:
        maxHeap.push(num)
        print('the size is ', maxHeap.size())
        if maxHeap.size() >k:
            element = maxHeap.pop()
            # print(element)

    return maxHeap.pop()
# also need to test this out
arr = [1, 2, 3, 4, 5]
print('the number is', findKthSmallest(arr, 5))

# top frequent elements occuring in k