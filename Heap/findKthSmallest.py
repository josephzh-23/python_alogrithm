import heapq


# TC: O (n log k) + O (N) for traversing
# log (k) for heapify
from Heap.heap_recursive import MinHeap
from Heap.max_heap import MaxHeap

# this need to be done using minHeap
h = heapq
def findKthSmallest(nums, k):



# will use a max heap here

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