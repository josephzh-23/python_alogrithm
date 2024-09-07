import collections

# this is the template for solving Distance_dijkstra's related algo
# in other words: weighted graph problem


# k would be the number of stops here as said
k = 2
pq = [(0, src, k + 1)]
graph = collections.defaultdict(dict)
for source, des, price in flights:
    graph[source][des] = price

print(graph)

while pq:
    nextItem = h.pop(pq)

    # the one with the least price will come off first
    price, source, stops = nextItem