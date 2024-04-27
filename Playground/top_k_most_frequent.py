import heapq
from collections import Counter

from Basics.minHeap import MinHeap

h = heapq
def topKMostFrequent(arr, k):
    heap = []
    #we can use a counter here
    counter = Counter(arr)
# and then here the code is pretty good here and then the code here is pretty good 
    # because we
    for num, freq in counter.items():
        h.heappush(heap, (-freq, num))
    print("heap is ", heap)
    result = []
    for _ in range(k):
        result.append(h.heappop(heap)[1])

    '''
    So then you ahve the above here and then 
    and then here you can havethe code 
    '''
    print("result is " , result)

topKMostFrequent([1, 1, 2, 2, 3], 2)