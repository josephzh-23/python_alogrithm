import heapq
res = []
h = heapq
res.append([1, 2, 3, 4])
res.append([3, 2, 3, 4])
res.append([2, 2, 3, 4])
h.heapify(res)

while len(res) >0:
    print(h.heappop(res))