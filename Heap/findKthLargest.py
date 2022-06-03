import heapq


# TC: O (n log k) + O (N) for traversing
# log (k) for heapify
h = heapq
def findKthLargest(nums, k):

    heap = []
    h.heapify(heap)

    for num in nums:
        h.heappush(heap, num)
        if len(heap) >k:
            element = h.heappop(heap)
            # print(element)

    return h.heappop(heap)
# also need to test this out
arr = [1, 2, 3, 4, 5]
print('the number is', findKthLargest(arr, 2))