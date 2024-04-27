import heapq

# You can use heap with list here

# use heap with q
h = heapq
cool = []
print(h)

cool.append([3, 'joseph'])
cool.append([4, 'mario'])
h.heapify(cool)

# after you heapify, need to pop then
h.heappop(cool)
print(cool)
