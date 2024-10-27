import heapq


# TC: O (n log k) + O (N) for traversing
# log (k) for heapify
from Heap.max_heap import OwnMaxHeap

# Find smallest -> use max heap
# Find biggest -> use min heap


'''
This question is hard here and then need studying here 
- That's why need studying here to make it better here 

'''
# this need to be done using minHeap
h = heapq
def findKthSmallest(nums, k):
# push everything in first and then start popping

    maxHeap = OwnMaxHeap()
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