import heapq


# TC: O (n log k) + O (N) for traversing
# log (k) for heapify

# this need to be done using minHeap
h = heapq
def findKthLargest(nums, k):



# will use a max heap here
# need to use a min heap here
    minHeap =[]
    h.heapify(minHeap)
    for num in nums:
        h.heappush(minHeap,num)
        if len(minHeap) >k:
            element = h.heappop(minHeap)
            print(element)

    return h.heappop(minHeap)
# also need to test this out
arr = [1, 2, 3, 4, 5]
print('the number is', findKthLargest(arr, 3))