import heapq
h = heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
h.heapify(listForTree)             # for a min heap
h._heapify_max(listForTree)        # for a maxheap!!

print(listForTree)

# h._heappop_max(listForTree)

print(h._heappop_max(listForTree))