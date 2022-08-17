import heapq

h = heapq
def findKthLargestElement(arr):

    res = []
    h.heapify(res)

    # O(n)
    for num in arr:
        res.append(num)

    if len(res) > h:
        elem = h.heappop(res)
        print(elem)