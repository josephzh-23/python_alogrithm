import heapq

h = heapq
def findKthLargest(arr):

    ans = []
    h.heapify(ans)
    # 1 2 3 4 5, add number to the list here
    for num in arr:
        #
        h.heappush(ans, num)