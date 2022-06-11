import heapq

h = heapq
def findKthLargest(arr, k):

    minHeap =[]
    h.heapify(minHeap)

    for num in arr:

        # the smallest will go in first
        h.heappush(num)

        # 1 2 3 4
        if len(minHeap) > k:
            h.heappop(minHeap)

    # 1 2  3 4
    return h.heappop(minHeap)




