import heapq
from collections import Counter

str = "aab"

count = Counter(str)
mheap = []

# use this instead of list comprehension
# for char, count in count.items():
#     mheap.append([-count, char])
mheap = [[-count, char] for char, count in count.items()]
heapq.heapify(mheap)  # O(n)
